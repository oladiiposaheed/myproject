def mul_by_five(x):
    return  5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

def cube_call(fn, arg):
    return fn(fn(fn(arg)))

print(
    call(mul_by_five, 1),   # 5 * 1 = 5
    squared_call(mul_by_five, 1), # fn(fn(arg)) = 5(5) = 25
    cube_call(mul_by_five, 1),  #5*5*5
    sep='\n'
)