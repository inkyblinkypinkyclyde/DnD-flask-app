from audioop import ratecv
from crypt import methods
from ctypes.wintypes import HPALETTE
from logging import raiseExceptions
from readline import set_history_length
from unicodedata import name
from flask import render_template, request, redirect, Blueprint
from models.character import *
import repositories.character_repository as character_repository

characters_blueprint = Blueprint("characters", __name__)

@characters_blueprint.route('/characters')
def all_characters():
    characters = character_repository.select_all()
    return render_template('characters/index.html', title="All Characters", characters = characters)

@characters_blueprint.route('/characters', methods=['POST'])
def new_character():
    name = request.form['name']
    HP = request.form['hp']
    AC = request.form['ac']
    strength = request.form['strength']
    dexterity = request.form['dexterity']
    constitution = request.form['constitution']
    intelligence = request.form['intelligence']
    wisdom = request.form['wisdom']
    charisma = request.form['charisma']
    character_class = request.form['character_class']
    race = request.form['race']
    region = request.form['region']
    character = Character(name, HP, AC, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, race, region)
    character_repository.save(character)
    return redirect('/characters')


@characters_blueprint.route('/create_new_encounter/<id>')
def add_to_encounter(id):
    character_repository.add_to_encounter(id)
    # breakpoint()
    return redirect('/characters')

@characters_blueprint.route('/lobby')
def all_characters_ready():
    characters = character_repository.select_all_ready()
    return render_template('lobby.html', title="All Characters", characters = characters)
