print('STUDENTS RECORD')
print('---------------')

record = {}
while True:
    name = input('Enter Student Name: ')
    mark = int(input('Enter Student Mark: '))
    record[name] = mark
    print('Student Record Inserted Successfully')
    option = input('Do you want to insert one more student record [YES | NO]: ')
    while True:
        if option.lower() in ['yes', 'no']:
            break
        else:
            option = input('Your input is invalid, please enter correct option [YES |NO]: ')
    if option.lower() == 'no':
        break
print(record)
