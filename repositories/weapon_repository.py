from db.run_sql import run_sql
from models.weapons import Weapon

def save(weapon):
    sql = "INSERT INTO weapons (name, d_size, d_number, damage_type, versatile, v_d_size, v_d_number, value, weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [
        weapon.name,
        weapon.d_size,
        weapon.d_number,
        weapon.damage_type,
        weapon.versatile,
        weapon.v_d_size,
        weapon.v_d_number,
        weapon.value,
        weapon.weight
    ]
    results = run_sql(sql, values)
    id = results[0]['id']
    weapon.id = id
    return weapon

def select_all():
    pass

def select_id(id):
    pass

def delete_all():
    sql = 'DELETE FROM weapons'
    run_sql(sql)