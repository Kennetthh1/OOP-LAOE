class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Super Book", "Masakazu Higuchi")
book2 = Book("Jujutsu Kaisen", "Gege Akutami")
print(book1.title, book1.author)
print(book2.title, book2.author)

del book1.author

#print(book1.title, book1.author)
print(book2.title, book2.author)
