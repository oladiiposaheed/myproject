fname = input('Enter File Name: ')
while True:
    f = open('E:\\studentdata\\'+fname, 'w')
    data = input('Enter Data to write: ')
    f.write(data+'\n')
    option = input('Do you want to add some more data[Yea|No]: ')
    if option.lower() == 'no':
        break
print('Successfully')
f.close()