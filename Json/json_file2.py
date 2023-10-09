import json

person_dict = {
    "name": "Bob",
    "languages": ["English", "French"],
    "married": True,
    "age": 32
}

with open('person.txt', 'w') as f:
    json.dump(person_dict, f)