# OpenMapBench: one recorded trial

This evidence supports slide 20, **not a configuration ranking**.
Run `20261012T213809Z-ee-vec-002-8b792b6e` recorded `passed` on 12 October 2026.
The agent metadata names `pi`; model and full skill/tool configuration are not
recorded there. No model identity or comparative claim is inferred.

The task matches Tartu pharmacies from Overture and OSM one-to-one within 60 m
in EPSG:3301. The expected JSON has five fields: Overture count, OSM count,
matched pairs, distinct count after merging and unmatched Overture IDs.
The recorded evaluator found zero mismatches: 21 Overture entries, 42 OSM
entries, 15 pairs, 48 distinct pharmacies and six unmatched Overture IDs.
This is the evaluator's verdict against its reference, not independent proof
of completeness of either source dataset.

Included here:

- `task-snapshot.yaml`: the staged task used by the run.
- `output.json`: the unchanged candidate artifact.
- `reference.json`: the unchanged retained reference.
- `verdict.json`: a scoped manifest extract with evaluation details, source
  manifest hash, input hashes, environment and retained log hashes.

The candidate, reference and all three input hashes were checked against the
retained files when this slide was authored. The current source task no longer
matches the recorded original task hash, so its later wording was not used as
the historical task. The staged snapshot has its own recorded hash here.

Full manifest and logs remain in the local OpenMapBench run directory:
`runs/benchmark/20261012T212928Z-9f13cbbc/task-runs/20261012T213809Z-ee-vec-002-8b792b6e/`.
Raw agent logs and source datasets are not copied into this presentation repo.
The hash inventory identifies those retained files; it is not their contents.
Task inputs cite Overture Maps and © OpenStreetMap contributors; see the
OpenMapBench task's source attribution for the datasets. No input dataset is
redistributed here.

A defensible configuration comparison fixes the versioned task, input data,
reference, evaluator, runtime, permissions and time/cost limits. It records the
agent/model/skill/tool configuration explicitly, repeats trials and reports
pass rates and variation in time and cost. This one trial supplies no such ranking.
