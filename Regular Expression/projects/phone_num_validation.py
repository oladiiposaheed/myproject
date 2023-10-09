import re

target = input('Enter Your Phone Number: ')
patterns = '(070 | 080 | 081)[3, 6][0-9]{7}'
match = re.fullmatch(patterns, target)
if match is not None:
    print('Valid Mobile Number')
else:
    print('Invalid Mobile Number')