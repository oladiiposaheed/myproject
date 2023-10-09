import re
matcher = re.sub('[0-9]', '#', 'a7b9kz@5kmn4')
print(matcher)
print('***************')
for match in matcher:
    print(match, end='')