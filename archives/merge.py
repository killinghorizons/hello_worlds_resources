import json

with open("../json/backup.json", "r", encoding="utf-8") as f:
    my_hellos = json.load(f)

with open("../json/github_hello_world.json", "r", encoding="utf-8") as f:
    github_hellos = json.load(f)

my_languages = [
    {"name": hello["language"], "code": hello["code"]} for hello in my_hellos
]
github_languages = [
    {"name": hello["name"], "code": hello["content"]} for hello in github_hellos
]


names_in_my_languages = {item["name"] for item in my_languages}
names_in_github_languages = {item["name"] for item in github_languages}

unique_items = {item["name"]: item for item in my_languages + github_languages}

merged_list = list(unique_items.values())

with open("filtered_merge_sample_V3.json", "w") as f:
    f.write(json.dumps(merged_list))
