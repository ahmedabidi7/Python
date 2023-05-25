from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.age = data_dict['age']
        self.dojo_id = data_dict['dojo_id']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_specefic(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results  = connectToMySQL(DATABASE).query_db(query,data)

        all_users = []
        for row in results:
            user = cls(row)
            all_users.append(user)
        print(all_users)
        return all_users

    @classmethod
    def create(cls,data):

        query = """
        INSERT INTO ninjas (first_name, last_name,age,dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM ninjas WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
