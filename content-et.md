# OpenMapStack — ET

Edit the text beneath each `##` key. Keep keys unchanged.
Blank lines and line breaks are allowed; **bold**, *italic* and `code` work in slide text.
Titles and speaker notes are plain text. Layout, timing, links and images live in layouts.json.

<!-- Slide 1: OpenMapStack -->

## slide-01.title

OpenMapStack

## slide-01.section

Küsimus ja raamistik

## slide-01.text-01

OpenMapStack

## slide-01.text-02

AI geo-oskused korratavaks kaardianalüüsiks

## slide-01.text-03

Tartu · 15 minuti linn · 45 min tööd

## slide-01.text-04

Illustratiivne joonis (AI looming).

## slide-01.note-01

GIS-tööriistad on meil olemas. Mis juhtub, kui küsimusest ehitusprojektini viiva töö teeb agent?

## slide-01.note-02

Näita töö käiku, piiranguid ja kontrollitavaid artefakte. 45 minuti sees ei käivita me tunnist andmepipeline’i.

## slide-01.note-03

Kaardigraafika on sünteetiline ja on hiljem interaktiivne.

<!-- Slide 2: Demoküsimus: Tartu algkoolid -->

## slide-02.title

Demoküsimus: Tartu koolivõrgu katvus

## slide-02.section

Küsimus ja raamistik

## slide-02.text-01

Üks kohalik küsimus.

## slide-02.text-02

Kui hea on Tartu algkoolide katvus

## slide-02.text-03

15 minuti jalutuskäiguga?

## slide-02.text-04

1

## slide-02.text-05

Millised koolid?

## slide-02.text-06

Algkooli tüübid (era, riigi, HEV), tegutsevad asutused, sissepääsud.

## slide-02.text-07

2

## slide-02.text-08

Milline jalutuskäik?

## slide-02.text-09

Tänavavõrk, kiirused, sillad, ülekäigud ja ligipääs.

## slide-02.text-10

3

## slide-02.text-11

Katvus mille suhtes?

## slide-02.text-12

Eluruumid, elanikud või vanusegrupi lapsed? 

## slide-02.text-13

Mida täpsem küsimuse täpsustus, seda parem, aga ka kitsam on tulemus. 
Detaile asendavad: (a) variandid (b) kõige tõenäolisem otsus (c) jätkuküsimused

## slide-02.note-01

Küsi publikult suuliselt, mida katvuse all mõõta. Võta kaks kiiret vastust.

## slide-02.note-02

Lähim kool ei tõenda koolikoha kättesaadavust: vabade kohtade arv, sihtgrupi vanus ja teeninduspiirkond on lisamõõtmed.

## slide-02.note-03

Algkoolide küsimus on algne lähtejuhtum. Live-demo näitab edasiarendust: Tartu Emajõe sillakohtade võrgumõju võrdlust.

<!-- Slide 3: 45 minuti teekond -->

## slide-03.title

45 minuti teekond

## slide-03.section

Küsimus ja raamistik.

## slide-03.text-01

45 minutit küsimusest otsuseni

## slide-03.text-02

16 min

## slide-03.text-03

Agent, skill ja projekt

## slide-03.text-04

15 min

## slide-03.text-05

Meetod ja juhitud demo

## slide-03.text-06

12 min

## slide-03.text-07

Kontrolli ja korda

## slide-03.text-08

2 min

## slide-03.text-09

Otsus

## slide-03.text-10

Väärtus

## slide-03.text-11

Töö muutub loetavaks, käivitatavaks ja kontrollitavaks.

## slide-03.text-12

Uuring
## slide-03.text-13

Kas agent valis õige allika, meetodi ja katvuse nimetaja?

## slide-03.text-14

GIS-eksperdi otsus

## slide-03.text-15

Millised andmed, eeldused ja piirangud on selle otsuse jaoks vastuvõetavad?

## slide-03.note-01

Ajajaotus on slaidide kestustest arvutatud: 16 + 15 + 12 + 2 = 45 minutit.

## slide-03.note-02

Demo sisaldab offline-skeemi ja tegeliku dashboardi avamist. Võrguprobleemi korral jää ekraanipiltide ja skeemi juurde.

<!-- Slide 4: Prompt on analüüsi lähteülesanne -->

## slide-04.title

Prompt on analüüsi lähteülesanne

## slide-04.section

Küsimus ja raamistik

## slide-04.text-01

Prompt - lähteülesanne.

## slide-04.text-02

Analüüsi Tartu algkoolide 15 minuti jalgsikatvust. Täpsusta koolide valik ja mõõda katvust eluruumide põhjal.

## slide-04.text-03

Kasuta kõnnitavat teedevõrku. Salvesta allikad, ajad, CRS, eeldused ja piirangud. Loo korratav OpenMapStacki projekt, kaart ning katvuse tundlikkus ajapiiri suhtes.

## slide-04.text-04

Kui vajalik allikas või ligipääsuinfo puudub, too see nähtavale.

## slide-04.text-05

Kursiivis nõuded lisab OpenMapStacki oskus vaikimisi; neid võib, aga pole vaja promptis korrata.

## slide-04.text-06

Demoks koostatud lähteülesanne:

## slide-04.text-07

Vaata päris Claude’i vestlust ↗

## slide-04.note-01

Esimene lõik on kasutaja lähteülesanne. Kaks kursiivis lõiku selgitavad OpenMapStacki oskuse vaikimisi nõudeid; neid pole vaja tegelikus promptis korrata.

## slide-04.note-02

GIS-eksperdi panus on mõiste ja meetodi ülevaatus, mitte iga Python-rea kirjutamine.

<!-- Slide 5: Vali agent ja võimekus -->

## slide-05.title

Vali agent ja võimekus

## slide-05.section

Küsimus ja raamistik

## slide-05.text-01

Vali töövahendid.

## slide-05.text-02

Agent + oskused

## slide-05.text-03

Skills (oskused), failide kirjutamine ja koodi käivitamine.

## slide-05.text-04

Keelemudel: Opus/Sol klass

## slide-05.text-05

Keeruka ruumilise töö jaoks alusta tugevast mudelist ja piisavast mõtlemisajast (High+ reasoning).

## slide-05.text-06

Töökeskkond

## slide-05.text-07

Desktop GUI, terminal, IDE või eraldatud kaugkeskkond.

## slide-05.text-08

Küsimus
+ projektikaust
+ geotööriistad (OpenMapBench)
+ agent keelemudeliga, mis neid kasutab
+ sinu sisuline ülevaatus
──────────────────────────
kontrollitav analüüs

## slide-05.text-09

ChatGPT, Claude, Gemini ja DeepSeek on autori katsetuste kontekst. Võimekus sõltub konkreetsest agendist, mudelist ja õigustest.

## slide-05.note-01

Autori eelistus on olnud tugev mudel ning high või kõrgem mõtlemistase, kui töövahend seda võimaldab.

## slide-05.note-02

Ära esita mudelite paremusjärjestust üldise benchmark’ina. Tippmudeli lisaväärtus ja hind tuleb oma ülesande peal võrrelda.

## slide-05.note-03

Tavaline vestlusliides ja koodi käivitav agent ei anna sama tööpinda. Iga toode ei pruugi toetada sama skill-formaati.

<!-- Slide 6: Skill annab detailid, kontroll annab kindluse -->

## slide-06.title

Skill annab detailid, kontroll annab kindluse

## slide-06.section

Küsimus ja raamistik

## slide-06.text-01

Skill/oskus annab detailid.

## slide-06.text-02

Kontroll annab kindluse.

## slide-06.text-03

1

## slide-06.text-04

Juhised

## slide-06.text-05

Allikate leidmine, formaadid ja töövoog.

## slide-06.text-06

2

## slide-06.text-07

Valikud

## slide-06.text-08

Open-first stack või olemasolev ettevõtte tehnoloogia (nt ESRI).

## slide-06.text-09

3

## slide-06.text-10

Väljundid

## slide-06.text-11

Projekt, pipeline.py, päritolu, readme ja valitud väljundid.

## slide-06.text-12

4

## slide-06.text-13

Tõendid

## slide-06.text-14

Testid, kontrollid (eval’id) ja tulemuse sisuline ülevaatus.

## slide-06.text-15

Skill on loetav täiendav juhis. Selle täpsustab agentide käitumist ja väljundit.

## slide-06.text-16

Riskid: andmed, teenus, formaat või API muutub. Täpne väide tuleb allikast uuesti kontrollida.

## slide-06.text-17

AI skill-i/oskuste populaarne kataloog:

## slide-06.text-18

skills.sh

## slide-06.text-19

· Kataloog ei taga iga oskuse sõltumatut kvaliteedikontrolli.

## slide-06.note-01

Skill ei tõesta automaatselt, et meetod on õige. Ka hästi kirjutatud juhisega agent võib eksida.

## slide-06.note-02

Opinionated stack vähendab otsinguruumi, kuid ettevõtte olemasolevat stack’i ei pea välja vahetama.

## slide-06.note-03

Mudeli ja skilli panuse eristamiseks on vaja võrreldavaid katseid. Üks demo on juhtum, mitte üldistus. skills.sh avaleht vaadatud 08.10.2026.

<!-- Slide 7: Andmed kontekstist tööriistadesse -->

## slide-07.title

Andmed kontekstist tööriistadesse

## slide-07.section

Küsimus ja raamistik

## slide-07.text-01

Andmed liiguvad läbi tööriistade.

## slide-07.text-02

Andmed

## slide-07.text-03

Töövahend

## slide-07.text-04

Kontroll

## slide-07.text-05

Väike väljavõte

## slide-07.text-06

Mudeli kontekst

## slide-07.text-07

Kas näidis esindab tervikut?

## slide-07.text-08

Struktureeritud failid

## slide-07.text-09

Python · pandas · GeoPandas

## slide-07.text-10

Tüübid, join’id, nullid, geomeetria

## slide-07.text-11

Ruumiline arvutus

## slide-07.text-12

GDAL/OGR · PROJ · DuckDB · PostGIS

## slide-07.text-13

CRS, indeksid, topoloogia, ühikud

## slide-07.text-14

Andmeladu ja teenused

## slide-07.text-15

BigQuery · MotherDuck · ruutimine

## slide-07.text-16

Päringu ulatus, kulud, õigused, päritolu

## slide-07.text-17

Mudeli konteksti mahul ja hinnal pole üht universaalset piiri. Suured toorandmed jäävad failidesse või andmebaasi.

## slide-07.note-01

Mudel kirjutab arvutuse ja loeb selle kontrollitud kokkuvõtet.

## slide-07.note-02

Struktureeritud andmed ja kood võimaldavad täpset arvutust, mis eeldab siiski õiget päringut ja metoodikat.

## slide-07.note-03

Drafti 100K tokeni / 2 dollari hinnang sõltub mudelist ja tariifist. Snowflake võib olla ettevõtte stack, mitte lubadus sisseehitatud connector’ist.

<!-- Slide 8: Vestlusest korratavaks projektiks -->

## slide-08.title

Vestlusest korratavaks projektiks

## slide-08.section

Küsimus ja raamistik

## slide-08.text-01

Küsimusest kontrollitava projektini

## slide-08.text-02

1

## slide-08.text-03

Küsimus

## slide-08.text-04

Otsus, ulatus ja mõõdik.

## slide-08.text-05

2

## slide-08.text-06

Skill + agent

## slide-08.text-07

Allikad, meetod ja teostus.

## slide-08.text-08

3

## slide-08.text-09

Projekt + pipeline

## slide-08.text-10

Loetav leping ja käivitatav arvutus.

## slide-08.text-11

4

## slide-08.text-12

Kontroll + väljund

## slide-08.text-13

Päritolu, tõendid ja kasutatav kaart.

## slide-08.text-14

openmapstack validate project.yaml --preflight
openmapstack run project.yaml
openmapstack verify project.yaml

## slide-08.text-15

Vestlus aitab tööd teha. Analüüsi sõltuvused peavad olema projektis loetavad.

## slide-08.note-01

OpenMapStacki CLI ei käivita vestlusprompti. run käivitab deklareeritud canonical pipeline’i.

## slide-08.note-02

Vähem varasemast chatist sõltumist võib vähendada uut kontekstitööd; kiiruse ja hinna muutus vajab mõõtmist.

## slide-08.note-03

Käsud on kontrollitud hoidla openmapstack/cli.py parseri järgi.

<!-- Slide 9: project.yaml on analüüsi leping -->

## slide-09.title

project.yaml on analüüsi leping

## slide-09.section

Küsimus ja raamistik

## slide-09.text-01

project.yaml: analüüsi leping

## slide-09.text-02

# Tartu näite lühendatud struktuur

## slide-09.text-03

schema:

## slide-09.text-04

openmapstack-project/v1

## slide-09.text-05

project:

## slide-09.text-06

id: tartu-development-access

## slide-09.text-07

sources:

## slide-09.text-08

pedestrian_network: …

## slide-09.text-09

processing:

## slide-09.text-10

routing: …

## slide-09.text-11

overrides:

## slide-09.text-12

…

## slide-09.text-13

outputs:

## slide-09.text-14

…

## slide-09.text-15

validation:

## slide-09.text-16

…

## slide-09.text-17

Allikad ja eeldused

## slide-09.text-18

Kust, millal, mis versioon, mis litsents?

## slide-09.text-19

Sammud ja parameetrid

## slide-09.text-20

Milline arvutus, mis CRS ja milline lävi?

## slide-09.text-21

Tulemus ja tõendid

## slide-09.text-22

Mida väljastati, kuidas kontrolliti, milline käivitus?

## slide-09.text-23

Väljavõte selgitab struktuuri; see ei ole käivitatav tervikmanifest.

## slide-09.note-01

Ava vajadusel project.yaml editoris. Ära loe pikka manifesti ette.

## slide-09.note-02

Püsivad seletused tuleb panna andmeväljadele. Näite pipeline serialiseerib YAML-i uuesti ega säilita tingimata kommentaare.

## slide-09.note-03

SHA-256 ja jooksu tõendid seovad konkreetse arvutuse konkreetsete failidega.

<!-- Slide 10: Töökaust on üleantav tulemus -->

## slide-10.title

Töökaust on üleantav tulemus

## slide-10.section

Küsimus ja raamistik

## slide-10.text-01

Töökaust, mille saad üle anda.

## slide-10.text-02

project.yaml

## slide-10.text-03

# analüüsi leping

## slide-10.text-04

pipeline.py

## slide-10.text-05

# korduskäivitus

## slide-10.text-06

requirements.txt

## slide-10.text-07

# keskkond

## slide-10.text-08

data/
  source/

## slide-10.text-09

# algandmed

## slide-10.text-10

overrides/

## slide-10.text-11

# muudatused

## slide-10.text-12

derived/

## slide-10.text-13

# tulemused

## slide-10.text-14

validation/

## slide-10.text-15

# kontrollitõendid

## slide-10.text-16

runs/

## slide-10.text-17

# jooksu identiteet

## slide-10.text-18

dashboard.html
README.md

## slide-10.text-19

Failid jäävad töö tulemuseks

## slide-10.text-20

GeoPackage, GeoParquet või GeoJSON vastavalt väljundile.

## slide-10.text-21

Vaade on valik

## slide-10.text-22

Dashboard; vajadusel QGIS või ettevõtte olemasolev vaade.

## slide-10.text-23

CLI on töövahend

## slide-10.text-24

openmapstack on paigaldatud käivitaja ja kontrollija, mitte iga projekti kopeeritud fail.

## slide-10.note-01

Näites on ka project.qgz, kuid QGIS ei ole kohustuslik igale projektile.

## slide-10.note-02

Algandmed ja tuletatud tulemused on eraldi. Vahemälu peab olema eristatav ametlikust allikast.

## slide-10.note-03

Praegune teostus kasutab SHA-256, mitte draftis mainitud MD5.

<!-- Slide 11: 15 minutit mööda võrku -->

## slide-11.title

15 minutit mööda võrku

## slide-11.section

Meetod ja demo

## slide-11.text-01

15 minutit mööda võrku.

## slide-11.text-02

Võrk määrab ulatuse

## slide-11.text-03

Sillad, läbipääsud ja katkestused muudavad aega.

## slide-11.text-04

Sihtpunkt määrab ligipääsu

## slide-11.text-05

Koolini jõudmine vajab õiget sissepääsu ja snap’i.

## slide-11.text-06

Sünteetiline võrk. Ajad on servade kaalud; skeem ei kasuta Tartu andmeid.

## slide-11.note-01

Demo 1: liiguta aega 15 → 10 → 20 minutit. Osuta üle jõe paiknevatele majadele. Lisa sünteetiline sild ja näita võrgumõju.

## slide-11.note-02

Selles suunamata sünteetilises võrgus on Dijkstra arvutus; sillademo arvutab eraldi jalgsi- ja rattavõrgu stsenaariumid.

## slide-11.note-03

Kõnni suund, tõusud, väravad ja ajaline ligipääs võivad päris võrgu keerukamaks muuta. Ruumiline puhver ei ole automaatselt võrgupõhine ligipääsetavus.

<!-- Slide 12: Katvuse nimetaja muudab vastust -->

## slide-12.title

Katvuse nimetaja muudab vastust

## slide-12.section

Meetod ja demo

## slide-12.text-01

Katvus millest?

## slide-12.text-02

Olemasolev võrk

## slide-12.text-03

Uue sillaga

## slide-12.text-04

Näidisandmed · diskreetne katvus sünteetilises võrgus · ei ole Tartu tulemus.

## slide-12.text-05

Katvus = ajapiiri sees olev kaal / kogu kaal.

## slide-12.text-06

Elumajade loend ja eluruumide kaal on eri mõõdikud. Laste katvus vajab vanuserühma andmeid.

## slide-12.note-01

Demo 2: lülita eluruumide kaal välja ja tagasi sisse. Sama võrk annab teise protsendi.

## slide-12.note-02

Eluruumide kaal ei võrdu laste arvu mõõtmisega.

## slide-12.note-03

Eurostati 1 km ruudustik võib olla lisakontroll, kuid ei anna automaatselt hoone täpsusega paiknemist. Ajalooline võrdlus ei ole siin uuesti arvutatud.

<!-- Slide 13: Dashboardi viis vaadet -->

## slide-13.title

Dashboardi viis vaadet

## slide-13.section

Meetod ja demo

## slide-13.text-01

Kaart, mida saab küsitleda.

## slide-13.text-02

Sillakohtade võrdlus ja soovitus võrgumõju põhjal

## slide-13.text-03

1

## slide-13.text-04

Kõik kohad

## slide-13.text-05

Sillakohtade järjestus ja kogu jõelõigu sõelumine.

## slide-13.text-06

2

## slide-13.text-07

Tuglase vs Marja

## slide-13.text-08

Üks sild, teine sild või mõlemad.

## slide-13.text-09

3

## slide-13.text-10

Teekonnad

## slide-13.text-11

Aadressipaarid ja stsenaariumide marsruudid.

## slide-13.text-12

4

## slide-13.text-13

Kaart ja päritolu

## slide-13.text-14

Mõõdikud, kihid, allikad ja kontrollid.

## slide-13.note-01

Demorakenduse päris vaated: Kõik kohad, Tuglase vs Marja, Teekonnad, Kaart, Päritolu.

## slide-13.note-02

Algne algkoolide küsimus on kasvanud linna liikuvuse küsimuseks: kuhu lisada uus ühendus ja kelle ligipääs paraneb?

## slide-13.note-03

Kõik kohad võrdleb planeeritud sillakohti ja iga 100 m järel tuletatud sõelumiskohti. Kasutuspotentsiaal on mudeli indeks, mitte loendus.

<!-- Slide 14: Juhitud demo: võrdle sillakohti -->

## slide-14.title

Juhitud demo: võrdle sillakohti

## slide-14.section

Meetod ja demo

## slide-14.text-01

Demo: võrdle sildu ja liikumisviise.

## slide-14.text-02

Kaardikihid, mõjumõõdikud ja tundlikkuse parameetrid

## slide-14.text-03

1

## slide-14.text-04

Vaheta sillakohta

## slide-14.text-05

Võrdle Karlovat, Tuglast, Marjat ja mõlemat koos.

## slide-14.text-06

2

## slide-14.text-07

Vaheta liikumisviisi

## slide-14.text-08

Jalgsi ja jalgrattaga võivad võitjad erineda.

## slide-14.text-09

3

## slide-14.text-10

Muuda mõõdikut

## slide-14.text-11

Ligipääsetavus, ajasääst või ajaläve piires lisanduv pind.

## slide-14.text-12

Ava Tartu sillaanalüüs ↗

## slide-14.note-01

Ava Tartu sillaanalüüs uuel tab’il; jäta esitlus alles.

## slide-14.note-02

Vali ülemisest menüüst Tuglase, Marja ja Tuglase + Marja; võrdle Jalgsi ja Jalgrattaga ning Mõju / Vahe Tuglasega.

## slide-14.note-03

Kaart: vaheta Ligipääsetavuse kasv (%) → Ajasääst keskmise teekonna kohta (s). Näita, et võitja sõltub mõõdikust.

## slide-14.note-04

Tundlikkus: gravitatsioonimõõdiku poolestusaeg 5/10/20 min; lisanduva pinna ajalävi jalgsi 10/15/20 min. Need on eri parameetrid.

## slide-14.note-05

Katkestuse korral kasuta ekraanipilte ja slaidide 11–12 offline-skeemi.

<!-- Slide 15: Juhitud demo: vaata päritolu -->

## slide-15.title

Juhitud demo: vaata päritolu

## slide-15.section

Meetod ja demo

## slide-15.text-01

Tulemus peab viima allikani.

## slide-15.text-02

Andmeallikad, versioonid ja analüüsi päritolu

## slide-15.text-03

1

## slide-15.text-04

Allikas

## slide-15.text-05

Planeering, hooned, rahvastik ja teedevõrk.

## slide-15.text-06

2

## slide-15.text-07

Hetkeseis

## slide-15.text-08

Allalaadimise aeg, versioon ja käivituse identiteet.

## slide-15.text-09

3

## slide-15.text-10

Meetod

## slide-15.text-11

Elanike jaotus hoonetele, kiirused ja kaugusekaal.

## slide-15.text-12

4

## slide-15.text-13

Piirang

## slide-15.text-14

Juurdepääs, kalibreerimata kasutus ja testimata kontroll.

## slide-15.note-01

Ava Päritolu. Näita allikate loendit, eeldusi, stsenaariumi lisandusi ja töövoogu.

## slide-15.note-02

Elanikud jaotatakse elamutele netopinna alusel; see on mudelieeldus, mitte iga hoone tegelike elanike register.

## slide-15.note-03

Silla kasutuspotentsiaal on kalibreerimata gravitatsioonimudeli indeks. Päevase kasutuse suurusjärk on seotud eraldi loendusega.

## slide-15.note-04

Rakenduse raportis on 28/29 kontrolli läbitud: qgis_runtime_load on ei testitud. See ei ole sama mis läbitud.

<!-- Slide 16: Juhitud demo: üks sild või mõlemad? -->

## slide-16.title

Juhitud demo: üks sild või mõlemad?

## slide-16.section

Meetod ja demo

## slide-16.text-01

Üks sild, teine või mõlemad?

## slide-16.text-02

Tuglase ja Marja võrdlus ning teise silla lisaväärtus

## slide-16.text-03

1

## slide-16.text-04

Võrdle üksiksildu

## slide-16.text-05

Suurem kogumõju ja suurem ajasääst pole sama asi.

## slide-16.text-06

2

## slide-16.text-07

Lisa teine sild

## slide-16.text-08

Koosmõju ei pea olema üksikmõjude summa.

## slide-16.text-09

3

## slide-16.text-10

Vaata teekonda

## slide-16.text-11

Näita võrgus, milline marsruut lüheneb.

## slide-16.text-12

Algandmed + deklareeritud võrgumuudatus = stsenaarium.

## slide-16.note-01

Ava Tuglase vs Marja. Võrdle ridu Üks, teine või mõlemad ning Teise silla lisaväärtus.

## slide-16.note-02

Sillad lisatakse selles rakenduses jalgsi- ja rattavõrku. Näita erinevust üksiksilla ja kombineeritud stsenaariumi vahel.

## slide-16.note-03

Teekonnad: vali Supilinn (Marja tn) → Staadioni tn kool; T/M/TM veerg näitab eri stsenaariumi marsruuti.

## slide-16.note-04

Algandmed ei muutu; kavandatavate sildade geomeetria tuleb planeeringust ning seost kontrollib pipeline.

<!-- Slide 17: Esimene prompt ei lõpeta tööd -->

## slide-17.title

Esimene prompt ei lõpeta tööd

## slide-17.section

Kontroll ja tootearendus

## slide-17.text-01

Esimene prompt ei lõpeta tööd.

## slide-17.text-02

1.0.1

## slide-17.text-03

Brauser ühendati; kontroll korrati.

## slide-17.text-04

Kas vaade renderdub ja nupud töötavad?

## slide-17.text-05

2.0

## slide-17.text-06

Katvuse dünaamika ja Tartu asumid.

## slide-17.text-07

Jalutusaeg vs katvus; aukude tabel.

## slide-17.text-08

+ kontroll

## slide-17.text-09

Eurostati 2021. aasta 1 km ruudustik.

## slide-17.text-10

Autori järeldus: kortermajade kaal oli juba sees.

## slide-17.text-11

+ UX

## slide-17.text-12

Koolipunkti klikk teise töövahendiga.

## slide-17.text-13

Sama töökaust, selged artefaktid.

## slide-17.text-14

Iteratsioon täpsustab nii küsimust kui ka toodet.

## slide-17.text-15

Autori algkoolide demo ajalugu. Neid versioone ja järeldusi ei ole hoidla näite põhjal sõltumatult kinnitatud.

## slide-17.note-01

See slaid säilitab autori antud ajaloolise loo, mitte hoidla versioneerimise.

## slide-17.note-02

Erista meetodi parandust, allika täpsustust ja UI-parandust.

## slide-17.note-03

Agentide vahetamine toimib paremini, kui lähteülesanne ja canonical pipeline on failides.

<!-- Slide 18: Brauser ja QGIS annavad eri tõendeid -->

## slide-18.title

Brauser ja QGIS annavad eri tõendeid

## slide-18.section

Kontroll ja tootearendus

## slide-18.text-01

Kontrolli vaadet seal, kus seda kasutatakse.

## slide-18.text-02

Brauser

## slide-18.text-03

Renderdus, layout, nupud, kaardikihid ja konsooli vead.

## slide-18.text-04

QGIS / PyQGIS / MCP

## slide-18.text-05

Projekt avaneb, kihid leitakse, CRS ja stiilid sobivad.

## slide-18.text-06

Visualiseerimise oskused

## slide-18.text-07

Loetav legend, mõõdiku ühikud ja ausad võrdlused.

## slide-18.text-08

Teekonnad: marsruudi ja arvutatud aja visuaalne kontroll

## slide-18.text-09

Automaatne kontroll sõltub agendi tööriistadest ja keskkonnast. Puuduv võimekus peab jääma nähtavaks.

## slide-18.note-01

Ühendus sõltub töövahendist: sisseehitatud brauser, plugin, Playwright või kaugühendus. Universaalset Chrome’i tuge ei eeldata.

## slide-18.note-02

QGIS MCP aitab siis, kui see on paigaldatud ja kasutatav. Näite runtime kontroll võib jääda not_testable.

## slide-18.note-03

Kaart ega brauseritest ei tõenda üksi analüüsi õigsust.

<!-- Slide 19: Kolm kontrollikihti -->

## slide-19.title

Kolm kontrollikihti

## slide-19.section

Kontroll ja tootearendus

## slide-19.text-01

Mis annab tulemusele usaldusväärsuse?

## slide-19.text-02

passed

## slide-19.text-03

Kontroll jooksis ja tingimus täitus.

## slide-19.text-04

warning

## slide-19.text-05

Tulemusel on nähtav tõlgenduspiir.

## slide-19.text-06

not_testable

## slide-19.text-07

Vajalik võimekus puudus.

## slide-19.text-08

failed

## slide-19.text-09

Tingimus ei täitunud; paranda põhjus.

## slide-19.text-10

openmapstack validate project.yaml

## slide-19.text-11

# manifest ja nõutud artefaktid

## slide-19.text-12

openmapstack verify project.yaml

## slide-19.text-13

# toodetud artefaktide kontroll

## slide-19.text-14

openmapstack verify project.yaml --rerun

## slide-19.text-15

# puhas korduskäivitus

## slide-19.text-16

Reprodutseeritav vale vastus on endiselt vale vastus. Kontrolli mõistet ja otsuse sobivust.

## slide-19.note-01

Puhas korduskäivitus võib võtta kaua; ära käivita seda laval ootamatult.

## slide-19.note-02

not_testable ei ole passed. Õige raport võib sisaldada piiranguid.

## slide-19.note-03

Invariandi näide: ajapiiri suurendamine ei tohiks fikseeritud võrgus ja sama nimetajaga katvust vähendada.

<!-- Slide 20: OpenMapBench -->

## slide-19-bench.title

OpenMapBench: võrdle seadistusi

## slide-19-bench.section

Kontroll ja tootearendus

## slide-19-bench.text-01

OpenMapBench: võrdle tulemusi

## slide-19-bench.text-02

OpenMapStack

## slide-19-bench.text-03

Töövoog · projekti struktuur · kontrollid

## slide-19-bench.text-04

OpenMapBench

## slide-19-bench.text-05

Agent × mudel × skill × tööriistad

## slide-19-bench.text-06

Üks päris katse · ee-vec-002

## slide-19-bench.text-07

Ülesanne

## slide-19-bench.text-08

Tartu apteegid · vasted kuni 60 m

## slide-19-bench.text-09

Oodatud artefakt

## slide-19-bench.text-10

`pharmacy_conflation.json`

## slide-19-bench.text-11

Tegelik otsus

## slide-19-bench.text-12

`passed` · 15 vastet · 48 eri apteeki

## slide-19-bench.text-13

Säilitatud tõendid

## slide-19-bench.text-14

Väljund · etalon · raport · räsid

## slide-19-bench.text-15

Aus võrdlus: sama ülesanne, andmed ja käituskeskkond. Iga seadistusega mitu katset.

## slide-19-bench.text-16

Ava tõendipakett

## slide-19-bench.text-17

Salvestatud tulemused · protokollid erinevad, mitte mudelite paremusjärjestus

## slide-19-bench.note-01

OpenMapStack juhendab projekti tegemist ja kontrollimist. OpenMapBench võrdleb katsetatud konfiguratsioone; ühe katse passed ei tõenda mudeli üldist paremust.
OpenMapStack annab töövoo juhised, projekti struktuuri ja projekti kontrollid. OpenMapBench võrdleb katsetatud agendi, mudeli, skilli ja tööriistade konfiguratsioone.

## slide-19-bench.note-02

Salvestatud jooks 20261012T213809Z-ee-vec-002-8b792b6e: agent pi. Manifest ei täpsusta mudelit ega skilli/tööriistade täielikku konfiguratsiooni. Seetõttu näitame päris katse otsust, mitte kontrollitud konfiguratsioonide võrdlust.

## slide-19-bench.note-03

Etalon ja väljund: Overture 21, OSM 42, vasted 15, ühendamisel 48 eri apteeki ning 6 vasteta Overture’i ID-d. Täpne kontroll võrdles kõiki viit välja; ID-de järjekord ei olnud oluline. Väljundi, etaloni ja kolme sisendi räsid kontrolliti säilinud failide vastu.

## slide-19-bench.note-04

Võrdluseks fikseeri ülesande versioon, andmete räsid, etalon, hindaja, tööriistaversioonid, õigused ja aja-/kulupiir. Korda iga konfiguratsiooni mitu korda. Raporteeri läbimismäär ning aja ja kulu hajuvus; puuduvat mudelimetaandmestikku ei tohi oletada. Tõendipaketis on salvestatud ülesande koopia, sest praegune ülesandefail on vahepeal muutunud.
Ekraanipilt pärineb OpenMapBenchi võrdlusaruande kuuest tähelepanu vajavast ülesandest. Veerud: GPT-5.6 Luna ja Sol ajaloolise lepinguga; samad mudelid OpenMapStackiga prompt-only protokollis; teised salvestatud jooksud. Need on eri katsete tulemused, mitte kontrollitud mudelite või skilli mõju võrdlus: ülesande prompt ja protokoll muutusid. Pi mudel on teadmata. FAILED, TIMEOUT ja MISSING OUTPUT on erinevad tulemused. Tabel on mõlemas keeleversioonis algsel ingliskeelsel kujul; klõps ava täissuuruses. Ühe apteekide katse tõendid on eraldi lingitud.
<!-- Slide 20: Aeg ja raha: ühe juhtumi kogemus -->

## slide-20.title

Aeg ja raha: ühe juhtumi kogemus

## slide-20.section

Kontroll ja tootearendus

## slide-20.text-01

Aeg ja raha: ühe juhtumi kogemus.

## slide-20.text-02

~1

## slide-20.text-03

h

## slide-20.text-04

Üks analüüsi iteratsioon.

## slide-20.text-05

~150

## slide-20.text-06

K

## slide-20.text-07

Tokenit iteratsiooni kohta.

## slide-20.text-08

~10

## slide-20.text-09

Täiendust 1–2 nädala jooksul.

## slide-20.text-10

Esimene küsimus + kaks täpsustavat prompti andsid autori demole kasutatava suuna.

## slide-20.text-11

Jälgi kulu eraldi: mudel, kordused, ruutimine, andmeladu ja eksperdi kontrollaeg.

## slide-20.text-12

Autori hinnangud, mitte benchmark ega hinnakiri. Tellimuse kasutuslimiit ei ole sama mis tokenipõhine API kulu.

## slide-20.note-01

150K tokenit on ligikaudne kogemushinnang. Täpne arvestus vajab logi ja mudeli tariifi.

## slide-20.note-02

Drafti Pro-plaani hind ja sessiooniaken on tollane kasutuskogemus, mitte üldine hinnaväide.

## slide-20.note-03

Võrdle sama töö ja kvaliteedikriteeriumiga läbimist. Väiksem kohalik mudel on siht, mitte tõendatud võrdväärne asendus.

<!-- Slide 21: Privaatandmed ja osalised uuendused -->

## slide-21.title

Privaatandmed ja osalised uuendused

## slide-21.section

Kontroll ja tootearendus

## slide-21.text-01

Privaatandmed. Selged muudatused.

## slide-21.text-02

1

## slide-21.text-03

Privaatallikas

## slide-21.text-04

PostGIS, MotherDuck või BigQuery; piiratud ulatusega päring.

## slide-21.text-05

2

## slide-21.text-06

Hetkeseis

## slide-21.text-07

Parquet / GeoParquet koos päringu ja identiteediga.

## slide-21.text-08

3

## slide-21.text-09

Töötlus

## slide-21.text-10

CLI + SQL / DuckDB Spatial / Python.

## slide-21.text-11

4

## slide-21.text-12

Uus tulemus

## slide-21.text-13

Kontrollitud korduskäivitus ja jooksu tõend.

## slide-21.text-14

Andmemuudatus:

## slide-21.text-15

eraldi override, põhjendus ja baseline’i võrdlus.

## slide-21.text-16

Määratle, millised andmed ja kokkuvõtted agenti või mudeliteenusesse jõuavad.

## slide-21.text-17

Override ei tähenda automaatselt inkrementaalset arvutust. Uuenduse ulatus sõltub pipeline’ist.

## slide-21.note-01

Hoidlas on PostGISi, MotherDucki ja BigQuery connector’id. Ettevõtte andmeplatvorm ei pea muutuma.

## slide-21.note-02

Fail võib jääda kohalikuks, kuid tool-output ja prompt võivad andmeid mudeliteenusesse viia. Määra andmevoo piir.

## slide-21.note-03

Uus sild peab muutma õiget arvutust. Muudatusefail ei tõenda, et ruutimisgraaf taastati.

<!-- Slide 22: Tootefookus: mida edasi ehitada? -->

## slide-22.title

Tootefookus: mida edasi ehitada?

## slide-22.section

Kontroll ja tootearendus

## slide-22.text-01

Mida edasi ehitada?

## slide-22.text-02

Esimene siht: korduskasutatav analüüs

## slide-22.text-03

Lähteülesandest üleantav projekt ja kontrollitav tulemus.

## slide-22.text-04

Järgmine siht: turvaline uuendus

## slide-22.text-05

Andmevoog, õigused, override’i aktsepteerimine ja jooksude võrdlus.

## slide-22.text-06

Uuritav suund: väiksemad mudelid ja streaming

## slide-22.text-07

Kohalik täitmine, sündmuspõhised uuendused ja püsiv värskus vajavad eraldi teostust.

## slide-22.text-08

Reaalaja andmevoog ei ole demos teostatud. Näitame snapshot’il põhinevat töövoogu.

## slide-22.note-01

Arutle integratsioonipiiridest: milline osa on agent, milline worker, milline kontrollija?

## slide-22.note-02

Streaming on pakutud tulevikusuund, mitte kinnitatud tarnelubadus.

<!-- Slide 23: Mida kaasa võtta? -->

## slide-23.title

Mida kaasa võtta?

## slide-23.section

Kontroll ja tootearendus

## slide-23.text-01

Hea tulemus jääb kausta.

## slide-23.text-02

Agent teeb töö.

## slide-23.text-03

Projekt säilitab meetodi.

## slide-23.text-04

GIS-ekspert hindab tähendust.

## slide-23.text-05

OpenMapStacki hoidla ↗

## slide-23.text-06

Koduleht ja töötavad näited ↗

## slide-23.text-07

Tartu sillaanalüüs ja selle päritolu ↗

## slide-23.text-08

Tehnilised allikad: README · project.yaml · pipeline.py · cli.py · validation/latest-report.json. Esitluse alus: autori demokogemus.

## slide-23.note-01

Kolm mõtet: failipõhine leping, õige ruumiline mõiste, nähtav kontroll.

## slide-23.note-02

Installi käsk ja täpne versioon on hoidla README-s. Lingid avanevad eraldi tab’il.

<!-- Slide 24: Arutelu: kus oleks teie esimene piloot? -->

## slide-24.title

Arutelu: kus oleks teie esimene piloot?

## slide-24.section

Arutelu

## slide-24.text-01

Kus oleks teie esimene piloot?

## slide-24.text-02

Üks otsus

## slide-24.text-03

Millist ruumilist küsimust kordate täna käsitsi?

## slide-24.text-04

Üks kontroll

## slide-24.text-05

Milline viga muudaks tulemuse kasutuskõlbmatuks?

## slide-24.text-06

Üks piir

## slide-24.text-07

Millised andmed ja õigused jäävad teie keskkonda?

## slide-24.text-08

Piloodi väljund: sama küsimus, sama mõõdik, nähtav meetod, korratav jooks ja eksperdi hinnang.

## slide-24.note-01

Võta üks konkreetne pilootnäide. Kui aega vähe, vali ainult kontrollküsimus.

## slide-24.note-02

Too arutelu ülesande ja kvaliteedipiiri juurde. 45 minuti lõpp; slaidivalik aitab lisaküsimustega.
