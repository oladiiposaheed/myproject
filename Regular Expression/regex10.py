import re

matchers = re.finditer('\D', 'a0ba0a1b2aa8a4b3a4a5aaaaaaa')
count = 0
for match in matchers:
    print(match.start(), '....>', match.group())
    count += 1
print('Total Number of Occurrence:',count)