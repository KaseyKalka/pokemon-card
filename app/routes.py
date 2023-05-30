from flask import request, render_template, redirect, url_for, flash
import requests
from app.forms import LoginForm, Get_Pokemon_Form, SignupForm
from app import app, db
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

# AUTHENTICATION
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f'Welcome back {queried_user.first_name}!', 'success')
            return redirect(url_for('home'))
        else: 
            error = 'Invalid email or password'
            return render_template('login.html', form=form, error=error)
    else:
        return render_template('login.html', form=form)
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out.', 'warning')
    return redirect(url_for('login'))

# SIGN UP FORM
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():

        # This data is coming from signup form
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data.lower(),
            'password': form.password.data
        }
        
        # Create user instance
        new_user = User()

        # Set user data to user attributes
        new_user.from_dict(user_data)

        # Save to db
        db.session.add(new_user)
        db.session.commit()

        flash(f'Thanks for signing up {user_data["first_name"]}!', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)

@app.route('/pokeapi', methods = ['GET', 'POST'])
@login_required
def get_pokemon():
    form = Get_Pokemon_Form()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.get_pokemon.data.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            poke_dict = {
                'name': data['name'],
                'ability': data['abilities'][0]['ability']['name'],
                'basexp': data['base_experience'],
                'sprite': data['sprites']['front_shiny'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat']
            }
            flash(f'Here is a card for {name}', 'warning')
            return render_template('pokeapi.html', poke_dict=poke_dict, form=form)
        else:
            flash(f"Sorry, couldn't find that pokemon.", 'danger')
            return render_template('pokeapi.html', form=form)
    return render_template('pokeapi.html', form=form)

