from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Message :
    def __init__(self,data):
        self.id = data['id']
        self.s_user_id = data['s_user_id']
        self.r_user_id = data['r_user_id']
        self.message = data['message']
        self.sender = user.User.get_by_id({'id':self.s_user_id}).first_name
    
    @classmethod
    def send_msg(cls, data):
        query = """
        INSERT INTO messages (s_user_id, r_user_id, message) 
        VALUES (%(s_user_id)s,%(r_user_id)s,%(message)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_msgs(cls, data):
        query = """
        SELECT * FROM messages WHERE r_user_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        msgs = []
        for row in results:
            msgs.append(cls(row))
        return msgs

    @classmethod
    def delete(cls, data):
        query = """
        delete from messages where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

