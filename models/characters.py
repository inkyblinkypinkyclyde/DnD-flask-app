from models.character import *

character1 = Character("Luna")
character2 = Character("Gabe")

character_list = [character1, character2]

def add_new_character(new_character):
    character_list.append(new_character)