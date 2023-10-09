import re
matcher = re.subn('[0-9]', '#', 'a7b9kz@5km66n4')
print(matcher)
print('REsult String:',matcher[0])
print('REsult String:',matcher[-1])