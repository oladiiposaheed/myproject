record = {}
while True:
    name = input('Enter Student Name: ')
    mark = int(input('Enter Student Mark: '))
    record[name] = mark
    print('Student Record Inserted Successfully')
    option = input('Do you want to insert one more student record [Y | N]: ')

    while option.lower() not in ['y', 'n']:
        option = input('Your input is invalid, please enter correct option [Y |N]: ')
    if option.lower() == 'n':
        break
print(record)
print('Name\t\tMarks')
for i in record:
    print('{}\t\t{}'.format(i,record[i]))