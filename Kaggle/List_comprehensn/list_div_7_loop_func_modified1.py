def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False

print(has_lucky_number([12, 14, 32, 6, 7, 0, 21]))


def has_lucky_number(nums):
    return any([num % 7 for num in nums])

a = [1, 2, 3, 4] > 2
print(a)