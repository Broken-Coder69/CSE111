class Book:
    def __init__(self, title, author, genre):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = True
        self.__borrower = None

    # Getter methods
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def is_available(self):
        return self.__available

    def get_borrower(self):
        return self.__borrower

    # Setter methods
    def set_available(self, available):
        self.__available = available

    def set_borrower(self, borrower):
        self.__borrower = borrower

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Genre: {self.__genre}")
        print(f"Availability: {'Available' if self.__available else 'Not Available'}")
        if self.__borrower:
            print(f"Borrower: {self.__borrower.get_name()}")
        print("------------------------")


class LibraryMember:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def borrow_book(self, book):
        if book.is_available():
            book.set_available(False)
            book.set_borrower(self)
            self.__borrowed_books.append(book)
            print(f"{self.__name} has borrowed '{book.get_title()}'.")
        else:
            print(f"'{book.get_title()}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.set_available(True)
            book.set_borrower(None)
            self.__borrowed_books.remove(book)
            print(f"{self.__name} has returned '{book.get_title()}'.")
        else:
            print(f"{self.__name} did not borrow '{book.get_title()}'.")

    def display_borrowed_books(self):
        print(f"{self.__name}'s Borrowed Books:")
        if not self.__borrowed_books:
            print("No books borrowed.")
        for book in self.__borrowed_books:
            print(f" - {book.get_title()}")
        print("------------------------")


class Library:
    def __init__(self):
        self.__available_books = []
        self.__library_members = []

    def add_book(self, book):
        self.__available_books.append(book)

    def add_library_member(self, member):
        self.__library_members.append(member)

    def display_book_list(self):
        print("Available Books:")
        if not self.__available_books:
            print("No books available in the library.")
        for book in self.__available_books:
            print(f" - {book.get_title()} by {book.get_author()}")

    def display_library_members(self):
        print("Library Members:")
        if not self.__library_members:
            print("No library members registered.")
        for member in self.__library_members:
            print(f" - {member.get_name()} (ID: {member.get_member_id()})")

# Create books
book1 = Book("Book One", "Author One", "Fiction")
book2 = Book("Book Two", "Author Two", "Fantasy")
book3 = Book("Book Three", "Author Three", "Mystery")

# Create library members
member1 = LibraryMember("John", "001")
member2 = LibraryMember("Alice", "002")

# Create library
library = Library()

# Add books and library members to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_library_member(member1)
library.add_library_member(member2)

# Display available books and library members
library.display_book_list()
library.display_library_members()

# Borrow and return books
member1.borrow_book(book1)
member1.borrow_book(book2)
member1.display_borrowed_books()

member2.borrow_book(book2)
member2.display_borrowed_books()

member1.return_book(book1)
member1.display_borrowed_books()

# Display book info
book1.display_info()
book2.display_info()
