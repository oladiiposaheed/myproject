def binarySearch(arr)


arr = [1, 2, 3, 4, 5, 6]
target = 6

result = binarySearch(arr, target) # return the index  of the target i.e index = 5, 6 is at index 5

if result != -1:
    print('Element is present at index %d', result)
else:
    print('element is not present in the array')