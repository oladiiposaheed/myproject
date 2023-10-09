f = open('nam2.txt', 'w')
d = {
    'Python\n':3.11,
    'PHP\n': 3.0,
    'Java\n': 4.1,
    'JavaScript\n': 2.9
}
f.writelines(d)
f.close()