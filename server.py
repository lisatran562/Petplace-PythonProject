from flask_app import app
from flask_app.controllers import controller_user, controller_pet, controller_post
from flask_app.config.mysqlconnection import connectToMySQL


if __name__=="__main__":
    app.run(debug=True)