import libmogra as lm

raag_db, _ = lm.raagfinder.parse.read_pickle()

for raag_name in raag_db.keys():
    raag_name = raag_name.replace(" ", "_")
    lm.raagfinder.info(raag_name, show_tonnetz=f"images/raag_{raag_name}.png")
    