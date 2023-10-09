def outer(msg):
    message = msg
    def inner():
        print(message)
    return inner

result1 = outer('Hello')
result2 = outer('Good Morning')
result1(), '+' , result2()