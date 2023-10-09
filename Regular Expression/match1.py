import re

p = input('Enter Pattern to Check: ')
matcher = re.match(p, 'bbbaaabfrab')
if matcher is not None:
    print('Target String Starts with:',matcher.group())
else:
    print('Target String NOT Starts with:',p)