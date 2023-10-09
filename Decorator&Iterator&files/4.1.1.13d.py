def outer(par):
    loc = par

    def inner():
        lst = []
        for i in loc:
            #print('Cube of {} = {}'.format(i, i ** 3))
            i = i **3
            lst.append(i)
        print(lst)
    return inner

#var = [12, 3, -4, 5, 0, -9, 3]

var = []
number = int(input('Enter a positive integer: '))
for j in range(number + 1):
    num = float(input('Enter an integer: '))
    var.append(num)
fun = outer(var)
fun()