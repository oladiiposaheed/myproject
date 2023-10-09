import re
target = input('Enter Identifier to Check: ')
patterns = '[a-k][0, 3, 6, 9][a-zA-Z0-9#]*'
match = re.fullmatch(patterns, target)
if match is not None:
    print('Valid Identifier')
else:
    print('Invalid Identifier')