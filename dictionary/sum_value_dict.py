d = eval(input('Enter dictionary: '))
#print('The Sum:',sum(d.values()))
sum = 0
for v in d.values():
    sum += v
    print('The Sum:', sum)