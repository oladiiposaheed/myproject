f = open('E:\\pq.txt', 'w')
lst = ['Toyota\n', 'Venza\n', 'Keke\n']
lst1 = {'Python\n', 'Django\n', 'JS\n'}
d = {'A':2, 'B':43, 'C':21}
f.writelines(lst)
f.writelines(lst1)
f.writelines(d)
print('Data written to the file successfully')
f.close()