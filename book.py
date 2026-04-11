class Book:
    def __init__(self, title, author, year, isbn, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({self.year}) | ISBN: {self.isbn} | {status}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Book(**data)