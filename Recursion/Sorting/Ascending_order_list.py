list1 = [56, 3, 2, 78, 6, 0, 89, -21]

for i in range(len(list1)):
    min_val = min(list1[i:])
    # print(min_val)
    index_val = list1.index(min_val)
    # print(index_val)
    list1[i], list1[index_val] = list1[index_val], list1[i]
    # print(list1)
print(list1)