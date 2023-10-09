import re
s = re.split('-','20-2-2023')
print(s)
for i in s:
    if i == '2':
        continue
    print(i)