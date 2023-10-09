import re

matchers = re.finditer('ab', 'a0ba0a1b2aba8a4b3a4a5abaabaaaba')
count = 0
for match in matchers:
    print(match.start(), '....>', match.group())
    count += 1
print('Total Number of Occurrence:',count)