f = open('name.txt', 'w')
names = ['Chika', 'Fatimah', 'Saheed', 'Mahmud']
for name in names:
    f.write(name+'\n')
f.close()
