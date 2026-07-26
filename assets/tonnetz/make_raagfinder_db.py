"""
Dump the libmogra raag database and its by-swar-set search index to a static
JSON asset, so that /raagfinder-by-notes/ can do `mogra search <swars>` in the
browser without re-implementing any of the lookup.

Run:
    poetry run python make_raagfinder_db.py

Writes:
    raagfinder/raagdb.json
"""

import json
import os

import libmogra as lm
from libmogra.raagfinder.parse import RAAG_DB, RAAG_DB_BY_SWAR


OUT_PATH = os.path.join(os.path.dirname(__file__), "raagfinder", "raagdb.json")


def format_value(key, value):
    """The same rendering libmogra.raagfinder.parse.print_table uses per row."""
    if key == "mukhyanga":
        return "\n".join("-- " + ", ".join(map(str, sub)) for sub in value)[:-4]
    if isinstance(value, list):
        return ", ".join(map(str, value))
    return str(value)


def main():
    # attribute rows, pre-rendered exactly as the CLI's print_table would show them
    raags = {
        raag_name: [[key, format_value(key, value)] for key, value in entry.items()]
        for raag_name, entry in RAAG_DB.items()
    }

    # the search index itself: "S,R,G,M,P,D,n" -> [raag names]
    by_swar = {",".join(swar_set): names for swar_set, names in RAAG_DB_BY_SWAR.items()}

    # so the page can normalize typed input the way libmogra.raagfinder.main.search does
    swar_order = {s.name: s.value for s in lm.datatypes.Swar}

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as fp:
        json.dump(
            {"swar_order": swar_order, "by_swar": by_swar, "raags": raags},
            fp,
            indent=1,
        )

    print(f"wrote {len(raags)} raags in {len(by_swar)} swar sets to {OUT_PATH}")


if __name__ == "__main__":
    main()
