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



@characters_blueprint.route('/add_to_encounter/<id>')
def add_to_encounter(id):
    character_repository.add_to_encounter(id)
    return redirect('/characters')

@characters_blueprint.route('/remove_from_encounter/<id>')
def remove_from_encounter(id):
    character_repository.remove_from_encounter(id)
    return redirect('/characters')

@characters_blueprint.route('/lobby')
def all_characters_ready():
    characters = character_repository.select_all_ready()
    return render_template('lobby.html', title="All Characters", characters = characters)

@characters_blueprint.route('/update_initiative', methods=['POST'])
def update_initiative():
    characters = character_repository.select_all_ready()
    for character in characters:
        input_name = character.id
        initiative = request.form[str(input_name)]
        print(f'The character is {character.name} and their current initiative is {character.initiative} it is being updated to {initiative}')
        character_repository.update_initiative(str(character.id), initiative)
    return redirect('/encounter')

@characters_blueprint.route('/encounter')
def encounter(): 
    characters = character_repository.select_all_ready()
    return render_template('encounter.html', characters=characters)
