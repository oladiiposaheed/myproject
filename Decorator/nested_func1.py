def outer():
    print('Outer Function started')

    def inner():
        print('Inner Function')
    inner()
    inner()

    print('End of outer function')

outer()