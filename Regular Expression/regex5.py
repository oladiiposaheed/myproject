import re

matchers = re.finditer('a*', 'abaabaaab')
count = 0
for match in matchers:
    print(match.start(), '....', match.group())
    count += 1
print('Total Number of Occurrence:',count)