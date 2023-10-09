import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2023, 3):
    print(data)

from datetime import date



a = date(1992, 1, 16)
b = date(1991, 2, 5)
print(a - b)

from os import strerror
c = bytearray(3)
print(c)

from datetime import datetime
p = datetime(2019, 11, 27, 11, 27, 22)
print(p.strftime('%y/%B/%d %H:%M:%S'))

def a(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
        
for x in a(2):
    print(x, end='')