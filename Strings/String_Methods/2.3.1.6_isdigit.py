lsts = ['python', 231, '0012', 'django12', 'des21r']
countainer = []
for lst in range(len(lsts)):
    if lsts[lst].isalpha():
        countainer.append(lst)
print(countainer)