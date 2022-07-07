import random

class Weapon():
    def __init__(
        self,
        name,
        d_size,
        d_number,
        damage_type,
        versatile,
        v_d_size,
        v_d_number,
        value,
        weight
        ):
        self.name = name
        self.d_size = d_size
        self.d_number = d_number
        self.damage_type = damage_type
        self.versatile = versatile
        self.v_d_size = v_d_size
        self.v_d_number = v_d_number
        self.value = value
        self.weight = weight

    def roll(self, size):
        return random.randint(1, size)

    def calculate_damage(self, d_size, d_number):
        return (self.roll(d_size))*d_number