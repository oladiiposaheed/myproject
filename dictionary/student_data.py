n = int(input('Enter the Number of Student: '))
d = {}
while len(d) <= n:
    name = input('Enter the Student Name: ')
    marks = float(input('Enter the Student Mark: '))
    d[name] = marks
#print(d)
print('All Students Data Inserted')
while True:
    name = input('Please Enter Student Name to get Marks: ')
    if name in d:
        print('The Marks of {}:{}'.format(name, d[name]))
    else:
        print('Student Name Not Found')

    option = input('Do you want to find another student marks [Yes | No]')
    while option not in ['yes', 'no']:
        option = input('Invalid option, Please enter Valid option [Yes | No]:')
    if option.lower() == 'no':
        break
print('Thanks For Using Our Application')
#print(d)