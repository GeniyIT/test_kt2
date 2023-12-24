import json

import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_FILE_PATH = get_path(filename="SuperHero.json")


with open(JSON_FILE_PATH, "r") as f:
    supers = json.loads(f.read())

print(supers)

members = []

for i in supers['members']:
    members.append(i)

members_sorted = sorted(members, key=lambda j: -j['age'])

print(members_sorted)