# Maintainer guide

This repository owns the standalone OpenMapStack presentation engine and its
bilingual 25-slide, 45-minute demo deck. It was extracted from
https://github.com/jaakla/openmapstack-skills.

## Sources of truth

- `content-et.md`, `content-en.md`: editable slide text and speaker notes.
- `layouts.json`: shared slide identities, layouts, links and timing.
- `build.py`: text validation, safe compilation and offline bundling.
- `serve.py`, `editor.html`: local editing, file watching and paired previews.
- `translate_sync.py`, `translation-state.json`: explicit incremental sync and
  the hashes of synchronized blocks.
- `app.js`, `presentation.js`, `timer.js`, `content.js`, `i18n.js`, `styles.css`, `viewer.html`, `assets/`:
  presentation behavior, interactive demo, viewer controls, design and images.
- `tests/`: deterministic engine, translation and editor contracts.
- `docs/presentation.md`: presenter guide, demo evidence and editing details.

## Working rules

Read the relevant code and current diff before making changes. Preserve both
language sources and the translation baseline. Keep text editing limited to
existing text keys; adding slides or layouts is a separate engine/content change.
The engine uses Python 3.10+ and only the standard library. Translation stays
behind a configurable command; no provider SDK or model is a renderer dependency.
Never invoke a real translator as a routine test: use the fake translator in the
test suite. Preserve screenshot attribution and the documented distinction
between real dashboard evidence and the synthetic network demo.

Run `python3 -m unittest discover -v` for engine changes and `python3 build.py`
after source changes. Commit `index.html` with its corresponding sources; it is
an intentional offline deliverable. For rendered changes, check both languages,
slide navigation, live updates, notes, screenshots and the interactive demo.
Keep README commands runnable from the repository root.
