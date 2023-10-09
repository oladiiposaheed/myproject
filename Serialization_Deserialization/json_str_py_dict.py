import json
json_str = '''{
    "Name": "Aisha",
    "Age": 15,
    "Salary": 400000,
    "Married": true,
    "Disability": null 
}'''
emp_dict = json.loads(json_str)
print('Employee Information')
for k, v in emp_dict.items():
    print('{}: {}'.format(k, v))