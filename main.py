import json

with open("data/rosettacode/rosetta_code.json", "r", encoding="utf-8") as f:
    data = json.load(f)


names = [x["name"] for x in data]

with open("data/rosettacode/rosettacode_names.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(names))
