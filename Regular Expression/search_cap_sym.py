import re
match = re.search('^Learn', 'Learning Python is very easy')
if match is not None:
    print('Target String Start with Patterns')
else:
    print('Target String is NOT Start with Patterns')
