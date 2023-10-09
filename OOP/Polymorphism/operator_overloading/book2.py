class Book:
    def __int__(self, pages):
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        newBook = Book(total_pages)
        return newBook

    def __str__(self):
        return str(self.pages)

b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
print(b1 + b2)
#print(b1 + b2 + b3)