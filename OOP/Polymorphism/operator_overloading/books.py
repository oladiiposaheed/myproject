class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return str(self.pages)

b1 = Book(120)
b2 = Book(300)
print(b1)
print(b2)