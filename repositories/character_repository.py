from db.run_sql import run_sql
from models.character import Character

def save(character):
    sql = "INSERT INTO characters (name, HP, AC, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, race, region, in_encounter) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [character.name, character.HP, character.AC, character.strength, character.dexterity, character.constitution, character.intelligence, character.wisdom, character.charisma, character.character_class, character.race, character.region, character.in_encounter]
    results = run_sql(sql, values)
    id = results[0]['id']
    character.id = id
    return character

def select_all():
    characters = []
    sql = "SELECT * FROM characters ORDER BY name"
    results = run_sql(sql)
    for row in results:
        character = Character(row['name'], row['hp'], row['ac'], row['strength'], row['dexterity'], row['constitution'], row['intelligence'], row['wisdom'], row['charisma'], row['character_class'], row['race'], row['region'], row['in_encounter'], row['initiative'], row['id'])
        characters.append(character)
    return characters

def select(id):
    character = None
    sql = "SELECT * FROM characters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        character = Character(result['name'], result['hp'], result['ac'], result['strength'], result['dexterity'], result['constitution'], result['intelligence'], result['wisdom'], result['charisma'], result['character_class'], result['race'], result['region'])
    return character

def delete_all():
    sql = 'DELETE FROM characters'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM characters WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(character):
    sql = 'UPDATE characters SET (name, HP, AC, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, race, region, in_encounter) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [character.name, character.HP, character.AC, character.strength, character.dexterity, character.constitution, character.intelligence, character.wisdom, character.charisma, character.character_class, character.race, character.region, character.initiative, character.id]
    run_sql(sql, values)

def add_to_encounter(id):
    sql = 'UPDATE characters SET in_encounter = %s WHERE id = %s'
    values = ['TRUE', id]
    run_sql(sql, values)

def select_all_ready():
    characters = []
    sql = "SELECT * FROM characters WHERE in_encounter = TRUE ORDER BY name"
    results = run_sql(sql)
    for row in results:
        character = Character(row['name'], row['hp'], row['ac'], row['strength'], row['dexterity'], row['constitution'], row['intelligence'], row['wisdom'], row['charisma'], row['character_class'], row['race'], row['region'], row['in_encounter'], row['id'])
        characters.append(character)
    return characters