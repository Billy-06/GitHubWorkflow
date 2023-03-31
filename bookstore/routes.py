from bookstore import app
from flask import Blueprint, render_template, request, redirect, url_for
from bookstore.models import Book, Member

# Create a dummy dictionary to act like the database
# This will be replaced with a real database later
# Call this variable db
db = {
    'books': [
        {
            'id': 1,
            'title': 'A Tale of Two Cities',
            'author': 'Charles Dickens',
            'pages': 544,
            'status': 'available'
        },
        {
            'id': 2,
            'title': 'The Picture of Dorian Gray',
            'author': 'Oscar Wilde',
            'pages': 320,
            'status': 'unavailable'
        },
        {
            'id': 3,
            'title': 'The Strange Case of Dr Jekyll and Mr Hyde',
            'author': 'Robert Louis Stevenson',
            'pages': 384,
            'status': 'available'
        },
        {
            'id': 4,
            'title': 'The Adventures of Sherlock Holmes',
            'author': 'Arthur Conan Doyle',
            'pages': 416,
            'status': 'available'
        },
        {
            'id': 5,
            'title': 'The Hound of the Baskervilles',
            'author': 'Arthur Conan Doyle',
            'pages': 348,
            'status': 'unavailable'
        },
        {
            'id': 6,
            'title': 'Othello',
            'author': 'William Shakespeare',
            'pages': 160,
            'status': 'available'
        },
        {
            'id': 7,
            'title': 'The Importance of Being Earnest',
            'author': 'Oscar Wilde',
            'pages': 496,
            'status': 'available'
        },
        {
            'id': 8,
            'title': 'The War of the Worlds',
            'author': 'H. G. Wells',
            'pages': 256,
            'status': 'available'
        },
        {
            'id': 9,
            'title': 'The Time Machine',
            'author': 'H. G. Wells',
            'pages': 288,
            'status': 'available'
        },
        {
            'id': 10,
            'title': 'Paradise Lost',
            'author': 'John Milton',
            'pages': 448,
            'status': 'available'
        }
    ]
}

# Create a shell context for the Flask shell
# This will allow us to use the db object in the shell


@app.shell_context_processor
def make_shell_context():
    list_of_books = []
    for item in db['books']:
        item = Book(item['title'], item['author'],
                    item['pages'], item['status'])
        list_of_books.append(item)

    db['books'] = list_of_books

    return {'db': db}


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "index.html",
        db=db
    )


@app.route("/borrow")
def borrow():
    return render_template(
        "borrow.html"
    )
