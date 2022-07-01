import random
import math
class Character():
    def __init__(
        self,
        name,
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
        in_encounter = False,
        initiative = 0,
        id = None
        ):
        self.name = name
        self.HP = HP
        self.AC = AC
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.character_class = character_class
        self.race = race
        self.region = region
        self.in_encounter = in_encounter
        self.initiative = initiative
        self.id = id

    ## ALTER BY ONE TESTS ##
    def remove_1_HP(self):
        self.HP -= 1
    def add_1_HP(self):
        self.HP += 1
    def remove_1_AC(self):
        self.HP -= 1
    def add_1_AC(self):
        self.HP += 1

    ## ALTER BY AMOUNT TESTS ##
    def remove_amount_HP(self, amount):
        self.HP -= amount
    def add_amount_HP(self, amount):
        self.HP += amount
    def remove_amount_AC(self, amount):
        self.AC -= amount
    def add_amount_AC(self, amount):
        self.AC += amount
    
    ## GAME MECHANIC TESTS ##
    def roll(self, size):
        return random.randint(1, size)

    def ability_modifier(self, ability):
        ability_modifier = math.floor((ability - 10)/2)
        return ability_modifier

    def carry_capacity(self):
        return self.strength * 15
    
    ## DC CHECKS ##



    

