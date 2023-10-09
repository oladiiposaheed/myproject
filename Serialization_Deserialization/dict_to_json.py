import json
emp = {
    'First Name': 'Ola',
    'Last Name': 'Fatimah',
    'Age': 15,
    'Married': False,
    'Disability': None
}
json_str = json.dumps(emp, indent=4, sort_keys=True)
#print(type(json_str))
print(json_str)

with open('emp.json', 'w') as f:
    json.dump(emp,f, indent=5)