from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.book import Book

@app.route('/books/new')
def new_book():
    if 'user_id' in session:
        return render_template("new_book.html")
    return redirect('/')

@app.route('/books/create' ,methods=['POST'])
def create_book():
    if(Book.validate(request.form)):
        data = {
            **request.form,'user_id':session['user_id']
        }
        Book.add_book(data)
        return redirect('/dashboard')
    return redirect('/books/new')

@app.route('/books/<book_id>/destroy/')
def delete_book(book_id):
    if (session['user_id'] == Book.get_by_id({'id':book_id}).user_id):
        Book.delete({'id':book_id})
    return redirect('/dashboard')

@app.route('/books/<book_id>/edit')
def edit_book(book_id):
    if 'user_id' in session:
        one_book=Book.get_by_id({'id':book_id})
        return render_template("edit_book.html", book=one_book)
    return redirect('/')

@app.route('/books/<book_id>/update' ,methods=['POST'])
def update_book(book_id):
    if(Book.validate(request.form)):
        Book.edit_book(request.form)
        return redirect('/dashboard')
    return redirect('/books/'+str(book_id)+'/edit')

@app.route('/books/<int:book_id>')
def one_book(book_id):
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        one_book=Book.get_by_id({'id':book_id})
        return render_template('one.html',book=one_book,user=user)
    return redirect('/')
