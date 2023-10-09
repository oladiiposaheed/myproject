def wish(name, msg='Bye'):
    print('Hello', name, msg)
wish(name='Python')
print('##################')
#def wish(name='Saheed', msg):
 #   print('Hello', name, msg)
#wish(name='Python')
#print('Python', msg='Good bye')
#print('***************')

def wish(name, msg='Bye'):
    print('Hello',msg, name)
wish(name='Python')
wish(msg='Good Morning', name='Django')
#wish(name='Saheed', 'BYE') WRONG bcos SyntaxError: positional argument follows keyword argument