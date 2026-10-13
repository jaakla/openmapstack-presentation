"""Local Markdown editor, file watcher and two live presentation previews."""
import argparse
import hashlib
import json
import os
import secrets
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

from build import ROOT, LANGUAGES, atomic_write, build, compile_deck
from translate_sync import sync


class Editor:
    def __init__(self, root=ROOT, translator=None):
        self.root = root
        self.translator = translator
        self.token = secrets.token_urlsafe(24)
        self.lock = threading.RLock()
        self.version = 0
        self.error = ''
        self.translation = ''
        self.translating = False
        self.html = ''
        self.deck = {}
        self.signature = None
        self.refresh()

    def markdown(self, lang):
        return (self.root / f'content-{lang}.md').read_text(encoding='utf-8')

    def revision(self, lang):
        return hashlib.sha256(self.markdown(lang).encode('utf-8')).hexdigest()

    def refresh(self):
        with self.lock:
            paths = ['content-et.md', 'content-en.md', 'layouts.json', 'content.js', 'i18n.js',
                     'presentation.js', 'timer.js', 'app.js', 'styles.css', 'viewer.html']
            paths += [str(p.relative_to(self.root)) for p in (self.root / 'assets').glob('*.png')]
            signature = tuple((p, (self.root / p).stat().st_mtime_ns, (self.root / p).stat().st_size) for p in paths)
            if signature == self.signature:
                return
            self.signature = signature
            try:
                deck = compile_deck(self.root)
                output = build(self.root)
            except (ValueError, OSError, KeyError) as exc:
                self.error = str(exc)
                return
            self.deck, self.html = deck, output
            self.error = ''
            self.version += 1

    def state(self):
        with self.lock:
            return dict(version=self.version, error=self.error, translation=self.translation,
                        translating=self.translating, canTranslate=bool(self.translator),
                        revisions={lang: self.revision(lang) for lang in LANGUAGES})

    def translate(self, source):
        try:
            message = sync(source, self.translator, self.root)
        except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
            message = f'Translation not applied: {exc}'
        with self.lock:
            self.translation = message
            self.translating = False
            self.refresh()


def handler_for(editor):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def reply(self, status, body, kind='application/json; charset=utf-8'):
            data = (json.dumps(body, ensure_ascii=False) if kind.startswith('application/json') else body).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', kind)
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            path = urlsplit(self.path).path
            editor.refresh()
            if path in ('/', '/editor.html'):
                self.reply(200, (editor.root / 'editor.html').read_text(encoding='utf-8').replace('__TOKEN__', editor.token), 'text/html; charset=utf-8')
            elif path == '/index.html':
                self.reply(200, editor.html, 'text/html; charset=utf-8')
            elif path == '/api/state':
                self.reply(200, editor.state())
            elif path == '/api/deck':
                self.reply(200, dict(version=editor.version, deck=editor.deck))
            elif path in ('/api/source/et', '/api/source/en'):
                lang = path.rsplit('/', 1)[1]
                with editor.lock:
                    self.reply(200, dict(markdown=editor.markdown(lang), revision=editor.revision(lang)))
            elif path == '/favicon.ico':
                self.reply(200, '', 'text/plain')
            else:
                self.reply(404, dict(error='Not found'))

        def do_POST(self):
            if self.headers.get('X-Editor-Token') != editor.token:
                self.reply(403, dict(error='Invalid editor token'))
                return
            try:
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 500_000:
                    raise ValueError('Invalid request size')
                body = json.loads(self.rfile.read(length))
                path = urlsplit(self.path).path
                if path in ('/api/source/et', '/api/source/en'):
                    lang = path.rsplit('/', 1)[1]
                    with editor.lock:
                        if body.get('revision') != editor.revision(lang):
                            self.reply(409, dict(error='This file changed elsewhere. Reload the source before saving.'))
                            return
                        if not isinstance(body.get('markdown'), str):
                            raise ValueError('Expected Markdown text')
                        atomic_write(editor.root / f'content-{lang}.md', body['markdown'])
                        editor.refresh()
                        self.reply(200, dict(revision=editor.revision(lang), **editor.state()))
                elif path == '/api/translate':
                    source = body.get('source')
                    if source not in LANGUAGES:
                        raise ValueError('Invalid source language')
                    with editor.lock:
                        if editor.translating:
                            self.reply(409, dict(error='Translation is already running'))
                            return
                        if not editor.translator:
                            raise ValueError('Start serve.py with --translator-command to enable translation')
                        editor.translating = True
                        editor.translation = 'Translating changed blocks…'
                        threading.Thread(target=editor.translate, args=(source,), daemon=True).start()
                    self.reply(202, dict(message='Translation started'))
                else:
                    self.reply(404, dict(error='Not found'))
            except (ValueError, OSError) as exc:
                self.reply(400, dict(error=str(exc)))
    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--translator-command', default=os.environ.get('OPENMAPSTACK_TRANSLATOR_COMMAND'))
    args = parser.parse_args()
    editor = Editor(translator=args.translator_command)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), handler_for(editor))
    stopped = threading.Event()

    def watch():
        while not stopped.wait(0.3):
            try:
                editor.refresh()
            except OSError as exc:
                with editor.lock:
                    editor.error = str(exc)

    threading.Thread(target=watch, daemon=True).start()
    print(f'Editor: http://127.0.0.1:{server.server_port}/', flush=True)
    print(f'Previews: /index.html?lang=et&live=1 and /index.html?lang=en&live=1', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stopped.set()
        server.server_close()


if __name__ == '__main__':
    main()
