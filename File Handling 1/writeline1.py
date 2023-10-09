f = open('a_bc.txt', 'w')
lst = ['Rice\n', 'Pawpaw\n', 'Guava\n', 'Pepper']
lst1 = {'Python\n', 'Django\n', 'JS\n'}
d = {'A':2, 'B':43, 'C':21}
f.writelines(lst)
f.writelines(lst1)
f.writelines(d)
print('Data written to the file successfully')
f.close()