from flask import render_template, request, redirect
from app import app
from models.characters import *
from models.character import *

@app.route('/characters')
def index():
    return render_template('index.html', title="Character entry", character_list = character_list)

@app.route('/characters', methods=['POST'])
def new_character():
    name = request.form['name']
    new_character = Character(name=name)
    add_new_character(new_character)
    return redirect('/characters')