def replace_spaces(replacement='*'):

    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement

stars = replace_spaces()
print(stars('And Now for Something Completely Different'))

def f(x): return 3*x
print(f(4))

f = lambda x: 3*x
print(f)