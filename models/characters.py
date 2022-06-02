from models.character import *

character1 = Character("Luna", 15, 10, 1, 2)
character2 = Character("Gabe", 50, 20, 3, 9)

character_list = [character1, character2]

def add_new_character(new_character):
    character_list.append(new_character)