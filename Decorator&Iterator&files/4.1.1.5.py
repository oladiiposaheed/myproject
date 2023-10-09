import time
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power ** 2
        power *= 2

for v in powers_of_2(8):
    print(v, end=' ')
    time.sleep(3)