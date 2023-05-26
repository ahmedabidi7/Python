from mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.location = data_dict['location']
        self.language = data_dict['language']
        self.comment = data_dict['comment']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * from users;"
        results  = connectToMySQL("dojo_survey_schema").query_db(query)
        all_users = []
        for row in results:
            user = cls(row)
            all_users.append(user)
        return all_users

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO dojos (name, location,language,comment)
        VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);
        """
        result  = connectToMySQL("dojo_survey_schema").query_db(query, data)
        print(result)
        return result
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("You must comment.")
            is_valid = False
        return is_valid
