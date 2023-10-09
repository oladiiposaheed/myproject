def even_odd(n):
    if n % 2:
        return n,'is an odd number'
    else:
        return n,'is an even number'
a = int(input('Enter the number: '))
op = even_odd(a)
print(op)