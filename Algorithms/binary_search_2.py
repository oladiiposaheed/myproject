def BinartSearch(lst, key):
    low = 0
    high = len(lst) - 1
    Found = False
    while low <= high and not Found:
        mid = (low + high) // 2
        if key == lst[mid]:
            Found = True
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if Found ==True:
        print('The key found in the array')
    else:
        print('The Key not found in the array')

lst = [27, 1, 4, 2, 5]
sorted_list = lst.sort()
key = int(input('Please the key to search: '))
BinartSearch(lst, key)