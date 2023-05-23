from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def greeting():
    return "Here you can find data about a pokemon!"

@app.route("/pokeapi", methods = ['GET', 'POST'])
def get_pokemon():
    if request.method == 'POST':
        name = request.form.get('name')
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
            return render_template('pokeapi.html', poke_dict=poke_dict)
    return render_template('pokeapi.html')
