"""Text source, translation and local editor contracts for the 45-minute deck."""
import importlib.util
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

DECK = Path(__file__).resolve().parents[1]


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, DECK / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build = load('presentation_build', 'build.py')
with patch.dict(sys.modules, {'build': build}):
    translate = load('presentation_translate', 'translate_sync.py')
    with patch.dict(sys.modules, {'translate_sync': translate}):
        serve = load('presentation_serve', 'serve.py')


class PresentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'deck'
        shutil.copytree(DECK, self.root, ignore=shutil.ignore_patterns('index.html', '__pycache__', '.git', 'tests', '.github', '.venv'))

    def edit(self, lang, key, value):
        path = self.root / f'content-{lang}.md'
        build.atomic_write(path, translate.replace_fields(path.read_text(encoding='utf-8'), {key: value}))

    def translator(self, body=None):
        script = self.root / 'translator.py'
        script.write_text(body or '''import json, sys
prompt = sys.stdin.read()
request = json.loads(prompt[prompt.index('{'):])
print(json.dumps({key: 'Translated: '+value for key,value in request['texts'].items()}))
''', encoding='utf-8')
        return shlex.join([sys.executable, str(script)])

    def test_both_decks_keep_slide_identity_and_timing(self):
        deck = build.compile_deck(self.root)
        for lang in ('et', 'en'):
            self.assertEqual(len(deck[lang]), 24)
            self.assertEqual(sum(s['minutes'] for s in deck[lang]), 45)
            self.assertTrue(all(s['notes'] for s in deck[lang]))
            self.assertFalse(any(build.SLOT.search(s['html']) for s in deck[lang]))
        self.assertEqual([s['minutes'] for s in deck['et']], [s['minutes'] for s in deck['en']])

    def test_edit_changes_only_one_language_and_escapes_html(self):
        before = build.compile_deck(self.root)
        self.edit('et', 'slide-01.text-02', '**New wording**\n<script>alert(1)</script>')
        after = build.compile_deck(self.root)
        self.assertIn('<strong>New wording</strong><br>&lt;script&gt;', after['et'][0]['html'])
        self.assertEqual(before['en'], after['en'])
        output = build.build(self.root)
        self.assertEqual(output, (self.root / 'index.html').read_text(encoding='utf-8'))
        self.assertIn('data:image/png;base64,', output)
        self.assertNotIn('__APP__', output)

    def test_reject_missing_duplicate_and_unknown_keys(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            build.parse_markdown('## slide-01.title\n\nA\n\n## slide-01.title\n\nB')
        self.edit('et', 'slide-01.title', '')
        with self.assertRaisesRegex(ValueError, 'Empty text block'):
            build.compile_deck(self.root)
        self.edit('et', 'slide-01.title', 'Restored\n\n## extra.key\n\nOops')
        with self.assertRaisesRegex(ValueError, 'unknown'):
            build.compile_deck(self.root)

    def test_script_closing_text_is_safe_in_offline_bundle(self):
        self.edit('et', 'slide-01.note-01', '</ScRiPt><script>alert(1)</script>')
        output = build.render(self.root)
        self.assertEqual(output.lower().count('</script'), 1)

    def test_prezi_code_changes_rebuild_the_watched_offline_export(self):
        editor = serve.Editor(self.root)
        version = editor.version
        camera = self.root / 'prezi.js'
        marker = '// Camera update reaches the offline bundle.'
        camera.write_text(camera.read_text(encoding='utf-8') + '\n' + marker, encoding='utf-8')
        editor.refresh()
        self.assertGreater(editor.version, version)
        self.assertIn(marker, editor.html)
        self.assertEqual(editor.html, (self.root / 'index.html').read_text(encoding='utf-8'))

    def test_replacing_fields_does_not_accumulate_blank_lines(self):
        source = (self.root / 'content-et.md').read_text(encoding='utf-8')
        fields = build.parse_markdown(source)
        self.assertEqual(translate.replace_fields(source, {'slide-01.title': fields['slide-01.title']}), source)

    def test_sync_noop_needs_no_translator(self):
        self.assertIn('No changed', translate.sync(root=self.root))

    def test_incremental_sync_preserves_unrelated_target_edits_and_supports_reverse(self):
        self.edit('et', 'slide-01.title', 'New title')
        self.edit('en', 'slide-02.title', 'Manual English title')
        before = build.read_sources(self.root)[1]['en']
        message = translate.sync(command=self.translator(), root=self.root)
        after = build.read_sources(self.root)[1]['en']
        self.assertIn('1 blocks', message)
        self.assertEqual(after['slide-01.title'], 'Translated: New title')
        self.assertEqual({k:v for k,v in before.items() if k!='slide-01.title'},
                         {k:v for k,v in after.items() if k!='slide-01.title'})
        self.assertIn('No changed', translate.sync(command=None, root=self.root))
        translate.sync(source='en', command=self.translator(), root=self.root)
        self.assertEqual(build.read_sources(self.root)[1]['et']['slide-02.title'], 'Translated: Manual English title')

    def test_sync_conflict_requires_explicit_overwrite(self):
        self.edit('et', 'slide-01.title', 'New source')
        self.edit('en', 'slide-01.title', 'Manual target')
        with self.assertRaisesRegex(ValueError, 'Both languages changed'):
            translate.sync(command=self.translator(), root=self.root)
        translate.sync(command=self.translator(), root=self.root, overwrite=True)
        self.assertEqual(build.read_sources(self.root)[1]['en']['slide-01.title'], 'Translated: New source')

    def test_bad_translation_does_not_modify_target_or_baseline(self):
        self.edit('et', 'slide-01.title', 'New source')
        paths = [self.root / 'content-en.md', self.root / 'translation-state.json']
        originals = [p.read_bytes() for p in paths]
        commands = ["print('{}')", "print('not JSON')", "print('{\"slide-01.title\": 123}')",
                    "print('{\"slide-01.title\": \"## extra.key\\\\n\\\\nBad\"}')"]
        for body in commands:
            with self.subTest(body=body):
                with self.assertRaises(ValueError):
                    translate.sync(command=self.translator(body), root=self.root)
                self.assertEqual([p.read_bytes() for p in paths], originals)

    def test_edits_during_translation_are_preserved(self):
        self.edit('et', 'slide-01.title', 'New source')
        original = (self.root / 'content-en.md').read_bytes()
        def change_while_running(*args, **kwargs):
            self.edit('et', 'slide-02.title', 'Concurrent edit')
            return subprocess.CompletedProcess(args, 0, '{"slide-01.title":"Translated"}', '')
        with patch.object(translate.subprocess, 'run', side_effect=change_while_running):
            with self.assertRaisesRegex(ValueError, 'changed during translation'):
                translate.sync(command='translator', root=self.root)
        self.assertEqual((self.root / 'content-en.md').read_bytes(), original)

    def test_local_editor_save_hot_update_conflict_and_error_recovery(self):
        editor = serve.Editor(self.root)
        server = serve.ThreadingHTTPServer(('127.0.0.1', 0), serve.handler_for(editor))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        base = f'http://127.0.0.1:{server.server_port}'
        def request(path, data=None, token=None):
            req = Request(base + path, data=json.dumps(data).encode() if data else None,
                          headers={'X-Editor-Token': token or '', 'Content-Type': 'application/json'})
            with urlopen(req) as response:
                return json.load(response)
        source = request('/api/source/et')
        version = request('/api/state')['version']
        changed = translate.replace_fields(source['markdown'], {'slide-01.text-02': 'Live wording'})
        body = dict(markdown=changed, revision=source['revision'])
        with self.assertRaises(HTTPError) as forbidden:
            request('/api/source/et', body)
        self.assertEqual(forbidden.exception.code, 403)
        forbidden.exception.close()
        saved = request('/api/source/et', body, editor.token)
        self.assertGreater(saved['version'], version)
        self.assertIn('Live wording', request('/api/deck')['deck']['et'][0]['html'])
        with self.assertRaises(HTTPError) as conflict:
            request('/api/source/et', body, editor.token)
        self.assertEqual(conflict.exception.code, 409)
        conflict.exception.close()
        invalid = changed.replace('## slide-01.title', '## wrong.key')
        failed = request('/api/source/et', dict(markdown=invalid, revision=saved['revision']), editor.token)
        self.assertTrue(failed['error'])
        self.assertEqual(failed['version'], saved['version'])
        self.assertEqual(request('/api/source/et')['markdown'], invalid)
        # Simulate saving from an external editor: GET picks it up without POST.
        build.atomic_write(self.root / 'content-et.md', changed)
        recovered = request('/api/state')
        self.assertEqual(recovered['error'], '')
        self.assertGreater(recovered['version'], failed['version'])


if __name__ == '__main__':
    unittest.main()
