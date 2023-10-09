from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))
print(d.strftime('%d/%m/%Y'))
print(d.strftime('%d-%m-%Y'))