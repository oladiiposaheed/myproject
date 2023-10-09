import re
match = re.findall('[^\D]', 'a7b9kz@5kmn4')
match1 = re.findall('[0-9]', 'a7b9kz@5kmn4')
match2 = re.findall('\d', 'a7b9kz@5kmn4')
print(match)
print(match1)
print(match2)
print('****************')
lst = []
for i in match2:
    if int(i) % 2:
        #print(i)
        for j in i:
            lst.append(i)
print(lst)
