from book import Book
from user import User
import library as lib

books, users = lib.load_data()

def get_int_input(message):
    try:
        return int(input(message))
    except ValueError:
        print("Please enter a valid number.")
        return None

while True:
    print("\n=== PERSONAL LIBRARY ===")
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Search for a book")
    print("4. Show all books")
    print("5. Display available books")
    print("6. Display borrowed books")
    print("7. Add a user")
    print("8. Show all users")
    print("9. Borrow a book")
    print("10. Return a book")
    print("11. Statistics")
    print("12. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        year = get_int_input("Year: ")
        isbn = input("ISBN: ")

        if year is not None:
            lib.add_book(books, Book(title, author, year, isbn))
            lib.save_data(books, users)

    elif choice == "2":
        isbn = input("ISBN: ")
        lib.delete_book(books, isbn)
        lib.save_data(books, users)

    elif choice == "3":
        keyword = input("Enter title or author: ")
        results = lib.search_by_title(books, keyword) + lib.search_by_author(books, keyword)
        lib.display_books(results)

    elif choice == "4":
        lib.display_books(books)

    elif choice == "5":
        lib.display_available_books(books)

    elif choice == "6":
        lib.display_borrowed_books(books)

    elif choice == "7":
        name = input("Name: ")
        user_id = get_int_input("User ID: ")
        if user_id is not None:
            lib.add_user(users, User(name, user_id))
            lib.save_data(books, users)

    elif choice == "8":
        lib.display_users(users)

    elif choice == "9":
        user_id = get_int_input("User ID: ")
        isbn = input("ISBN: ")
        if user_id is not None:
            lib.borrow_book(books, users, user_id, isbn)
            lib.save_data(books, users)

    elif choice == "10":
        user_id = get_int_input("User ID: ")
        isbn = input("ISBN: ")
        if user_id is not None:
            lib.return_book(books, users, user_id, isbn)
            lib.save_data(books, users)

    elif choice == "11":
        lib.statistics(books, users)

    elif choice == "12":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")