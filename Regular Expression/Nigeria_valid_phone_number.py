import re
num = input('Enter Mobile Number to Validate: ')
pattern = '[2][3][4][-][0-9]{10}'
match = re.fullmatch(pattern, num)
if match is not None:
    print('{} is a Valid Nigeria Mobile Number'.format(num))
else:
    print('{} is Not a Valid Nigeria Mobile Number'.format(num))