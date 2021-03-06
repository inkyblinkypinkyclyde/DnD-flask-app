import random
import math
class Character():
    def __init__(
        self,
        name,
        max_hp,
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
        self.max_HP = max_hp
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
        return random.randint(1, int(size))

    def attack_roll(self, victim):
        roll = self.roll(20)
        if (roll + self.strength) > victim.AC:
            return True
        else:
            return False

    def calculate_hp_change(self, d_size, d_number):
        roll = self.roll(d_size)
        total = int(roll) * int(d_number)
        return total

    def carry_out_attack(self, d_size, d_number, victim):
        if self.attack_roll(victim):
            return self.calculate_hp_change(d_size, d_number)
        else:
            return 0

        
    def ability_modifier(self, ability):
        ability_modifier = math.floor((ability - 10)/2)
        return ability_modifier

    def carry_capacity(self):
        return self.strength * 15
    
    ## DC CHECKS ##



    

