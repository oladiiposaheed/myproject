import copy
l1 = [1, 2, [3,5], 4]
l2 = copy.deepcopy(l1)
print("The original elements before deep copying")
for i in range(0, len(l1)):
    print(l1[i], end=' ')
print('\r')
# adding and element to new list
l2[2][0] = 230
# Change is reflected in l2
print("The new list of elements after deep copying ")
for i in range(0, len(l2)):
    print(l2[i], end=' ')
# Change is NOT reflected in original list
# as it is a deep copy
print("The original elements after deep copying")
for i in range(0,len( l1)):
    print (l1[i],end=" ")