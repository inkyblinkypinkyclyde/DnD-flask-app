import unittest
from models.character import Character

class TestCharacter(unittest.TestCase):
    
    def setUp(self):
        self.pippin = Character("Peregrin Took", 10, 15, 10, 10, 10, 10, 10, 10, 'Rogue', 'Halfling', 'The Shire')
        self.Angmar = Character("The Witch King Angmar", 200, 20, 20, 20, 20, 20, 20, 20, 'Numenorean', 'Paladin', 'Minas Morgul')
    
    def test_character_has_name(self):
        self.assertEqual("Peregrin Took", self.pippin.name)
    
    def test_character_has_HP(self):
        self.assertEqual(10, self.pippin.HP)

    def test_character_can_remove_HP(self):
        self.pippin.remove_1_HP()
        self.assertEqual(9, self.pippin.HP)

    def test_character_can_add_HP(self):
        self.pippin.add_1_HP()
        self.assertEqual(11, self.pippin.HP)

    def test_character_can_remove_AC(self):
        self.pippin.remove_1_AC()
        self.assertEqual(9, self.pippin.HP)

    def test_character_can_add_AC(self):
        self.pippin.add_1_AC()
        self.assertEqual(11, self.pippin.HP)

    def test_character_can_remove_HP_by_amount(self):
        self.pippin.remove_amount_HP(9)
        self.assertEqual(1, self.pippin.HP)
    
    def test_character_can_roll(self):
        self.assertEqual(1, self.pippin.roll(1))
    
    def test_character_can_return_ability_modifier(self):
        self.assertEqual(0, self.pippin.ability_modifier(self.pippin.strength))
    
    def test_character_has_max_carry_capacity(self):
        self.assertEqual(150, self.pippin.carry_capacity())
