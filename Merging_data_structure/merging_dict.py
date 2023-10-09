d1 = {'Fatimah': 100, 'Umar': 99}
d2 = {'Seun': 89, 'Chukwu': 91}
d3 = {'Akin': 56, 'Jumai': 88}
result1 = {**d1, **d2, **d3}
result2 = {*d1, *d3, *d2}
result3 = {*d1.keys(), *d3.keys(), *d2.keys()}
result4 = {*d1.values(), *d2.values(), *d3.values()}
result5 = [*d1.values(), *d2.values(), *d3.values()]
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)