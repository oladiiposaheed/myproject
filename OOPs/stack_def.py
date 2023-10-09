stack = []

def push(val):
    stack.append(val)
    print(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(12)
push(0)
push(-1)
push('Python')
print('*******')
print(pop())
print(pop())