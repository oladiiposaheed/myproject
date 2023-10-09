list1 = [56, 3, 2, 78, 6, 0, 89, -21]

for i in range(len(list1)):
    max_val = max(list1[i:])
    # print(min_val)
    index_val = list1.index(max_val)
    # print(index_val)
    list1[i], list1[index_val] = list1[index_val], list1[i]
    # print(list1)
print(list1)