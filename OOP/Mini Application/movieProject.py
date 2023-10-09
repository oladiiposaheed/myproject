class Movie:
    ''' Movie class developed by Oladiipo for Python Demo Purpose '''
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie Name: {}'.format(self.title))
        print('Hero Name: {}'.format(self.hero))
        print(('Heroine Name: {}'.format(self.heroine)))

list_movies = []
while True:
    title = input('Enter Movie Name: ')
    hero = input('Enter Hero Name: ')
    heroine = input('Enter Heroine Name: ')
    # Create Movie Objects
    m = Movie(title, hero, heroine)
    list_movies.append(m)
    print('Movie Added Successfully')
    option = input('Do you want Add one more movie [Yes !No]: ')
    if option.lower() == 'no':
        break

print('All Movies Information')
print('*' * 40)
for movie in list_movies:
    movie.info()
    print('-' * 40)

