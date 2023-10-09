lst = ['python', 'django', 'php', 'java', 'javasCrIpt', 'Dsa']
for i in range(len(lst)):
    print(lst[i])
print('**********')
for j in lst:
    if j.endswith('p') or j.startswith('j'):
        print('Latest Programming: {}'.format(j.capitalize()))