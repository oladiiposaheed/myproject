def decor_sum(func):
    def inner(x, y):
        print("#" * 40)
        print('{} + {} = {}'.format(x, y, x + y))
        func(x, y)
        print('#'*40)
    return inner

@decor_sum
def add(a, b):
    print(a + b)

add(23, 5)