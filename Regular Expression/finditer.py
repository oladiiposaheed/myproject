import re
matcher = re.finditer('[0-9]', 'a7b9kz@5kmn4')
for match in matcher:
    print('{}....{}'.format(match.start(), match.group()))