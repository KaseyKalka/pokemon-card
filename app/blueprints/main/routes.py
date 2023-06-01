from flask import request, render_template, flash
import requests
from app.blueprints.main.forms import Get_Pokemon_Form
from . import main
from flask_login import login_required
from app.models import Pokemon

@main.route("/")
@main.route('/home')
def home():
    pokemon = Pokemon.query.all()
    return render_template('home.html', pokemon=pokemon[::-1])

# MAIN
@main.route('/pokeapi', methods = ['GET', 'POST'])
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
            flash(f'Here is a card for {name}!', 'warning')
            return render_template('pokeapi.html', poke_dict=poke_dict, form=form)
        else:
            flash(f"Sorry, couldn't find that pokemon.", 'danger')
            return render_template('pokeapi.html', form=form)
    return render_template('pokeapi.html', form=form)

