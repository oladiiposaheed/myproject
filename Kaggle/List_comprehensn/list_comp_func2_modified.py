def count_negatives(nums):
    return sum([num < 0 for num in nums])
print(count_negatives([5, -1, -2, 0, -21, -0,  3, -19]))
