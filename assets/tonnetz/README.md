This module uses the `libmogra` python package to generate static assets that can be read by .js scripts for the site.

Procedure to update the notes of a raag:
1. Edit in the LibMogra repo (`~/Repos/libmogra/libmogra/shrutidata/make_tonnetz.ipynb`) --> this will edit the `hypothesized_gt_3_5.pkl`
2. [don't remember this]... somehow the `raags.pkl` changes in LibMogra?
3. Run `poetry run python make_nets.py` in this dir --> this will change the files under `images/`, which will be picked up by the site build.

Procedure to update keyboard layout:
1. Make necessary edits (in `mogra` or in `make_layout.py`)
2. Run `poetry run python make_layout.py` in this dir --> this will change `keyboard/key_layout.json`, which will be picked up by the site build.

Procedure to update the interactive tonnetz (`/tonnetz-interactive/`):
1. Make necessary edits (Sa frequency, Devanagari mappings, or genus) in `make_tonnetz_interactive.py`
2. Run `poetry run python make_tonnetz_interactive.py` in this dir --> this will regenerate `interactive/tonnetz_layout.json`, which is fetched at runtime by `tonnetz-interactive/index.html`.
