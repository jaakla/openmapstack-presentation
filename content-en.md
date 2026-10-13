# OpenMapStack — EN

Edit the text beneath each `##` key. Keep keys unchanged.
Blank lines and line breaks are allowed; **bold**, *italic* and `code` work in slide text.
Titles and speaker notes are plain text. Layout, timing, links and images live in layouts.json.

<!-- Slide 1: OpenMapStack -->

## slide-01.title

OpenMapStack

## slide-01.section

Question and framework

## slide-01.text-01

OpenMapStack

## slide-01.text-02

AI geospatial skills for reproducible map analysis

## slide-01.text-03

Tartu · a 15-minute walk · 45 min

## slide-01.text-04

Method illustration, not a measured result for Tartu.

## slide-01.note-01

We already have GIS tools. What happens when an agent does the work from question to project?

## slide-01.note-02

Show the workflow, limitations and inspectable artifacts. We will not run an hour-long data pipeline during this 45-minute session.

## slide-01.note-03

The network graphic is synthetic and becomes interactive later.

<!-- Slide 2: Demo question: primary schools in Tartu -->

## slide-02.title

Demo question: primary schools in Tartu

## slide-02.section

Question and framework

## slide-02.text-01

One local question.

## slide-02.text-02

How well do Tartu’s primary schools cover the city

## slide-02.text-03

within a 15-minute walk?

## slide-02.text-04

1

## slide-02.text-05

Which schools?

## slide-02.text-06

Define primary school, operating institutions and entrances.

## slide-02.text-07

2

## slide-02.text-08

Which walk?

## slide-02.text-09

Street network, speed, bridges, crossings and access.

## slide-02.text-10

3

## slide-02.text-11

Coverage of what?

## slide-02.text-12

Dwellings, residents or children? Each denominator gives a different answer.

## slide-02.text-13

Author’s experience: the first usable result took roughly an hour. Correctness needs a separate review.

## slide-02.note-01

Ask the audience what coverage should measure. Take two quick answers.

## slide-02.note-02

The nearest school does not prove that a school place is available: capacity, age and catchment area are additional dimensions.

## slide-02.note-03

Primary schools were the original case. The live demo shows its evolution: comparing the network effects of bridge locations over the Emajõgi in Tartu.

<!-- Slide 3: The 45-minute journey -->

## slide-03.title

The 45-minute journey

## slide-03.section

Question and framework

## slide-03.text-01

45 minutes: from question to decision

## slide-03.text-02

16 min

## slide-03.text-03

Agent, skill and project

## slide-03.text-04

15 min

## slide-03.text-05

Method and guided demo

## slide-03.text-06

12 min

## slide-03.text-07

Validation and product

## slide-03.text-08

2 min

## slide-03.text-09

Discussion

## slide-03.text-10

What do we demonstrate?

## slide-03.text-11

The work becomes readable, runnable and verifiable.

## slide-03.text-12

What do we investigate?

## slide-03.text-13

Did the agent choose the right source, method and coverage denominator?

## slide-03.text-14

What does the GIS expert decide?

## slide-03.text-15

Which assumptions and limitations are acceptable for this decision?

## slide-03.note-01

The schedule is calculated from slide durations: 16 + 15 + 12 + 2 = 45 minutes.

## slide-03.note-02

The demo includes an offline illustration and the actual dashboard. If the connection fails, use the screenshots and illustration.

<!-- Slide 4: The prompt defines the analysis task -->

## slide-04.title

The prompt defines the analysis task

## slide-04.section

Question and framework

## slide-04.text-01

The prompt defines the task.

## slide-04.text-02

Analyse 15-minute walking coverage of operating primary schools in Tartu. Clarify which schools to include and measure coverage by dwellings.

## slide-04.text-03

Use the walkable network. Record sources, timestamps, CRS, assumptions and limitations. Create a reproducible OpenMapStack project, a map and a coverage sensitivity analysis for the time threshold.

## slide-04.text-04

If a required source or access information is missing, make that visible.

## slide-04.text-05

The OpenMapStack skill adds the italicised requirements by default; you do not need to repeat them in the prompt.

## slide-04.text-06

Task wording prepared for this demo.

## slide-04.text-07

View the actual Claude conversation ↗

## slide-04.note-01

The first paragraph is the user’s task. The two italicised paragraphs explain the skill’s default requirements; they do not need to appear in the actual prompt.

## slide-04.note-02

The GIS expert reviews the concept and method rather than writing every line of Python.

<!-- Slide 5: Choose the agent and its capabilities -->

## slide-05.title

Choose the agent and its capabilities

## slide-05.section

Question and framework

## slide-05.text-01

Choose a tool that can do the work.

## slide-05.text-02

Agent + skills

## slide-05.text-03

Load skills, write files and execute code.

## slide-05.text-04

Model capability

## slide-05.text-05

Start complex spatial work with a strong model and enough reasoning time.

## slide-05.text-06

Workspace

## slide-05.text-07

Desktop GUI, terminal, IDE or an isolated remote environment.

## slide-05.text-08

Question
+ project folder
+ geospatial tools
+ an agent that uses them
+ your expert review
──────────────────────────
verifiable analysis

## slide-05.text-09

ChatGPT, Claude, Gemini and DeepSeek are the context of the author’s trials. Capabilities depend on the specific agent, model and permissions.

## slide-05.note-01

The author has preferred a strong model and high or higher reasoning effort where the tool supports it.

## slide-05.note-02

Do not present a model ranking as a general benchmark. Compare the value and cost of a top model on your own task.

## slide-05.note-03

A chat interface and an agent that executes code offer different workspaces. Products may support different skill formats.

<!-- Slide 6: Skills add detail; checks add confidence -->

## slide-06.title

Skills add detail; checks add confidence

## slide-06.section

Question and framework

## slide-06.text-01

Skills add detail.

## slide-06.text-02

Checks add confidence.

## slide-06.text-03

1

## slide-06.text-04

Instructions

## slide-06.text-05

Source discovery, CRS, formats and workflow.

## slide-06.text-06

2

## slide-06.text-07

Choices

## slide-06.text-08

An open-first stack or the company’s existing technology.

## slide-06.text-09

3

## slide-06.text-10

Artifacts

## slide-06.text-11

Project, pipeline, provenance and selected outputs.

## slide-06.text-12

4

## slide-06.text-13

Evidence

## slide-06.text-14

Tests, evaluations and expert review of the result.

## slide-06.text-15

A skill is readable, versioned guidance. Its value can be measured in agent behaviour.

## slide-06.text-16

Risk: a service, format or API changes. Verify specific claims against the source again.

## slide-06.text-17

Example skill catalogue:

## slide-06.text-18

skills.sh

## slide-06.text-19

· a listing does not imply independent quality assurance.

## slide-06.note-01

A skill does not automatically prove the method is correct. An agent can make mistakes even with good instructions.

## slide-06.note-02

An opinionated stack narrows the search space; a company need not replace its existing stack.

## slide-06.note-03

Separating the contribution of the model and skill requires comparable trials. One demo is a case study, not a generalisation. skills.sh homepage checked on 8 October 2026.

<!-- Slide 7: From context to data tools -->

## slide-07.title

From context to data tools

## slide-07.section

Question and framework

## slide-07.text-01

Data moves into tools.

## slide-07.text-02

Data work

## slide-07.text-03

Tool

## slide-07.text-04

What does the expert check?

## slide-07.text-05

Small sample

## slide-07.text-06

Model context

## slide-07.text-07

Does the sample represent the whole?

## slide-07.text-08

Structured files

## slide-07.text-09

Python · pandas · GeoPandas

## slide-07.text-10

Types, joins, nulls, geometry

## slide-07.text-11

Spatial computation

## slide-07.text-12

GDAL/OGR · PROJ · DuckDB · PostGIS

## slide-07.text-13

CRS, indexes, topology, units

## slide-07.text-14

Warehouses and services

## slide-07.text-15

BigQuery · MotherDuck · routing

## slide-07.text-16

Query scope, cost, permissions, provenance

## slide-07.text-17

There is no universal limit or price for model context. Large raw datasets stay in files or databases.

## slide-07.note-01

The model writes the computation and reads a checked summary of its output.

## slide-07.note-02

Structured data and code enable precise computation, but still require the right query and methodology.

## slide-07.note-03

The draft’s 100K-token / $2 estimate depends on the model and tariff. Snowflake may be part of the company stack; this is not a promise of a built-in connector.

<!-- Slide 8: From conversation to reproducible project -->

## slide-08.title

From conversation to reproducible project

## slide-08.section

Question and framework

## slide-08.text-01

From question to a verifiable project

## slide-08.text-02

1

## slide-08.text-03

Question

## slide-08.text-04

Decision, scope and metric.

## slide-08.text-05

2

## slide-08.text-06

Skill + agent

## slide-08.text-07

Sources, method and implementation.

## slide-08.text-08

3

## slide-08.text-09

Project + pipeline

## slide-08.text-10

A readable contract and runnable computation.

## slide-08.text-11

4

## slide-08.text-12

Checks + output

## slide-08.text-13

Provenance, evidence and a usable map.

## slide-08.text-14

openmapstack validate project.yaml --preflight
openmapstack run project.yaml
openmapstack verify project.yaml

## slide-08.text-15

Conversation helps get the work done. The analysis dependencies must be readable in the project.

## slide-08.note-01

The OpenMapStack CLI does not execute a chat prompt. run executes the declared canonical pipeline.

## slide-08.note-02

Less dependence on prior chat may reduce context work; changes in speed and cost need measurement.

## slide-08.note-03

The commands were checked against the parser in openmapstack/cli.py.

<!-- Slide 9: project.yaml is the analysis contract -->

## slide-09.title

project.yaml is the analysis contract

## slide-09.section

Question and framework

## slide-09.text-01

project.yaml: the analysis contract

## slide-09.text-02

# Abbreviated Tartu example

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

Sources and assumptions

## slide-09.text-18

Where, when, which version and licence?

## slide-09.text-19

Steps and parameters

## slide-09.text-20

Which computation, CRS and threshold?

## slide-09.text-21

Results and evidence

## slide-09.text-22

What was produced, how was it checked, which run?

## slide-09.text-23

This excerpt explains the structure; it is not a complete runnable manifest.

## slide-09.note-01

Open project.yaml in an editor if needed. Do not read a long manifest aloud.

## slide-09.note-02

Persistent explanations belong in data fields. The example pipeline reserialises YAML and may not preserve comments.

## slide-09.note-03

SHA-256 and run evidence link a specific computation to specific files.

<!-- Slide 10: A workspace you can hand over -->

## slide-10.title

A workspace you can hand over

## slide-10.section

Question and framework

## slide-10.text-01

A workspace you can hand over.

## slide-10.text-02

project.yaml

## slide-10.text-03

# analysis contract

## slide-10.text-04

pipeline.py

## slide-10.text-05

# rerun

## slide-10.text-06

requirements.txt

## slide-10.text-07

# environment

## slide-10.text-08

data/
  source/

## slide-10.text-09

# source data

## slide-10.text-10

overrides/

## slide-10.text-11

# changes

## slide-10.text-12

derived/

## slide-10.text-13

# results

## slide-10.text-14

validation/

## slide-10.text-15

# check evidence

## slide-10.text-16

runs/

## slide-10.text-17

# run identity

## slide-10.text-18

dashboard.html
README.md

## slide-10.text-19

Files are the deliverable

## slide-10.text-20

GeoPackage, GeoParquet or GeoJSON, depending on the output.

## slide-10.text-21

The view is a choice

## slide-10.text-22

Dashboard; QGIS or an existing company view where needed.

## slide-10.text-23

The CLI is a tool

## slide-10.text-24

openmapstack is an installed runner and checker, rather than a file copied into every project.

## slide-10.note-01

The example also has project.qgz, but QGIS is not mandatory for every project.

## slide-10.note-02

Source data and derived results are separate. Distinguish a cache from the authoritative source.

## slide-10.note-03

The current implementation uses SHA-256, not the MD5 mentioned in the draft.

<!-- Slide 11: 15 minutes along the network -->

## slide-11.title

15 minutes along the network

## slide-11.section

Method and demo

## slide-11.text-01

15 minutes along the network.

## slide-11.text-02

The network defines reach

## slide-11.text-03

Bridges, passages and breaks change travel time.

## slide-11.text-04

The destination defines access

## slide-11.text-05

Reaching a school requires the right entrance and network snapping.

## slide-11.text-06

Synthetic network. Times are edge weights; this illustration does not use Tartu data.

## slide-11.note-01

Demo 1: change the time 15 → 10 → 20 minutes. Point out homes across the river. Add the synthetic bridge and show its network effect.

## slide-11.note-02

This undirected synthetic graph uses Dijkstra. The bridges demo computes separate walking and cycling network scenarios.

## slide-11.note-03

Direction, slopes, gates and time-dependent access can make real networks more complex. A spatial buffer does not automatically measure network accessibility.

<!-- Slide 12: The coverage denominator changes the answer -->

## slide-12.title

The coverage denominator changes the answer

## slide-12.section

Method and demo

## slide-12.text-01

Coverage of what?

## slide-12.text-02

Existing network

## slide-12.text-03

With a new bridge

## slide-12.text-04

Example data · discrete coverage in a synthetic network · not a Tartu result.

## slide-12.text-05

Coverage = weight within the time threshold / total weight.

## slide-12.text-06

Counting residential buildings and weighting by dwellings are different metrics. Coverage of children needs age-group data.

## slide-12.note-01

Demo 2: turn dwelling weights off and on. The same network gives a different percentage.

## slide-12.note-02

Dwelling weights do not measure the number of children.

## slide-12.note-03

Eurostat’s 1 km grid can be an additional check, but does not automatically locate people at building resolution. The historical comparison has not been recomputed here.

<!-- Slide 13: Five dashboard views -->

## slide-13.title

Five dashboard views

## slide-13.section

Method and demo

## slide-13.text-01

A map you can interrogate.

## slide-13.text-02

Bridge location comparison and a network-based recommendation

## slide-13.text-03

1

## slide-13.text-04

All locations

## slide-13.text-05

Rank bridge locations and screen the entire river section.

## slide-13.text-06

2

## slide-13.text-07

Tuglase vs Marja

## slide-13.text-08

One bridge, the other or both.

## slide-13.text-09

3

## slide-13.text-10

Routes

## slide-13.text-11

Address pairs and scenario routes.

## slide-13.text-12

4

## slide-13.text-13

Map and provenance

## slide-13.text-14

Metrics, layers, sources and checks.

## slide-13.note-01

Actual application tabs (Estonian): Kõik kohad (All locations), Tuglase vs Marja, Teekonnad (Routes), Kaart (Map), Päritolu (Provenance).

## slide-13.note-02

The original primary-school question evolved into an urban mobility question: where to add a connection and whose access improves?

## slide-13.note-03

All locations compares planned bridges and screening locations derived every 100 m. Usage potential is a model index, not an observed count.

<!-- Slide 14: Guided demo: compare bridge locations -->

## slide-14.title

Guided demo: compare bridge locations

## slide-14.section

Method and demo

## slide-14.text-01

Demo: compare bridges and travel modes.

## slide-14.text-02

Map layers, impact metrics and sensitivity parameters

## slide-14.text-03

1

## slide-14.text-04

Change bridge location

## slide-14.text-05

Compare Karlova, Tuglase, Marja and both together.

## slide-14.text-06

2

## slide-14.text-07

Change travel mode

## slide-14.text-08

Walking and cycling may produce different winners.

## slide-14.text-09

3

## slide-14.text-10

Change the metric

## slide-14.text-11

Accessibility, time saved or added floor area within a time threshold.

## slide-14.text-12

Open Tartu bridge analysis ↗

## slide-14.note-01

Open the Tartu bridge analysis in a new tab; keep the presentation open. The live application and screenshots are in Estonian.

## slide-14.note-02

Use the top menu to select Tuglase, Marja and Tuglase + Marja. Compare Jalgsi (Walking), Jalgrattaga (Cycling), Mõju (Impact) and Vahe Tuglasega (Difference from Tuglase).

## slide-14.note-03

Map: switch Ligipääsetavuse kasv (%) (Accessibility increase) to Ajasääst keskmise teekonna kohta (s) (Average time saved per trip). Show that the winner depends on the metric.

## slide-14.note-04

Sensitivity: gravity metric half-life 5/10/20 min; the walking threshold for added floor area 10/15/20 min. These are different parameters.

## slide-14.note-05

If interrupted, use the screenshots and the offline illustration on slides 11–12.

<!-- Slide 15: Guided demo: inspect provenance -->

## slide-15.title

Guided demo: inspect provenance

## slide-15.section

Method and demo

## slide-15.text-01

The result must lead back to its sources.

## slide-15.text-02

Data sources, versions and analysis provenance

## slide-15.text-03

1

## slide-15.text-04

Source

## slide-15.text-05

Planning, buildings, population and road network.

## slide-15.text-06

2

## slide-15.text-07

Snapshot

## slide-15.text-08

Download time, version and run identity.

## slide-15.text-09

3

## slide-15.text-10

Method

## slide-15.text-11

Population allocation to buildings, speeds and distance decay.

## slide-15.text-12

4

## slide-15.text-13

Limitation

## slide-15.text-14

Access, uncalibrated usage and an untested check.

## slide-15.note-01

Open Päritolu (Provenance). Show the source list, assumptions, scenario additions and workflow.

## slide-15.note-02

Residents are allocated to residential buildings by net floor area. This is a model assumption, not a register of actual residents in each building.

## slide-15.note-03

Bridge usage potential is an uncalibrated gravity-model index. The order of magnitude of daily usage is tied to a separate observed count.

## slide-15.note-04

The application report shows 28/29 checks passed: qgis_runtime_load is not tested. That is not a pass.

<!-- Slide 16: Guided demo: one bridge or both? -->

## slide-16.title

Guided demo: one bridge or both?

## slide-16.section

Method and demo

## slide-16.text-01

One bridge, the other or both?

## slide-16.text-02

Tuglase and Marja comparison and the value of a second bridge

## slide-16.text-03

1

## slide-16.text-04

Compare individual bridges

## slide-16.text-05

Greater total impact and greater time savings are different things.

## slide-16.text-06

2

## slide-16.text-07

Add the second bridge

## slide-16.text-08

The combined effect need not equal the sum of individual effects.

## slide-16.text-09

3

## slide-16.text-10

Inspect a route

## slide-16.text-11

Show which network route becomes shorter.

## slide-16.text-12

Source data + a declared network change = a scenario.

## slide-16.note-01

Open Tuglase vs Marja. Compare Üks, teine või mõlemad (One, the other or both) and Teise silla lisaväärtus (Value of the second bridge).

## slide-16.note-02

This application adds bridges to walking and cycling networks. Show the difference between individual and combined scenarios.

## slide-16.note-03

Teekonnad (Routes): select Supilinn (Marja tn) → Staadioni tn kool. The T/M/TM column shows the scenario route.

## slide-16.note-04

Source data stays unchanged. Proposed bridge geometry comes from planning data; the pipeline checks the network connection.

<!-- Slide 17: The first prompt does not finish the job -->

## slide-17.title

The first prompt does not finish the job

## slide-17.section

Validation and product development

## slide-17.text-01

The first prompt does not finish the job.

## slide-17.text-02

1.0.1

## slide-17.text-03

Browser connected; checks repeated.

## slide-17.text-04

Does the view render? Do the buttons work?

## slide-17.text-05

2.0

## slide-17.text-06

Coverage dynamics and Tartu districts.

## slide-17.text-07

Walking time vs coverage; a table of gaps.

## slide-17.text-08

+ check

## slide-17.text-09

Eurostat’s 2021 population grid, 1 km.

## slide-17.text-10

Author’s finding: apartment weights were already included.

## slide-17.text-11

+ UX

## slide-17.text-12

School point clicks added with another tool.

## slide-17.text-13

The same workspace and clear artifacts.

## slide-17.text-14

Iteration refines both the question and the product.

## slide-17.text-15

The author’s primary-school demo history. These versions and findings have not been independently confirmed from the repository example.

## slide-17.note-01

This slide preserves the author’s historical account, not repository versioning.

## slide-17.note-02

Distinguish improvements to the method, source clarification and UI fixes.

## slide-17.note-03

Switching agents works better when the task and canonical pipeline are in files.

<!-- Slide 18: Browser and QGIS provide different evidence -->

## slide-18.title

Browser and QGIS provide different evidence

## slide-18.section

Validation and product development

## slide-18.text-01

Check the view where it is used.

## slide-18.text-02

Browser

## slide-18.text-03

Rendering, layout, buttons, map layers and console errors.

## slide-18.text-04

QGIS / PyQGIS / MCP

## slide-18.text-05

The project opens, layers resolve, CRS and styles are appropriate.

## slide-18.text-06

Visualisation skills

## slide-18.text-07

Readable legends, metric units and honest comparisons.

## slide-18.text-08

Routes: visually checking the route and computed time

## slide-18.text-09

Automatic checks depend on the agent’s tools and environment. Missing capabilities must remain visible.

## slide-18.note-01

Connection depends on the tool: built-in browser, plugin, Playwright or remote access. Universal Chrome support is not assumed.

## slide-18.note-02

QGIS MCP helps when it is installed and available. The example runtime check may remain not_testable.

## slide-18.note-03

A map or browser test alone does not prove that the analysis is correct.

<!-- Slide 19: Three layers of validation -->

## slide-19.title

Three layers of validation

## slide-19.section

Validation and product development

## slide-19.text-01

What makes a result trustworthy?

## slide-19.text-02

passed

## slide-19.text-03

The check ran and the condition held.

## slide-19.text-04

warning

## slide-19.text-05

A visible limitation affects interpretation.

## slide-19.text-06

not_testable

## slide-19.text-07

A required capability was unavailable.

## slide-19.text-08

failed

## slide-19.text-09

The condition did not hold; fix the cause.

## slide-19.text-10

openmapstack validate project.yaml

## slide-19.text-11

# manifest and required artifacts

## slide-19.text-12

openmapstack verify project.yaml

## slide-19.text-13

# inspect produced artifacts

## slide-19.text-14

openmapstack verify project.yaml --rerun

## slide-19.text-15

# clean rerun

## slide-19.text-16

A reproducible wrong answer is still wrong. Check the concept and fitness for the decision.

## slide-19.note-01

A clean rerun may take a long time. Do not start it unexpectedly on stage.

## slide-19.note-02

not_testable is not passed. A valid report may include limitations.

## slide-19.note-03

Example invariant: increasing the time threshold should not reduce coverage on a fixed network with the same denominator.

<!-- Slide 20: OpenMapBench -->

## slide-19-bench.title

OpenMapBench: compare configurations

## slide-19-bench.section

Validation and product development

## slide-19-bench.text-01

OpenMapBench: compare results

## slide-19-bench.text-02

OpenMapStack

## slide-19-bench.text-03

Workflow · project structure · checks

## slide-19-bench.text-04

OpenMapBench

## slide-19-bench.text-05

Agent × model × skill × tools

## slide-19-bench.text-06

One recorded trial · ee-vec-002

## slide-19-bench.text-07

Task

## slide-19-bench.text-08

Tartu pharmacies · matches within 60 m

## slide-19-bench.text-09

Expected artifact

## slide-19-bench.text-10

`pharmacy_conflation.json`

## slide-19-bench.text-11

Actual verdict

## slide-19-bench.text-12

`passed` · 15 pairs · 48 distinct pharmacies

## slide-19-bench.text-13

Retained evidence

## slide-19-bench.text-14

Output · reference · report · hashes

## slide-19-bench.text-15

Fair comparison: same task, data and runtime. Repeat trials for every configuration.

## slide-19-bench.text-16

Open evidence bundle

## slide-19-bench.text-17

Recorded results · protocols differ; not a model ranking

## slide-19-bench.note-01

OpenMapStack guides project work and project checks. OpenMapBench compares tested configurations; one passing trial does not establish a model’s general superiority.
OpenMapStack supplies workflow guidance, project structure and project checks. OpenMapBench compares tested agent/model/skill/tool configurations.

## slide-19-bench.note-02

Recorded run 20261012T213809Z-ee-vec-002-8b792b6e used agent pi. The manifest does not identify the model or the full skill/tool configuration. This is a real trial verdict, not a controlled comparison between configurations.

## slide-19-bench.note-03

Reference and output: 21 Overture pharmacies, 42 OSM pharmacies, 15 matched pairs, 48 distinct pharmacies after merging and 6 unmatched Overture IDs. The exact check compared all five fields; ID order was ignored. Output, reference and all three input hashes were checked against retained files.

## slide-19-bench.note-04

For comparison, fix the task version, data hashes, reference, evaluator, tool versions, permissions and time/cost limits. Repeat each configuration several times. Report pass rate and variation in time and cost; never infer missing model metadata. The evidence bundle retains the staged task snapshot because the current task file has since changed.
The screenshot shows six tasks requiring attention in the OpenMapBench comparison report. Columns: GPT-5.6 Luna and Sol with the historical contract; those models with OpenMapStack under the prompt-only protocol; other recorded runs. These are recorded outcomes, not a controlled comparison of models or skill effects: task prompts and protocols changed. The Pi model is unknown. FAILED, TIMEOUT and MISSING OUTPUT are distinct outcomes. The original English table is retained in both language versions; click to enlarge. The single pharmacy trial has its own linked evidence.
<!-- Slide 20: Time and money: one case study -->

## slide-20.title

Time and money: one case study

## slide-20.section

Validation and product development

## slide-20.text-01

Time and money: one case study.

## slide-20.text-02

~1

## slide-20.text-03

h

## slide-20.text-04

One analysis iteration.

## slide-20.text-05

~150

## slide-20.text-06

K

## slide-20.text-07

Tokens per iteration.

## slide-20.text-08

~10

## slide-20.text-09

Updates over 1–2 weeks.

## slide-20.text-10

The initial question + two follow-up prompts gave the author’s demo a usable direction.

## slide-20.text-11

Track costs separately: model, retries, routing, warehouse and expert review time.

## slide-20.text-12

Author’s estimates, not a benchmark or price list. Subscription usage limits differ from token-based API spend.

## slide-20.note-01

150K tokens is an approximate experience-based estimate. Exact accounting requires logs and the model tariff.

## slide-20.note-02

The draft’s Pro-plan price and session window describe the author’s experience at the time, not general pricing.

## slide-20.note-03

Compare the same task and quality criteria. A smaller local model is a goal, not a proven equivalent replacement.

<!-- Slide 21: Private data and partial updates -->

## slide-21.title

Private data and partial updates

## slide-21.section

Validation and product development

## slide-21.text-01

Private data. Explicit changes.

## slide-21.text-02

1

## slide-21.text-03

Private source

## slide-21.text-04

PostGIS, MotherDuck or BigQuery; a scoped query.

## slide-21.text-05

2

## slide-21.text-06

Snapshot

## slide-21.text-07

Parquet / GeoParquet with query and identity.

## slide-21.text-08

3

## slide-21.text-09

Processing

## slide-21.text-10

CLI + SQL / DuckDB Spatial / Python.

## slide-21.text-11

4

## slide-21.text-12

New result

## slide-21.text-13

A validated rerun and run evidence.

## slide-21.text-14

Data change:

## slide-21.text-15

a separate override, rationale and baseline comparison.

## slide-21.text-16

Define which data and summaries reach the agent or model service.

## slide-21.text-17

An override does not automatically mean incremental computation. Update scope depends on the pipeline.

## slide-21.note-01

The repository has PostGIS, MotherDuck and BigQuery connectors. The company’s data platform need not change.

## slide-21.note-02

A file may remain local, but tool output and prompts can carry data to a model service. Define the data-flow boundary.

## slide-21.note-03

A new bridge must change the correct computation. A change file does not prove the routing graph was rebuilt.

<!-- Slide 22: Product focus: what should we build next? -->

## slide-22.title

Product focus: what should we build next?

## slide-22.section

Validation and product development

## slide-22.text-01

What should we build next?

## slide-22.text-02

First goal: reusable analysis

## slide-22.text-03

From a task to a transferable project and a verifiable result.

## slide-22.text-04

Next goal: safe updates

## slide-22.text-05

Data flow, permissions, accepting overrides and comparing runs.

## slide-22.text-06

Research direction: smaller models and streaming

## slide-22.text-07

Local execution, event-driven updates and persistent freshness need separate implementation.

## slide-22.text-08

Real-time streaming is not implemented in this demo. We show a snapshot-based workflow.

## slide-22.note-01

Discuss integration boundaries: which part is the agent, the worker and the checker?

## slide-22.note-02

Streaming is a proposed future direction, not a confirmed delivery commitment.

<!-- Slide 23: What should you take away? -->

## slide-23.title

What should you take away?

## slide-23.section

Validation and product development

## slide-23.text-01

A good result stays in the folder.

## slide-23.text-02

The agent does the work.

## slide-23.text-03

The project preserves the method.

## slide-23.text-04

The GIS expert judges its meaning.

## slide-23.text-05

OpenMapStack repository ↗

## slide-23.text-06

Homepage and working examples ↗

## slide-23.text-07

Tartu bridge analysis and its provenance ↗

## slide-23.text-08

Technical sources: README · project.yaml · pipeline.py · cli.py · validation/latest-report.json. Presentation basis: the author’s demo experience.

## slide-23.note-01

Three ideas: a file-based contract, the right spatial concept and visible validation.

## slide-23.note-02

The installation command and exact version are in the repository README. Links open in a separate tab.

<!-- Slide 24: Discussion: where would you pilot this? -->

## slide-24.title

Discussion: where would you pilot this?

## slide-24.section

Discussion

## slide-24.text-01

Where would you pilot this?

## slide-24.text-02

One decision

## slide-24.text-03

Which spatial question do you repeatedly answer manually?

## slide-24.text-04

One check

## slide-24.text-05

Which error would make the result unusable?

## slide-24.text-06

One boundary

## slide-24.text-07

Which data and permissions stay in your environment?

## slide-24.text-08

Pilot deliverable: the same question and metric, a visible method, a repeatable run and expert judgement.

## slide-24.note-01

Take one concrete pilot example. If time is short, choose only the validation question.

## slide-24.note-02

Bring the discussion back to the task and quality bar. End at 45 minutes; the slide chooser helps with follow-up questions.
