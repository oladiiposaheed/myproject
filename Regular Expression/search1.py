import re
match = re.search('bbb', 'abbabbbabb')
#match = re.search('bbb', 'abbabbabb')
if match is not None:
    print('Match is Available at',match.start(), '---->',match.end())
else:
    print('Match is Not Available')