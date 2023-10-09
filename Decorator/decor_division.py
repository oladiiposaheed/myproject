def smart_division(func):
    def inner(a, b):
        if b == 0:
            print('Hello, You cannot divide by zero')
        else:
            func(a, b)
    return inner

@smart_division
def division(a, b):
    print(a/b)

#division(10, 2)
division(10, 0)