def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative += 1
    print(n_negative)
count_negatives([5, -1, -2, 0, 3, -0, -12])