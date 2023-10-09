import time


def power_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for i in range(20):
    if i in power_2(5):
        print(i, end=' ')
        time.sleep(2)