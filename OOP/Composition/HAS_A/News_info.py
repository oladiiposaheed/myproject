class SportsNews:
    def sportsInfo(self):
        print('Sport Information 1')
        print('Sport Information 2')
        print('Sport Information 3')

class MovieNews:
    def movieInfo(self):
        print('Movie Information 1')
        print('Movie Information 2')
        print('Movie Information 3')

class PoliticsNews:
    def politicsInfo(self):
        print('Politics Information 1')
        print('Politics Information 2')
        print('Politics Information 3')

class SaheedNews:
    def __init__(self):
        self.sport = SportsNews()
        self.movie = MovieNews()
        self.politics = PoliticsNews()

    def getsaheedInfo(self):
        print('News Information')
        print('-'*25)
        self.movie.movieInfo()
        print('*'*25)
        self.sport.sportsInfo()
        print('*'*25)
        self.politics.politicsInfo()

s = SaheedNews()
s.getsaheedInfo()