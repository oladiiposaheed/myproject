import re

p = input('Enter Pattern to Check: ')
matcher = re.fullmatch(p, 'bbbaaabfrab')
if matcher is not None:
    print('Total Target String Starts with:',matcher.group())
else:
    print('Total Target String NOT Starts with',p)