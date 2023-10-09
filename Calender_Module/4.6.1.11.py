import calendar

c = calendar.Calendar()
for iter in c.itermonthdays(2023, 3):
    print(iter, end=' ')