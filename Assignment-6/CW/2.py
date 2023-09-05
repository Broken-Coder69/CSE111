class Book:
    def __init__(self, title, author, genre):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = True
        self.__borrower = None

    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author
    def get_author(self):
        return self.__author


    def set_genre(self, genre):
        self.__genre = genre
    def get_genre(self):
        return self.__genre

    def set_availability(self, available):
        self.__available = available
    def get_availability(self):
        return self.__available

    def set_borrower(self, borrower):
        self.__borrower = borrower
    def get_borrower(self):
        return self.__borrower


    def details(self):
        print("Details:")
        print(f"Name of the Book: {self.__title}")
        print(f"Authors Name: {self.__author}")
        print(f"Genre: {self.__genre}")
        print(f"Availability: {'Available' if self.__available else 'Not Available'}")
        if self.__borrower:
            print(f"Borrower: {self.__borrower.get_name()}")






class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.borrowed_books = []

    def set_member_id(self, member_id):
        self.__member_id = member_id
    def get_member_id(self):
        return self.__member_id

    def set_name(self, name):
        self.__name_id = name
    def get_name(self):
        return self.__name


    def borrow_book(self, book):
        if book.get_availability():
            book.set_availability(False)
            book.set_borrower(self)
            self.borrowed_books.append(book)
            print(f"{self.__name} has borrowed {book.get_title()}")
        else:
            print("Sorry this book is already borrowed by someone else")



    def return_book(self, book):
        if book in self.borrowed_books:
            book.set_availability(True)
            book.set_borrower(None)
            self.borrowed_books.remove(book)
            print(f"{self.__name} has returned {book.get_title()}")
        else:
            print(f"{self.__name} never borrowed the book to start with")


    def display_borrowed_books(self):
        print(f"Here's the list of books that {self.__name} has borrowed:")
        if not self.borrowed_books:
            print("None")

        for i in self.borrowed_books:
            print(f" - {i.get_title()}")




class Library:
    def __init__(self):
        self.books_available = []
        self.library_members = []


    def add_book(self, book):
        self.books_available.append(book)

    def add_library_member(self, member):
        self.library_members.append(member)


    def display_book_list(self):
        print("Available Books:")
        if not self.books_available:
            print("No books to show")
        for i in self.books_available:
            print(f"- {i.get_title()} by {i.get_author()}")




    def display_library_members(self):
        print("Our Belover Library Members:")
        if not self.library_members:
            print("Sorry! No member found")

        for i in self.library_members:
            print(f"- Name: {i.get_name()}    ID: {i.get_member_id()}")





# book1 = Book("Harry Potter", "J.K", "fantasy")
# book2 = Book("Nothing Lasts Forever", "Sidney Sheldon", "Fiction")
# book1.details()

# print("######1######")

# member1 = LibraryMember("001", "John" )
# member1.borrow_book(book1)
# print("#############")
# book1.details()
# member1.borrow_book(book2)

# member2 = LibraryMember("002", "Snow" )

# member2.borrow_book(book1)

# print("######2######")

# member1.return_book(book1)
# # member2.return_book(book1)

# print("######3######")

# member1.display_borrowed_books()


# print("######")
# print("######")
# print("######")
# library = Library()
# library.display_book_list()
# library.add_book(book1)
# library.add_book(book2)
# library.display_book_list()
# library.display_library_members()
# library.add_library_member(member1)
# library.add_library_member(member2)
# library.display_library_members()


book1 = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fiction")
book2 = Book("Nothing Lasts Forever", "Sidney Sheldon", "Fiction")
book3 = Book("Calculus", "Gilbert Strang", "Education")

# Create LibraryMember objects
member1 = LibraryMember("LM01", "Tom Cruise")
member2 = LibraryMember("LM02", "Brad Pitt")

# Create Library object
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add library members
library.add_library_member(member1)
library.add_library_member(member2)

# Library members borrow books
member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book3)

# Display all books in the library
library.display_book_list()
print("1======================================")

# Display library members and their borrowed books
member1.display_borrowed_books()
print("2======================================")
member2.display_borrowed_books()
print("3======================================")
# Returning book2 by member 1
member1.return_book(book2)
print("4======================================")
# Display library member1's borrowed books
member1.display_borrowed_books()
# Display all books in the library
library.display_book_list()