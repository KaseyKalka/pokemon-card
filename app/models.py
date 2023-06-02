from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

caught_pokemon = db.Table(
    'caught_pokemon',
    db.Column('user_caught_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('pokemon_caught', db.String, db.ForeignKey('pokemon.pokemon_name'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    pokemon_caught = db.relationship('User',
        secondary = caught_pokemon,
        primaryjoin = (caught_pokemon.columns.user_caught_id == id),
        secondaryjoin = (caught_pokemon.columns.pokemon_caught == id),
        backref = db.backref('caught_pokemon', lazy='dynamic'),
        lazy='dynamic'
    )

    #hashes password at signup
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    #assigns values to columns
    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password = self.hash_password(user_data['password'])

class Pokemon(db.Model):
    pokemon_name = db.Column(db.String, primary_key=True)
    ability = db.Column(db.String, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    # FK
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def from_dict(self, poke_data):
        self.pokemon_name = poke_data['pokemon_name']
        self.ability = poke_data['ability']
        self.hp = poke_data['hp']
        self.defense = poke_data['defense']
        self.attack = poke_data['attack']
        self.user_id = poke_data['user_id']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)