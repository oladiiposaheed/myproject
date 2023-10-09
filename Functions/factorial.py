def facorial(num):
    result = 1
    while num > 1:
        result = result * num
        num = num - 1
    return result

#f = facorial(5)
#print(f)
n = int(input('Enter a Number to find its factorial: '))
if n <= 0:
    print('Please enter an integer greater than 1')
else:
    for i in range(0, n):
        a = facorial(i)
        print('The Factorial of {} is {}'.format(i, a))