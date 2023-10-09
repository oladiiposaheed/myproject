import re
match = re.search('EASY$', 'Learning Python is very easy', re.IGNORECASE)
if match is not None:
    print('Target String Start with Patterns')
else:
    print('Target String is NOT Start with Patterns')
