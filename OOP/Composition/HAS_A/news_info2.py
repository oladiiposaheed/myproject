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
    def __init__(self, sport, movie, c):
        self.sport = sport
        self.movie = movie
        self.politics = politics

    def getsaheedInfo(self):
        print('News Information')
        print('-'*21)
        self.movie.movieInfo()
        print('*'*21)
        self.sport.sportsInfo()
        print('*'*21)
        self.politics.politicsInfo()

sport = SportsNews()
movie = MovieNews()
politics = PoliticsNews()

s = SaheedNews(sport, movie, politics)
s.getsaheedInfo()