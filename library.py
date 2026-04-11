import json
from book import Book
from user import User

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            books = [Book.from_dict(b) for b in data["books"]]
            users = [User.from_dict(u) for u in data["users"]]
            return books, users
    except:
        return [], []

def save_data(books, users):
    data = {
        "books": [b.to_dict() for b in books],
        "users": [u.to_dict() for u in users]
    }
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def add_book(books, book):
    if any(b.isbn == book.isbn for b in books):
        print("Book with this ISBN already exists.")
        return
    books.append(book)
    print("Book added successfully.")

def delete_book(books, isbn):
    for b in books:
        if b.isbn == isbn:
            books.remove(b)
            print("Book deleted.")
            return
    print("Book not found.")

def search_by_title(books, title):
    return [b for b in books if title.lower() in b.title.lower()]

def search_by_author(books, author):
    return [b for b in books if author.lower() in b.author.lower()]

def display_books(book_list):
    if not book_list:
        print("No books found.")
        return
    for b in book_list:
        print(b)

def display_available_books(books):
    display_books([b for b in books if b.available])

def display_borrowed_books(books):
    display_books([b for b in books if not b.available])

def add_user(users, user):
    if any(u.user_id == user.user_id for u in users):
        print("User ID already exists.")
        return
    users.append(user)
    print("User added successfully.")

def display_users(users):
    if not users:
        print("No users found.")
        return
    for u in users:
        print(u)

def borrow_book(books, users, user_id, isbn):
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.isbn == isbn), None)

    if not user:
        print("User not found.")
        return
    if not book:
        print("Book not found.")
        return

    if user.borrow_book(book):
        print("Book borrowed successfully.")
    else:
        print("Book is already borrowed.")

def return_book(books, users, user_id, isbn):
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.isbn == isbn), None)

    if not user or not book:
        print("Invalid user or book.")
        return

    if user.return_book(book):
        print("Book returned successfully.")
    else:
        print("This book was not borrowed by the user.")

def statistics(books, users):
    total_books = len(books)
    total_users = len(users)
    borrowed = sum(len(u.books_borrowed) for u in users)

    print("\n LIBRARY STATISTICS")
    print(f"Total Books: {total_books}")
    print(f"Total Users: {total_users}")
    print(f"Borrowed Books: {borrowed}")