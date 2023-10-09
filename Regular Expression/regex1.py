import re

matchers = re.finditer('.', 'a7b@k 9Yz')
count = 0
for match in matchers:
    print(match.start(), '....', match.group())
print('Total Number of Occurrence:',count)