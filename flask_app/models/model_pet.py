from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models import model_user

class Pet:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.age = data['age']
        self.likes = data['likes']
        self.birthday = data['birthday']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image = data['image']

    @classmethod
    def create_pet(cls, data):
        query = "INSERT INTO pets (name, breed, age, likes, birthday, user_id) VALUES (%(name)s, %(breed)s, %(age)s, %(likes)s, %(birthday)s, %(user_id)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all_pets_with_users(cls):
        query = "SELECT * FROM pets JOIN users ON pets.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        print(results)
        if results:
            pets = []
            for row in results:
                pet = cls(row)
                data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                    'image': row['image']
                }
                user = model_user.User(data)
                pet.user = user
                pets.append(pet)
            return pets
        return False

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM pets WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)

        if result:
            return cls(result[0])

        return False

    @classmethod
    def update_one(cls, data):
        query = "UPDATE pets SET name = %(name)s, breed = %(breed)s, age = %(age)s, birthday = %(birthday)s, likes = %(likes)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * FROM pets JOIN users ON pets.user_id = users.id WHERE pets.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            pets = []
            for row in result:
                pet = cls(row)
                data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                user = model_user.User(data)
                pet.user = user
                pets.append(pet)
            return pets
        return False

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM pets WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)

    @staticmethod
    def validate_pet(data):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash('Pet must have a name', 'err_pet_name')

        if len(data['breed']) < 1:
            is_valid = False
            flash('Pet must have a breed', 'err_pet_breed')

        if len(data['age']) < 1:
            is_valid = False
            flash("Please enter pet's age", 'err_pet_age')

        if len(data['birthday']) < 1:
            is_valid = False
            flash("Please enter pet's birthday", 'err_pet_birthday')

        if len(data['likes']) < 1:
            is_valid = False
            flash("Please enter your pet's likes", 'err_pet_likes')

        return is_valid