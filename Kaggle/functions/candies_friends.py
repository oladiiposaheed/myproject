def to_smash(total_candies, n):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.


    1
    """
    alice_candies = 20
    bob_candies = 39
    carol_candies = 89
    total_candies = (alice_candies + bob_candies + carol_candies)
    return total_candies % n


print(to_smash(98, n=3))
# Check your answer
# q3.check()

def f(x):
    y = abs(x)
    return y
print(f(-5))