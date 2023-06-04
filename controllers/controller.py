from flask import render_template, request, redirect
from app import app
from models.book import *
from models.book_list import books, add_new_book, delete_book

# @app.route('/')
# def index():
#     return render_template("index.html", title = "library")

@app.route('/books')
def index():
    return render_template("index.html", title = "Home", books=books)

# @app.route("/books")
# def show_books():
#     return render_template("index.html", book_list = books)

@app.route("/books", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = True if "checked_out" in request.form else False
    new_book = Book(title, author, genre, checked_out)
    add_new_book(new_book)
    # return render_template("index.html", book_list=books)
    return redirect("/books")

@app.route("/books/del/<index>", methods=["POST"])
def delete_by_index(index):
    delete_book(int(index))
    return redirect("/books")

@app.route("/books/<index>")
def single_book(index):
    chosen_book = books[int(index)]
    return render_template("book_detail.html", book=chosen_book)


# @app.route('/book/<int:book_id>')
# def item_page(item_id):
#     # Logic to retrieve item details based on item_id
#     chosenbook = get_item_by_id(item_id)
#     # Render a template for the item page and pass the item data
#     return render_template('item.html', chosenbook=chosenbook)
