from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Book :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.author = data['author']
        self.thoughts = data['thoughts']
        self.poster = user.User.get_by_id({'id':self.user_id}).name

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM books;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        recp = []
        for row in results:
            recp.append(cls(row))
        return recp

    @classmethod
    def add_book(cls, data):
        query = """
        INSERT INTO books (user_id, title, author,thoughts) 
        VALUES (%(user_id)s,%(title)s,%(author)s,%(thoughts)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])< 2:
            flash("title must be at least 3")
            is_valid = False
        if len(data['author'])< 3:
            flash("author too short")
            is_valid = False
        if len(data['thoughts'])< 10:
            flash("thoughts too short")
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls, data):
        query = """
        delete from books where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_book(cls, data):
        query = """
        UPDATE books SET title = %(title)s, author = %(author)s, thoughts= %(thoughts)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM books WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
