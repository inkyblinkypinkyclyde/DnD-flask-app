
from models.character import Character
# from character import Character

character1 = Character("Luna", 20, 10)
character2 = Character("Gabe", 25, 15)

character_list = [character1, character2]

def add_new_character(new_character):
    character_list.append(new_character)

def remove_1_hp(character):
    for character_in_list in character_list:
        if character_in_list.name == character:
            character_in_list.HP -= 1
            print(character_in_list.HP)
            break

def add_1_hp(character):
    for character_in_list in character_list:
        if character_in_list.name == character:
            character_in_list.HP += 1
            print(character_in_list.HP)
            break