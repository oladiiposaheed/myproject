squares = []
squared_even = []
num = int(input('Enter either positive or negative integer: '))
for i in range(1, num):
    squares.append(i**2)
    print(squares)
    print('_______________')
    for j in squares:
        if j % 2 == 0:
            squared_even.append(j)
    print(squared_even)