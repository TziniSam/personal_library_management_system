class User:
    def __init__(self, name, user_id, books_borrowed=None):
        self.name = name
        self.user_id = user_id
        self.books_borrowed = books_borrowed or []

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id}) - Borrowed Books: {len(self.books_borrowed)}"

    def borrow_book(self, book):
        if book.borrow():
            self.books_borrowed.append(book.isbn)
            return True
        return False

    def return_book(self, book):
        if book.isbn in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book.isbn)
            return True
        return False
        
    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return User(**data)