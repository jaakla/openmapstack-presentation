# OpenMapStack presentation

A standalone Markdown presentation editor with two live language previews,
explicit translation sync and a self-contained offline HTML export. Includes
the bilingual Estonian/English OpenMapStack demo: 24 slides, 45 minutes, speaker
notes, dashboard screenshots and an interactive synthetic network example.

## Present online

Open the [presentation on GitHub Pages](https://jaakla.github.io/openmapstack-presentation/)
in any modern browser. No installation, account or local server is required.

- [Estonian](https://jaakla.github.io/openmapstack-presentation/?lang=et)
- [English](https://jaakla.github.io/openmapstack-presentation/?lang=en)

Use **ET / EN** to switch languages, **← / →** to navigate, **F** for fullscreen
and **N** for speaker notes. Screenshots and the interactive synthetic network
demo are included; the external Tartu dashboard needs a network connection.

The bottom toolbar hides automatically and overlays the slide without reserving
space, including in fullscreen. Move the pointer to the bottom edge, tap the small
bottom handle, or Tab to the controls to reveal it. **F / Escape** exits fullscreen.
**Overview / O** opens the slide overview; choose a slide or press
**Escape / O** to return. The overview button is in the bottom toolbar.

Slides in the overview run left to right, then top to bottom. Selecting one
preserves the language, notes and interactive demo settings. Desktop slides use
one fixed layout and scale proportionally to the available viewport, including
fullscreen and large displays. Text, graphics and spacing grow together. On small
screens, the normal view keeps its scrollable mobile layout. Everything is included
in the offline HTML.

## Start editing

Requires Python 3.10+; the engine uses only the standard library.

```bash
git clone https://github.com/jaakla/openmapstack-presentation.git
cd openmapstack-presentation
python3 serve.py
```

Open <http://127.0.0.1:8765/>. Edit Markdown in the browser or your own editor:

- [content-et.md](content-et.md): Estonian text and speaker notes.
- [content-en.md](content-en.md): English text and speaker notes.

Browser edits autosave after a short typing pause. Saved file edits also rebuild
HTML automatically. Both previews follow the slide under the cursor and preserve
navigation, open notes and interactive demo state during updates. The other
language keeps its wording until an explicit translation sync.

The MVP edits existing text blocks. Slide structure, layout, image choices,
links and timing live in [layouts.json](layouts.json). Viewer and interactive
labels remain in JavaScript. Missing, duplicate or unknown Markdown keys are
reported; previews keep the last valid build while you fix the source.

Separate preview windows:

- [Estonian preview](http://127.0.0.1:8765/index.html?lang=et&live=1)
- [English preview](http://127.0.0.1:8765/index.html?lang=en&live=1)

## Translate on demand

Choose an installed and authenticated translator command. For example:

```bash
python3 serve.py \
  --translator-command 'codex exec --ephemeral --sandbox read-only -'
```

Click **Refresh other language** to translate only changed source blocks into
the other Markdown file. Or run a manual sync:

```bash
python3 translate_sync.py --from et \
  --translator-command 'codex exec --ephemeral --sandbox read-only -'
```

Use `--from en` for English → Estonian. Both commands also accept
`OPENMAPSTACK_TRANSLATOR_COMMAND`. Claude and custom commands are documented in
[the editing guide](docs/presentation.md#explicit-translation-sync).
Translation never runs automatically on typing. Changes to the same block in
both languages are reported as conflicts; unrelated manual target edits remain.
Keep [translation-state.json](translation-state.json) with both sources.

## Build and present offline

```bash
python3 build.py
```

Open [index.html](index.html) in a browser. This single file embeds both language
decks, styles, scripts and screenshots. It requires no server, runtime or API key
to present. The external Tartu bridge dashboard requires a network connection;
the embedded screenshots and synthetic example remain available offline.

See [the presenter guide](docs/presentation.md) for navigation, the 45-minute
schedule, demo steps and evidence limitations.

## Publish updates

[GitHub Actions](.github/workflows/pages.yml) tests and builds the presentation
on every push to `main`, checks that the committed `index.html` matches its
sources, and deploys that single HTML file to GitHub Pages. After editing sources,
run `python3 build.py` and commit the updated `index.html` with them.

The repository's **Settings → Pages → Source** must be **GitHub Actions**.
To republish the current `main` without a new commit, run **Publish presentation**
from the repository's **Actions** tab using **Run workflow**. Deployment status
and the published URL appear in that workflow's `github-pages` environment.

## Develop

```bash
python3 -m unittest discover -v
python3 build.py
git diff --exit-code -- index.html
```

Tests use a fake translator and make no model calls. CI checks Python 3.10 and
3.12, the deterministic tests and synchronization of the committed offline
export. See [AGENTS.md](AGENTS.md) for maintenance guidance.

## Origin and license

Extracted from [OpenMapStack skills](https://github.com/jaakla/openmapstack-skills)
with its presentation history and the Markdown/live-editing implementation. The
presentation's original introduction was commit
[`d79cc32`](https://github.com/jaakla/openmapstack-skills/commit/d79cc32401f4e9c882b131671d70a9784d698634).
GIS skills, project validators and evaluation infrastructure remain in that
repository.

[MIT license](LICENSE), copyright 2026 Jaak Laineste. Dataset and screenshot
attributions remain in the deck and presenter guide.
