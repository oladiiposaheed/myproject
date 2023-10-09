import time
def countdown(n):
    print('Count Down')
    maxNum = 10
    while maxNum > 0:
        yield maxNum
        maxNum -= 1
v = countdown(10)
for i in v:
    print(i)
    time.sleep(1)