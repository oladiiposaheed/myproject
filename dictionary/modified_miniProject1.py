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
        if option.lower() == 'no':
            option = 'no'
            break
        elif option.lower() == 'yes':
            option = 'yes'
            break
        else:
            option = input('Your input is invalid, please enter correct option [YES |NO]: ')
    if option == 'no':
        break
print(record)
