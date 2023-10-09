class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        #total_pages = self.pages + other.pages + other.pages
        total_pages = self.pages + other.pages
        return total_pages

    def __sub__(self, other):
        reduced_pages = self.pages - other.pages
        return reduced_pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __mod__(self, other):
        return self.pages % other.pages

    def __floordiv__(self, other):
        return self.pages // other.pages

    def __ipow__(self, other):
        return self.pages ** other.pages

b1 = Book(120)
b2 = Book(200)
b3 = Book(350)
print(b1 + b2)
print(b1 + b3)
print(b3 + b2)
print('***********')
print(b1 - b2)
print('***********')
print(b1 * b2)
print('***********')
print(b1 % b2)
print('***********')
print(b2 // b1)
print('***********')
#print(pow(b1, b2))