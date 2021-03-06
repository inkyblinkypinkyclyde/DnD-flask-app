from db.run_sql import run_sql
from models.character import Character

def save(character):
    sql = "INSERT INTO characters (name, max_HP, HP, AC, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, race, region, in_encounter, initiative) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [
        character.name,
        character.max_HP,
        character.HP,
        character.AC,
        character.strength,
        character.dexterity,
        character.constitution,
        character.intelligence,
        character.wisdom,
        character.charisma,
        character.character_class,
        character.race,
        character.region,
        character.in_encounter,
        character.initiative
        ]
    results = run_sql(sql, values)
    # breakpoint()
    id = results[0]['id']
    character.id = id
    return character

def select_all():
    characters = []
    sql = "SELECT * FROM characters ORDER BY name"
    results = run_sql(sql)
    for row in results:
        character = Character(
            row['name'],
            row['max_hp'],
            row['hp'],
            row['ac'],
            row['strength'],
            row['dexterity'],
            row['constitution'],
            row['intelligence'],
            row['wisdom'],
            row['charisma'],
            row['character_class'],
            row['race'],
            row['region'],
            row['in_encounter'],
            row['initiative'],
            row['id']
            )
        characters.append(character)
    return characters

def select(id):
    character = None
    sql = "SELECT * FROM characters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        character = Character(
            result['name'],
            result['max_hp'],
            result['hp'],
            result['ac'],
            result['strength'],
            result['dexterity'],
            result['constitution'],
            result['intelligence'],
            result['wisdom'],
            result['charisma'],
            result['character_class'],
            result['race'],
            result['region'],
            result['in_encounter'],
            result['initiative'],
            result['id'])
    return character

def delete_all():
    sql = 'DELETE FROM characters'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM characters WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(character):
    sql = 'UPDATE characters SET (name, max_HP, HP, AC, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, race, region, in_encounter, initiative) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [
        character.name,
        character.max_HP,
        character.HP,
        character.AC,
        character.strength,
        character.dexterity,
        character.constitution,
        character.intelligence,
        character.wisdom,
        character.charisma,
        character.character_class,
        character.race,
        character.region,
        character.in_encounter,
        character.initiative,
        character.id
        ]
    run_sql(sql, values)

def add_to_encounter(id):
    sql = 'UPDATE characters SET in_encounter = %s WHERE id = %s'
    values = ['TRUE', id]
    run_sql(sql, values)

def remove_from_encounter(id):
    sql = 'UPDATE characters SET in_encounter = %s WHERE id = %s'
    values = ['FALSE', id]
    run_sql(sql, values)

def select_all_ready():
    characters = []
    sql = "SELECT * FROM characters WHERE in_encounter = TRUE ORDER BY initiative DESC"
    results = run_sql(sql)
    for row in results:
        character = Character(
            row['name'],
            row['max_hp'],
            row['hp'],
            row['ac'],
            row['strength'],
            row['dexterity'],
            row['constitution'],
            row['intelligence'],
            row['wisdom'],
            row['charisma'],
            row['character_class'],
            row['race'],
            row['region'],
            row['in_encounter'],
            row['initiative'],
            row['id']
            )
        characters.append(character)
    return characters

def count_number_in_encounter():
    pass

def update_initiative(id, initiative):
    sql = "UPDATE characters SET initiative = %s WHERE id = %s"
    values = [initiative, id]
    print(f'the sql being passed in is {sql} and the initiative is {initiative} and the id is {id}')
    run_sql(sql, values)

def change_hp(id, amount):
    sql = "UPDATE characters SET hp = %s WHERE id = %s"
    values = [amount, id]
    run_sql(sql, values)
