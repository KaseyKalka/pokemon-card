from flask import request, render_template, flash, redirect, url_for
import requests
from app.blueprints.main.forms import Get_Pokemon_Form
from . import main
from flask_login import login_required, current_user
from app.models import Pokemon, User
from app import db

@main.route("/")
@main.route('/home')
def home():
    pokemon = Pokemon.query.all()
    return render_template('home.html', pokemon=pokemon)

# MAIN
@main.route('/pokeapi', methods = ['GET', 'POST'])
@login_required
def get_pokemon():
    form = Get_Pokemon_Form()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.get_pokemon.data.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        if not Pokemon.is_known(name): 
            response = requests.get(url)
            if response.ok:
                data = response.json()
                poke_dict = {
                    'pokemon_name': data['name'],
                    "img_url": data['sprites']['other']['home']["front_default"],
                    'ability': data['abilities'][0]['ability']['name'],
                    'basexp': data['base_experience'],
                    'sprite': data['sprites']['front_shiny'],
                    'hp': data['stats'][0]['base_stat'],
                    'attack': data['stats'][1]['base_stat'],
                    'defense': data['stats'][2]['base_stat']
                }
        
                pokemon = Pokemon()
                pokemon.from_dict(poke_dict)

                pokemon.save_to_db()

                flash(f'Here is a card for {name}!', 'warning')
                return render_template('pokeapi.html', poke_dict=poke_dict, form=form)
            else:
                flash(f"Sorry, couldn't find that pokemon.", 'danger')
                return render_template('pokeapi.html', form=form)
        if Pokemon.is_known(name):
            pokemon = Pokemon.query.filter_by(pokemon_name=name).first()
            pokemon.to_dict()
            return render_template('pokeapi.html', poke_dict=pokemon, form=form)
    return render_template('pokeapi.html', form=form)

# CATCHING AND RELEASING
@main.route('/catch_pokemon/<string:pokemon_name>', methods=['GET', 'POST'])
@login_required
def catch_pokemon(pokemon_name):
    pokemon = Pokemon.query.get(pokemon_name)
    print(pokemon)
    if pokemon:
        current_user.pokemon_caught.append(pokemon)
        db.session.commit()

        flash(f'You caught a {pokemon.pokemon_name}! {pokemon.pokemon_name} has been added to your team.', 'success')
        return redirect(url_for('main.home'))
    else:
        flash('Sorry you did not catch the pokemon! Try again!', 'warning')
        return redirect(url_for('main.home')) 
    
@main.route('/release_pokemon/<string:pokemon_caught>')
@login_required
def release_pokemon(pokemon_caught):
    pokemon = Pokemon.query.get(pokemon_caught)
    if pokemon:
        current_user.pokemon.remove(pokemon_caught)
        db.session.commit()

        flash(f"You've released {pokemon.pokemon_name} back into the wild!")
        return redirect(url_for('main.home'))
    else:
        flash(f"You can't release a pokemon you haven't caught!")
        return redirect(url_for('main.home'))
