def upper_case(func):
    def inner1():
        result1 = func()
        return result1.upper()
    return inner1

def split_string(func):
    def inner2():
        return func().split()
    return inner2

@split_string
@upper_case
def ordinary():
    return 'python is a very good programming language for data sceince'
print(ordinary())