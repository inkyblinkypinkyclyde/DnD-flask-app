from crypt import methods
from flask import render_template, request, redirect, Blueprint
from models.character import *
from models.turn import Turn
import repositories.character_repository as character_repository
import repositories.turn_repository as turn_repository
from datetime import date

characters_blueprint = Blueprint("characters", __name__)

@characters_blueprint.route('/characters')
def all_characters():
    characters = character_repository.select_all()
    return render_template('characters/index.html', title="All Characters", characters = characters)

@characters_blueprint.route('/characters', methods=['POST'])
def new_character():
    name = request.form['name']
    max_HP = request.form['hp']
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
    character = Character(
        name,
        max_HP,
        HP,
        AC,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        character_class,
        race,
        region)
    character_repository.save(character)
    return redirect('/characters')

@characters_blueprint.route('/characters/<id>/delete')
def delete_character_check(id):
    character = character_repository.select(id)
    return render_template('/characters/delete.html', character = character)

@characters_blueprint.route('/characters/<id>/remove')
def remove_character_confirmed(id):
    character_repository.delete(id)
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
        character_repository.update_initiative(str(character.id), initiative)
    return redirect('/encounter')

@characters_blueprint.route('/encounter')
def encounter(): 
    characters = character_repository.select_all_ready()
    turns = turn_repository.select_all()
    return render_template('encounter.html', characters=characters, turns=turns)

@characters_blueprint.route('/encounter/attack/<id>', methods=['POST'])
def do_attack(id):
    d_size = request.form['d_size']
    d_number = request.form['d_number']
    manual_entry = request.form['manual_entry']
    victim = character_repository.select(request.form['victim'])
    attacker = character_repository.select(id)
    if int(manual_entry) < 1:
        total_damage = Character.carry_out_attack(attacker, d_size, d_number, victim)
        new_victim_hp = victim.HP - total_damage
        character_repository.change_hp(victim.id, new_victim_hp)
        string = f'{attacker.name} hit {victim.name} doing {total_damage} damage'
        turn = Turn(date.today(), string)
        turn_repository.save(turn)
    else:
        new_victim_hp = victim.HP - int(manual_entry)
        character_repository.change_hp(victim.id, new_victim_hp)
        string = f'{attacker.name} hit {victim.name} doing {manual_entry} damage'
        turn = Turn(date.today(), string)
        turn_repository.save(turn)
    
    return redirect('/encounter')

@characters_blueprint.route('/encounter/heal/<id>', methods=['POST'])
def do_heal(id):
    d_size = request.form['d_size']
    d_number = request.form['d_number']
    manual_entry = request.form['manual_entry']
    victim = character_repository.select(request.form['victim'])
    attacker = character_repository.select(id)
    if int(manual_entry) < 1:
        total_damage = Character.calculate_hp_change(attacker, d_size, d_number)
        new_victim_hp = victim.HP + total_damage
        if new_victim_hp > victim.max_HP:
            new_victim_hp = victim.max_HP
        character_repository.change_hp(victim.id, new_victim_hp)
        string = f'{attacker.name} healed {victim.name} by {total_damage}'
        turn = Turn(date.today(), string)
        turn_repository.save(turn)
    else:
        new_victim_hp = victim.HP + int(manual_entry)
        character_repository.change_hp(victim.id, new_victim_hp)
        string = f'{attacker.name} healed {victim.name} by {manual_entry}'
        turn = Turn(date.today(), string)
        turn_repository.save(turn)
    

    return redirect('/encounter')

@characters_blueprint.route('/<id>/edit')
def edit_page(id):
    character = character_repository.select(id)
    return render_template('/characters/edit.html', character = character)

@characters_blueprint.route('/<id>/edit', methods=['POST'])
def edit(id):
    name            = request.form['name']
    max_HP          = request.form['max_hp']
    HP              = request.form['hp']
    AC              = request.form['ac']
    strength        = request.form['strength']
    dexterity       = request.form['dexterity']
    constitution    = request.form['constitution']
    intelligence    = request.form['intelligence']
    wisdom          = request.form['wisdom']
    charisma        = request.form['charisma']
    character_class = request.form['character_class']
    race            = request.form['race']
    region          = request.form['region']
    in_encounter    = False
    initiative      = request.form['initiative']
    character = Character(
        name,
        max_HP,
        HP,
        AC,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        character_class,
        race,
        region,
        in_encounter,
        initiative,
        id)
    character_repository.update(character)
    return redirect('/characters')