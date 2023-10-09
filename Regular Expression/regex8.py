import re

matchers = re.finditer('a{2,5}', 'abaabaaabaa aaaaaaa')
count = 0
for match in matchers:
    print(match.start(), '....', match.group())
    count += 1
print('Total Number of Occurrence:',count)