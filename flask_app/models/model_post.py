from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models import model_user

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.post = data['post']
        self.user_id = data['user_id']
        self.pet_id = data['pet_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO posts (post, user_id, pet_id) VALUES (%(post)s, %(user_id)s, %(pet_id)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all_posts_by_users(cls, data):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            list_posts = []
            for row in results:
                post = cls(row)
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
                post.user = user
                list_posts.append(post)
            return list_posts
        return False


    @staticmethod
    def validate_post(data):
        is_valid = True

        if len(data['post']) < 2:
            is_valid = False
            flash('Post must be at least 2 characters', 'err_post_post')

        return is_valid
