def outer():
    print('Outer Function started')

    def inner():
        print('Inner Function')
    print('End of outer function')
    #return inner()
    return inner

newf = outer()
newf()
newf()
#print(newf)