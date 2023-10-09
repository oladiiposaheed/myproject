import calendar

c = calendar.Calendar()
for iter in c.itermonthdays2(2023, 3):
    print(iter, end=' ')
    #print()

c = calendar.Calendar()
for iter in c.itermonthdays3(2023, 3):
    print(iter, end=' ')

c = calendar.Calendar()
for iter in c.itermonthdays4(2023, 3):
    print(iter, end=' ')