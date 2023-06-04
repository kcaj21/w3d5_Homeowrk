from models.book import *
from flask import url_for

book_1 = Book("The Bible", "Alex Jack", "Documentary", True)
book_2 = Book("Gary Potter and the Prisoner of Kazakhstan", "Joanne Rowly", "Sci-fi", False)

books = [book_1, book_2]

def add_new_book(book):
    books.append(book)

def delete_book(index):
    books.pop(index)

# chosenbook = books()



# for book in books:
#     book_url = url_for('book_detail', book_id=book.id)
#     # Save the item URL or use it to generate links in your application
#     print(book_url)