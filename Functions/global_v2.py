a = 12
def f1():
    a = 444
    print('Local variable:', a)
    #To print global variable a = 12
    #print('Global variable value: ',globals().get('a'))
    print('Global variable value: ', globals()['a'])

f1()