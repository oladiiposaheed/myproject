def fact(num):
    result = 1
    while num > 1:
        result = result * num
        num = num - 1
    print('The Factorial of {} is {}'.format(i, result))
num = int(input('Enter the Number: '))
if num <= 0:
    print('Enter number greater than 1')
else:
    for i in range(num):
        fact(i)