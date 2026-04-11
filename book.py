class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn} - Available: {self.available}"

    def borrow(self):
        if self.available:
            self.available = False
        else:
            print("Book is already borrowed.")

    def return_book(self):
        self.available = True