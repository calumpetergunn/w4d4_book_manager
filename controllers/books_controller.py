from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    year = request.form['year']
    genre = request.form['genre']
    purchased = request.form['purchased']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, year, genre, purchased, author)
    book_repository.save(book)
    return redirect('/books')

@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', selected_book=book)

@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', selected_book=book, all_authors=authors)

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    year = request.form['year']
    genre = request.form['genre']
    purchased = request.form['purchased']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, year, genre, purchased, author, id)
    book_repository.update(book)
    return redirect('/books')



