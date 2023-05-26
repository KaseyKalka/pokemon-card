from flask import request, render_template
import requests
from app.forms import LoginForm, Get_Pokemon_Form, SignupForm
from app import app

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        return 'Successfully logged in!'
    else:
        return render_template('login.html', form=form)
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        return 'Thanks for signing up!'
    else:
        return render_template('signup.html', form=form)

@app.route("/pokeapi", methods = ['GET', 'POST'])
def get_pokemon():
    form = Get_Pokemon_Form()
    if request.method == 'POST' and form.validate_on_submit():
        #pokemon = form.get_pokemon.data.lower()
        print('posting')
        name = form.get_pokemon.data.lower()
        print(name)
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
            return render_template('pokeapi.html', poke_dict=poke_dict, form=form)
    return render_template('pokeapi.html', form=form)

