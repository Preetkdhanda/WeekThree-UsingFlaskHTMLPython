from flask import render_template, request, redirect
from app import app
from modules.booklist import *
from modules.book import *


@app.route("/books")
def index():
    return render_template("books/index.html", title="Home", all_books=books)

@app.route("/books/addanewbook")
def new():
       return render_template("books/addanewbook.html")

@app.route("/books", methods=["POST"])
def addanewbook():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title,author,genre)

    add_book(new_book)
  
    return redirect("/books")
   
@app.route("/books/removeabook")
def remove():
    return render_template("books/removeabook.html")

@app.route("/books", methods=["delete"])
def delete():
    title = request.form["title"]

    removed_book = Book(title)

    remove_book(removed_book)
  
    return redirect("/books")

