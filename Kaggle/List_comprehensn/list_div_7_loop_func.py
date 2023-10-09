def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
        at least one number divisible by 7.
        """
    lst1 = []
    lst2 = []
    for num in nums:
        if num % 7 == 0:
            lst1.append(num)
            print('Divisible by 7: ',lst1)
            #return True
        else:
            lst2.append(num)
            print('Not divisible by 7: ',lst2)
            #return False
has_lucky_number([12, 14, 32, 6, 7, 0, 21])
