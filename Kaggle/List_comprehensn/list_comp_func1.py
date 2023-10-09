def count_negatives(nums):
    return len([num for num in nums if num < 0])
print(count_negatives([5, -1, -2, 0, 3, -19]))
