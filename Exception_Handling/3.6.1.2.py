def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print('Division Failed')
        n = None
    else:
        print('Everything Went Fine')
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print()
print(reciprocal(0))