import json

def read_and_update_json(file_path, new_superheroes):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        data['members'].extend(new_superheroes)

    return data

json_file_path = 'superhero.json'
new_superheroes = [
    {
        "name": "New Hero 1",
        "age": 30,
        "secretIdentity": "Secret 1",
        "powers": ["Power 1", "Power 2"]
    },
    {
        "name": "New Hero 2",
        "age": 25,
        "secretIdentity": "Secret 2",
        "powers": ["Power 3", "Power 4"]
    }
]

updated_data = read_and_update_json(json_file_path, new_superheroes)


sorted_members = sorted(updated_data['members'], key=lambda x: x['age'])
sorted_data = {
    "squadName": updated_data["squadName"],
    "homeTown": updated_data["homeTown"],
    "formed": updated_data["formed"],
    "secretBase": updated_data["secretBase"],
    "active": updated_data["active"],
    "members": sorted_members
}

with open('superhero_new.json', 'w') as jsonfile:
    json.dump(sorted_data, jsonfile, indent=2)