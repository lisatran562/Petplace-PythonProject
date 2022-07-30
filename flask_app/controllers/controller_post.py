from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_user import User
from flask_app.models.model_pet import Pet
from flask_app.models.model_post import Post


@app.route('/post/new', methods=['POST'])
def add_post():
    id = request.form['id']
    if not Post.validate_post(request.form):
        return redirect(f'/pet/{id}')

    Post.create_one(request.form)
    return redirect(f'/pet/{id}')

