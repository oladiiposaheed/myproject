def round_to_two_places(num):
    """Return the given number rounded to two decimal places.
    """
    return round(num, 2)

def large_num(n):
    return round(n, -3)
print(round_to_two_places(5.3412))
print(large_num(56439.32156))
print(large_num(67887.32156))
print(large_num(0.32156))