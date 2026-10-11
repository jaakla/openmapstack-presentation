# OpenMapStack — 45 minuti demo ja esitlus

Eesti- ja ingliskeelne esitlus tehnilise tooteettevõtte GIS-ekspertidele: 24 slaidi,
45 minuti ajastus, juhitud demo ja iga slaidi esinejamärkmed.

## Ava ja esitle

Ava [veebiesitlus](https://jaakla.github.io/openmapstack-presentation/?lang=et)
brauseris — kohalikku paigaldust pole vaja. [Ingliskeelne otseviide](https://jaakla.github.io/openmapstack-presentation/?lang=en).

Ava `index.html` brauseris. See on üks iseseisev HTML-fail: stiilid, JavaScript,
graafika ja viis tegelikku dashboardi ekraanipilti on faili sees. Slaidid ja
interaktiivne näidis töötavad ilma serveri või võrguühenduseta.

- **ET / EN jaluses:** slaidide, esinejamärkmete, graafikute ja juhtnuppude keel.
  Valik säilib järgmisel avamisel, kui brauser lubab kohalikku salvestust.
  Keelevahetus säilitab slaidi ja interaktiivse demo seaded. Päris dashboardi
  ekraanipildid ja väline demorakendus jäävad eestikeelseks.
- **Edasi / ← → / PageDown / PageUp:** järgmine või eelmine slaid.
- **Vali slaid / G:** slaidivalik koos ajakavaga.
- **Täisekraan / F:** brauseri täisekraan. Piiratud eelvaaturis ava fail tavalises brauseris.
- **Märkmed / N:** esinejamärkmed ja slaidi kavandatud aeg; paneel on samas aknas.
- **Home / End:** esimene või viimane slaid.
- **Klõps ekraanipildil:** pildi suurendus; Escape sulgeb.

## 45 minuti läbimäng

| Slaidid | Aeg | Teema |
|---|---:|---|
| 1–10 | 0–16 min | Demoküsimus, agent, skill, andmetöö ja projektileping |
| 11–16 | 16–31 min | Võrgupõhine katvus, kaalud, dashboard, päritolu, stsenaarium |
| 17–23 | 31–43 min | Iteratsioon, brauser/QGIS, kontrollid, kulu, privaatandmed |
| 24 | 43–45 min | Arutelu ja piloodi valik |

Demo kolm käiku:

1. Slaid 11: muuda jalutusaega 15 → 10 → 20 minutit ja lisa näidisvõrku sild.
2. Slaid 12: võrdle elumajade arvu ja eluruumidega kaalutud katvust.
3. Slaid 16: võrdle päris rakenduses Tuglast, Marjat ja mõlemat silda koos.

Slaidilt 14 saab avada [Tartu Emajõe sillaanalüüsi](https://tartu-sillad.jaak-laineste.workers.dev/).
Live-demo viis vaadet on Kõik kohad, Tuglase vs Marja, Teekonnad, Kaart ja
Päritolu. Võrdle sillakohti, jalgsi/rattaga liikumist, mõjumõõdikuid ja
tundlikkuse parameetreid. Poolestusaeg (gravitatsioonipõhine ligipääsetavus) ja
ajalävi (kumulatiivne ligipääsetavus) on eri parameetrid. Rakendus vajab võrku;
katkestuse korral kasuta sisse ehitatud ekraanipilte ja näidisvõrku.

## Sisu ja tõendite piir

Algkoolide 15 minuti küsimus jääb algse analüüsi lähtejuhtumiks; selle
katvusprotsenti pole välja mõeldud. Live-demo ja viis ekraanipilti näitavad
kasutaja antud Tartu sillaanalüüsi. Pildid jäädvustati 08.10.2026; rakenduse
Päritolu vaates on käivitus `run-20261002-181138`. Kaardi omistused
Maa- ja Ruumiametile, OpenStreetMapi panustajatele ja Overture Mapsile on
ekraanipiltidel säilitatud. See on rakenduse tulemuste esitlus; analüüsi ei ole
esitluse koostamisel sõltumatult uuesti arvutatud.

Interaktiivne võrk ja katvuse graafik kasutavad selgelt märgitud sünteetilisi
andmeid: servade ajakulud, 12 elumaja ja 304 eluruumi. Arvutus on Dijkstra
lühim tee suunamata võrgus. Katvuse graafik tuleneb samast arvutusest ning
hoonete kaaludest; selle joon pole käsitsi joonistatud trend. Sünteetiline sild
lisab võrguserva. Ka päris sillaanalüüs kirjeldab Päritolu vaates sildade
lisamist jalgsi- ja rattavõrku; selle arvutus ei ole sama mis esitlusskeemi oma.

Autori antud ajakulu, tokenikulu, iteratsioonid ja ajaloolised versioonid on
märgitud demokogemusena. Mudelite üldist paremusjärjestust ega muutuvat
hinnakirja ei esitata kontrollitud faktina. Tehniliste väidete aluseks on hoidla
README, CLI parser, hoidla projekti näide ja sillarakenduse Päritolu vaade.
[skills.sh](https://skills.sh/) on kataloogi näide, mitte kvaliteedigarantii.

## Edit wording in Markdown

The text sources are `content-et.md` (Estonian) and `content-en.md` (English).
They contain slide titles, section names, visible slide text, screenshot labels,
code examples and speaker notes. The existing 24 slides, timings, layouts, image
choices and link destinations are fixed in `layouts.json`. Viewer controls and
interactive diagram labels remain in `i18n.js`, `app.js` and `content.js`.

Each text block has a stable key. Edit the text below the key; keep the key itself:

```markdown
## slide-01.text-02

AI geospatial skills for reproducible map analysis
```

`title` names the slide in the chooser; `text-01`, `text-02`, etc. follow the
visible text in layout order; `note-01`, etc. are speaker notes. A chooser title
and the heading on the slide are separate blocks. Line breaks, **bold**, *italic*
and inline `code` are supported in slide text. Titles, notes and preformatted
code examples stay plain text. Raw HTML is escaped. Do not add/remove keys or
slides in this MVP. Invalid or missing keys produce an actionable build error.
Longer wording may need a visual check for fit.

### Live editor and two previews

From the repository root:

```bash
python3 serve.py
```

Open <http://127.0.0.1:8765/>. The Markdown editor saves after a short typing pause
(250 ms), and both language previews poll for changes every 500 ms. The preview
for the language being edited updates; the other keeps its wording until you
explicitly translate it. Clicking or typing in a text block navigates both
previews to that slide. Updates preserve slide position, open speaker notes and
interactive demo settings. The port can be changed with `--port`.

You can instead edit either Markdown file in your own editor. The server watches
saved files, rebuilds the standalone `index.html`, and updates open previews:

- Estonian: <http://127.0.0.1:8765/index.html?lang=et&live=1>
- English: <http://127.0.0.1:8765/index.html?lang=en&live=1>

The `lang` parameter pins each preview's initial language independently of the
saved viewer preference. Invalid Markdown is saved so you can fix it, while the
previews and `index.html` retain the last valid build. The editor displays the
error. If another editor changes a file while you have unsaved edits, the server
rejects the stale save; copy your pending wording before using **Reload source**.
Code, stylesheet or layout edits rebuild `index.html`; refresh preview pages to
pick up changes beyond text. Stop the server with Ctrl+C.

### Explicit translation sync

Translation uses a command you select. The renderer and editor need only Python
3.10+ and the standard library; translation requires your chosen tool to be
installed and authenticated. For example, start with an installed Codex CLI:

```bash
python3 serve.py \
  --translator-command 'codex exec --ephemeral --sandbox read-only -'
```

The command follows Codex's [non-interactive stdin/stdout interface](https://learn.chatgpt.com/docs/non-interactive-mode).
An installed Claude CLI can also be used:

```bash
python3 serve.py \
  --translator-command 'claude -p --output-format text --tools ""'
```

Choose the source language in the editor, then click **Refresh other language**.
This translates changed source blocks into the other Markdown file and rebuilds
HTML. It never translates on a keypress. Alternatively, run the same sync from a
terminal (use `--from en` for English → Estonian):

```bash
python3 translate_sync.py --from et \
  --translator-command 'codex exec --ephemeral --sandbox read-only -'
```

Both commands also accept `OPENMAPSTACK_TRANSLATOR_COMMAND`. A custom translator
receives a prompt on stdin ending in a JSON object with `source_language`,
`target_language`, `texts` and `current_target`. It must print only a JSON object
mapping exactly the supplied text keys to translated strings; a JSON code fence
is accepted. Commands are split into arguments without a shell. Use an executable
wrapper script if your translator needs pipes, environment setup or other shell
logic. The command has a 180-second timeout. Select a model through the chosen
tool's own configuration or command arguments.

`translation-state.json` records hashes of the last synchronized blocks. Keep it
with the two Markdown files. Only changed source blocks are sent for translation;
unrelated manual target edits remain intact. If the same block changed in both
languages, sync reports a conflict. Review the wording or rerun the terminal
command with `--overwrite` to intentionally replace those target blocks. Edits
made while translation is running cause sync to abort; retry with the latest
files. Malformed translation responses do not change the target Markdown or
baseline. Review translated wording before presenting.

### Standalone HTML build

```bash
python3 build.py
```

`index.html` remains a self-contained offline presentation with both languages
and embedded screenshots. Opening it normally needs no server, runtime or API
key. Live polling is enabled only for previews explicitly opened with `?live=1`.

### Implementation and checks

- `layouts.json`: shared, fixed slide structure and timing for both languages.
- `content.js`: screenshot helpers and runtime layout components.
- `app.js`: viewer, live text updates and interactive calculations.
- `i18n.js`: language choice and viewer controls.
- `styles.css`, `viewer.html`, `assets/`: design, shell and screenshot originals.
- `build.py`, `serve.py`, `translate_sync.py`: compilation, editing and translation.

Focused deterministic checks (with a fake translator; no model calls):

```bash
python3 -m unittest tests.test_presentation_editing -v
```
