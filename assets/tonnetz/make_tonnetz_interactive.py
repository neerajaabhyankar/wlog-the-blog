"""
Generates interactive/tonnetz_layout.json for tonnetz-interactive/index.html.
Run with: poetry run python make_tonnetz_interactive.py
"""

import json
import os
from libmogra.tonnetz import Tonnetz, EFGenus, GT_GENUS
from libmogra.datatypes import normalize_frequency, ratio_to_swarval

DVNGRI = {
    "S": "सा", "r": "रे्", "R": "रे", "g": "ग्", "G": "ग",
    "m": "म",  "M": "म्", "P": "प",  "d": "ध्", "D": "ध",
    "n": "नी्", "N": "नी",
}

Sa = 220.0

tn = Tonnetz(EFGenus.from_list(GT_GENUS))

def theme_colors(theme):
    tn.set_color_scheme(theme)
    return {
        "chord_major": tn.color_scheme.chord_major,
        "chord_minor": tn.color_scheme.chord_minor,
        "node_blank":  tn.color_scheme.node_blank,
        "nodes":       {tuple(c): tn.get_node_color(tuple(c)) for c in tn.node_coordinates},
    }

twilight = theme_colors("twilight")
daylight = theme_colors("daylight")

meta = {
    "sa_hz":       Sa,
    "chord_major": {"twilight": twilight["chord_major"], "daylight": daylight["chord_major"]},
    "chord_minor": {"twilight": twilight["chord_minor"], "daylight": daylight["chord_minor"]},
    "node_blank":  {"twilight": twilight["node_blank"],  "daylight": daylight["node_blank"]},
}

nodes = []
for coord, name, ratio in zip(tn.node_coordinates, tn.node_names, tn.node_ratios):
    nodes.append({
        "x":      int(coord[0]),
        "y":      int(coord[1]),
        "name":   str(name),
        "dvngri": DVNGRI[str(name)],
        "ratio":  str(ratio),
        "freq":   round(Sa * float(ratio), 4),
        "color":  {
            "twilight": twilight["nodes"][tuple(coord)],
            "daylight": daylight["nodes"][tuple(coord)],
        },
    })

out_path = os.path.join("interactive", "tonnetz_layout.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"meta": meta, "nodes": nodes}, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(nodes)} nodes + meta to {out_path}")
