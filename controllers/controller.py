from argparse import Action
from ctypes.wintypes import HPALETTE
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
    HP = request.form['HP']
    AC = request.form['AC']
    new_character = Character(name=name, HP=HP, AC=AC)
    add_new_character(new_character)
    return redirect('/characters')

@app.route('/characters/remove_HP/<name>', methods=['Post'])
def lower_hp(name):
    remove_1_hp(name)
    return redirect('/characters')

@app.route('/characters/add_HP/<name>', methods=['Post'])
def raise_hp(name):
    add_1_hp(name)
    return redirect('/characters')
