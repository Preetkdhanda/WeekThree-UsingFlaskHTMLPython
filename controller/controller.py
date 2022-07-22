from flask import render_template 
from app import app
from modules.booklist import books

@app.route("/books")
def index():
    return render_template("index.html", title="Home", all_orders=books)

@app.route("/books/<index>")
def singleorder(index):
    index = int(index)
    return render_template("singlebook.html", title="Book", order=books[index])

