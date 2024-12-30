import os
import json
import libmogra as lm


raag_db, raag_db_by_notes = lm.raagfinder.parse.read_pickle()
json_path = "tables/"


for raag_name in raag_db.keys():
    raag_info = raag_db[raag_name]
    raag_name = raag_name.replace(" ", "_")
    with open(os.path.join(json_path, f"{raag_name}.json"), "w") as f:
        json.dump(raag_info, f, indent=4)
