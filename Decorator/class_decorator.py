class decor(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Wrapper Executed This before {}'.format(self.func.__name__))
        return self.func(*args, **kwargs)

@decor
def display():
    print('Display Result')
display()
print('*'*35)

@decor
def display_info(name, age, rollno):
    print('Display Information Ran With Arguments [{}, {}, {}]'.format(name, age, rollno))
    print('Student Name: {}'.format(name))
    print('Student Age: {}'.format(age))
    print('Student Seat Number: {}'.format(rollno))

display_info('Fatima', 15, 100)
#display()