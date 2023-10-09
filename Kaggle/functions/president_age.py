def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)
print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(51, True))

def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

def sign(a):
    if a < 0:
        print('a = ', a)
    elif a > 0:
         print('a = ', a)
    else:
         print('a = ', a)
sign(-1)
sign(1)
sign(0)


def sign(a):
    if a < 0:
        print('a = ', a)
    if a > 0:
         print('a = ', a)
    if a < 0:
         print('a = ', a)
sign(-1)
sign(1)
sign(0)