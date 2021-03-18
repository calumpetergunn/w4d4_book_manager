from db.run_sql import run_sql

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, year, genre, purchased, author_id) VALUES(%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.year, book.genre, book.purchased, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row[author.id])
        book = Book(row['title'], row['year'], row['genre'], row['purchased'], row['id'] ,author)
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository(result['author.id'])
        book = Book(result['title'], result['year'], result['genre'], result['purchased'], result['id'], author)
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title, year, genre, purchased, author_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.year, book.genre, book.purchased, book.author_id]
    run_sql(sql, values)