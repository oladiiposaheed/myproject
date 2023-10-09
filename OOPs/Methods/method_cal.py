class Cal:
    def Sum(self, nums):
        s = 0
        for num in range(nums + 1):
            s += num
        print('Sum of first {} numbers = {}'.format(nums, s))
    pass

nums = int(input('Enter Positive Integer: '))
obj = Cal()
obj.Sum(nums)
