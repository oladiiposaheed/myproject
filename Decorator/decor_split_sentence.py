from functools import wraps
def decor(func):

    @wraps(func)
    def inner(lst):
        return [func(value) for value in lst]
    return inner

@decor
def camelCase(s):
    return ''.join([word.capitalize() for word in s.split(',')])
    #return [word for word in names.split()]

names = ['Python', 'django', 'php', 'java']
print(camelCase(names))
#print(camelCase('lower_string'))
#print(camelCase('python_is_simple'))
print(camelCase.__doc__)