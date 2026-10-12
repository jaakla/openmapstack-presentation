"""Compile the two text-only Markdown sources into an offline presentation."""
import base64
import html
import json
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGUAGES = ('et', 'en')
KEY = re.compile(r'^## ([a-z0-9.-]+)[ \t]*$', re.MULTILINE)
SLOT = re.compile(r'\{\{([a-z0-9.-]+)\}\}')


def parse_markdown(source):
    """Read keyed text blocks; layout and slide identity cannot change here."""
    fields = {}
    matches = list(KEY.finditer(source))
    if not matches:
        raise ValueError('No text blocks found. Keep the ## slide-01.title keys.')
    for i, match in enumerate(matches):
        key = match[1]
        if key in fields:
            raise ValueError(f'Duplicate text key: {key}')
        end = matches[i + 1].start() if i + 1 < len(matches) else len(source)
        value = source[match.end():end]
        value = re.sub(r'^<!-- Slide .* -->\s*$', '', value, flags=re.MULTILINE).strip()
        if re.search(r'^## ', value, flags=re.MULTILINE):
            raise ValueError(f'Invalid text key after {key}')
        if not value:
            raise ValueError(f'Empty text block: {key}')
        fields[key] = value
    return fields


def expected_keys(slides):
    keys = set()
    for slide in slides:
        prefix = slide['id']
        keys.update((f'{prefix}.title', f'{prefix}.section'))
        keys.update(SLOT.findall(slide['html']))
        keys.update(f'{prefix}.note-{i:02d}' for i in range(1, slide['notes'] + 1))
    return keys


def validate_fields(fields, slides):
    expected = expected_keys(slides)
    missing, extra = expected - fields.keys(), fields.keys() - expected
    if missing or extra:
        raise ValueError(f'Text keys must match the fixed layouts. Missing: {sorted(missing)}; unknown: {sorted(extra)}')


def inline_markdown(value):
    """Small, escaped inline subset: emphasis, code and line breaks. No raw HTML."""
    tokens = re.split(r'(`[^`\n]+`|\*\*[^*]+\*\*|\*[^*\n]+\*)', value)
    result = []
    for token in tokens:
        if token.startswith('`') and token.endswith('`') and len(token) > 2:
            result.append('<code>' + html.escape(token[1:-1]) + '</code>')
        elif token.startswith('**') and token.endswith('**') and len(token) > 4:
            result.append('<strong>' + html.escape(token[2:-2]) + '</strong>')
        elif token.startswith('*') and token.endswith('*') and len(token) > 2:
            result.append('<em>' + html.escape(token[1:-1]) + '</em>')
        else:
            result.append(html.escape(token))
    return ''.join(result).replace('\n', '<br>')


def read_sources(root=ROOT):
    layouts = json.loads((root / 'layouts.json').read_text(encoding='utf-8'))
    sources = {}
    for lang in LANGUAGES:
        sources[lang] = parse_markdown((root / f'content-{lang}.md').read_text(encoding='utf-8'))
        validate_fields(sources[lang], layouts)
    return layouts, sources


def compile_deck(root=ROOT):
    layouts, sources = read_sources(root)
    deck = {}
    for lang in LANGUAGES:
        fields = sources[lang]
        deck[lang] = []
        for slide in layouts:
            prefix = slide['id']
            # Preformatted examples retain literal newlines rather than <br> tags.
            template = slide['html']
            parts = re.split(r'(<pre\b[^>]*>.*?</pre>)', template, flags=re.DOTALL)
            template = ''.join(SLOT.sub(lambda m: (html.escape(fields[m[1]]) if part.startswith('<pre')
                                                   else inline_markdown(fields[m[1]])), part) for part in parts)
            deck[lang].append(dict(title=fields[f'{prefix}.title'], section=fields[f'{prefix}.section'],
                                   minutes=slide['minutes'], html=template,
                                   notes=[fields[f'{prefix}.note-{i:02d}'] for i in range(1, slide['notes'] + 1)]))
    return deck


def render(root=ROOT):
    deck = compile_deck(root)
    images = {}
    for key in ('analysis', 'map', 'provenance', 'comparison', 'trips'):
        images[key] = 'data:image/png;base64,' + base64.b64encode((root / 'assets' / f'bridges-{key}.png').read_bytes()).decode('ascii')
    script = '\n'.join([
        (root / 'i18n.js').read_text(encoding='utf-8'),
        (root / 'content.js').read_text(encoding='utf-8').replace('__IMAGES__', json.dumps(images)).replace('__DECK__', json.dumps(deck, ensure_ascii=False)),
        (root / 'presentation.js').read_text(encoding='utf-8'),
        (root / 'app.js').read_text(encoding='utf-8'),
    ])
    script = re.sub(r'</script', r'<\\/script', script, flags=re.IGNORECASE)
    template = (root / 'viewer.html').read_text(encoding='utf-8')
    return template.replace('__STYLES__', (root / 'styles.css').read_text(encoding='utf-8')).replace('__APP__', script)


def atomic_write(path, source):
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                     prefix=path.name + '.', suffix='.tmp', delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(source)
    try:
        temporary.chmod(path.stat().st_mode & 0o777 if path.exists() else 0o644)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def build(root=ROOT):
    output = render(root)
    atomic_write(root / 'index.html', output)
    return output


if __name__ == '__main__':
    output = build()
    print(f'Built {ROOT / "index.html"} ({len(output.encode("utf-8")):,} bytes)')
