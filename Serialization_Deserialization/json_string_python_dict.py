import json
json_str = '''{
    "name": "Aisha",
    "Age": 15,
    "Salary": 400000,
    "Married": true,
    "disability": null 
}'''
#print(json_str)
e_dict = json.loads(json_str)
#print(type(e))
print(e_dict)
print('Employee Name:',e_dict['name'])
print('Employee Age:',e_dict['Age'])
print('Employee Salary:',e_dict['Salary'])
print('Employee Sex:',e_dict['Married'])
print('Employee Disability:',e_dict['disability'])
