list1 = [56, 3, 2, 78, 6, 0]
min_val = min(list1)
# Find the index of minimum value
min_index = list1.index(min_val)
print('{} is present at index {}'.format(min_val, min_index))
#Swap the first value and the last value
print(list1)
list1[0], list1[min_index] = list1[min_index], list1[0]
print(list1)
min_index = list1.index(min_val)
print('{} is present at index {} now'.format(min_val, min_index))
