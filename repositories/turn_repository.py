from db.run_sql import run_sql
from models.turn import Turn

def save(turn):
    sql = "INSERT INTO turns (date, description) VALUES (%s, %s) RETURNING *"
    values = [
        turn.date,
        turn.description
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    turn.id = id
    return turn

def select_all():
    turns = []
    sql = "SELECT * FROM turns ORDER BY id DESC"
    results = run_sql(sql)
    for row in results:
        turn = Turn(
            row['date'],
            row['description'],
            row['id']
            )
        turns.append(turn)
    return turns

def delete_all():
    sql = 'DELETE FROM turns'
    run_sql(sql)
