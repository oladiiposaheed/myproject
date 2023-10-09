d = {
    100 : 'Nigeria',
    200 : 'Fatimah',
    300 : 'Phone',
    400 : 'Ahmad'
}
while True:
    key = int(input('Enter key to find the corresponding value: '))
    if key in d:
        print(d[key])
    else:
        print('Specified key is not available')
        break