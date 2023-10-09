class Book:
    def __init__(self, author, pages):
        self.author = author
        self.pages = pages

    def __add__(self, other):
        desc= 'This book is written by {} and {}'.format(self.author, other.author)
        total_pages = self.pages + other.pages
        return desc, total_pages


b1 = Book('Saheed', 2000)
b2 = Book('Oladiipo', 3500)
result = b1 + b2
print(result)

for i in result:
    if i == 0:
        print(i)
    else:
        print('Pages:',i)