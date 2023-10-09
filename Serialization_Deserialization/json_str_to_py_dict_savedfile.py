import json
with open('emp.json', 'r') as f:
    emp_dict = json.load(f)

#emp_dict = json.loads(json_str)
print('Employee Information')
for k, v in emp_dict.items():
    print('{}: {}'.format(k, v))