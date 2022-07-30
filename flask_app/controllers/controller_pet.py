from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.model_user import User
from flask_app.models.model_pet import Pet
from flask_app.models.model_post import Post

@app.route('/pet/new')
def new_pet():
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'id': session['user_id']
    }

    user = User.get_one(data)
    return render_template('new.html', user=user)

@app.route('/pet/add', methods=['POST'])
def add_pet():
    if not Pet.validate_pet(request.form):
        return redirect('/pet/new')

    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        'breed': request.form['breed'],
        'likes': request.form['likes'],
        'birthday': request.form['birthday'],
        'user_id': session['user_id']
    }

    Pet.create_pet(data)
    return redirect('/dashboard')

@app.route('/pet/<int:id>/edit')
def edit_pet(id):
    if 'user_id' not in session:
        return redirect('/')
        
    data = {
        'id': session['user_id']
    }
    pet_data = {
        'id': id
    }
    user = User.get_one(data)
    pet = Pet.get_one(pet_data)
    return render_template('edit.html', user=user, pet=pet)

@app.route('/pet/<int:id>/update', methods=['POST'])
def update_pet(id):
    if not Pet.validate_pet(request.form):
        return redirect(f'/pet/{id}/edit')

    Pet.update_one(request.form)
    return redirect(f'/pet/{id}')

@app.route('/pet/<int:id>')
def display_pet(id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    pet_data = {
        'id': id
    }

    post_data = {
        'id': id
    }
    post = Post.get_all_posts_by_users(post_data)
    user = User.get_one(data)
    pets = Pet.get_one_with_user(pet_data)


    print(post)
    return render_template('show.html', user=user, pets=pets, post=post)

@app.route('/pet/<int:id>/delete')
def delete_one(id):
    data = {
        'id': id
    }

    Pet.delete_one(data)

    return redirect('/dashboard')

@app.route('/adopt')
def display_rescue():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('rescue.html')