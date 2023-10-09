def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

lst = [23, 1, 0, 4, 22, 7, 9, 6, 0]
for i in lst:
    if is_even(i) == True:
        lst.append(i)
print(lst)