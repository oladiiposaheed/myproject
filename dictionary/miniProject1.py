print('STUDENTS RECORD')
print('---------------')

record = {}
while True:
    name = input('Enter Student Name: ')
    mark = float(input('Enter Student Mark: '))
    record[name] = mark
    print('Student Record Inserted Successfully')
    option = input('Do you want to insert one more student record [YES | NO]: ')
    if option.lower() == 'no':
            break
print(record)
