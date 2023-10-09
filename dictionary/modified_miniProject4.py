record = {}
while len(record) <= 3:
    name = input('Enter Student Name: ')
    mark = int(input('Enter Student Mark: '))
    record[name] = mark
    print('Student Record Inserted Successfully')
    #option = input('Do you want to insert one more student record [Y | N]: ')

print(record)
print('Name\t\tMarks')
for i in record:
    print('{}\t\t{}'.format(i,record[i]))