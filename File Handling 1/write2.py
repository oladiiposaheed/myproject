f = open('xy.txt', 'w')
f.write('Python\n')
f.write('Software\n')
f.write('Django\n')
f.write('PHP\n')
f.write('Golang ')
f.write('JavaScript ')
f.write('PHP ')

print('Data written to the file successfully')
f.close()

cc = '00998783747667'

for num in cc:
    nums = num.split()
    nums[0:7] = 'x'
    print(nums, end='')