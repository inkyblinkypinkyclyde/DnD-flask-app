import pdb
from models.character import Character
from models.weapons import Weapon
import repositories.character_repository as character_repository
import repositories.weapon_repository as weapon_repository
import repositories.turn_repository as turn_repository


character_repository.delete_all()
weapon_repository.delete_all()
turn_repository.delete_all()



pippin = Character("Peregrin Took", 10, 10, 15, 10, 10, 10, 10, 10, 10, 'Rogue', 'Halfling', 'The Shire')
character_repository.save(pippin)
Angmar = Character("The Witch King Angmar", 200, 200, 20, 20, 20, 20, 20, 20, 20, 'Numenorean', 'Paladin', 'Minas Morgul')
character_repository.save(Angmar)
gimli = Character("Gimli son of Gloin", 18, 18, 15, 17, 10, 19, 11, 9, 11, 'Fighter', 'Dwarf', 'Mines of Moria')
character_repository.save(gimli)
aragorn = Character("Aragorn son or Arathorn", 16, 16, 15, 12, 17, 16, 19, 17, 14, 'Ranger', 'Human', 'The Woods')
character_repository.save(aragorn)

longsword = Weapon("Longsword", 8, 1, "slashing", True, 10, 1, 10, 3)
weapon_repository.save(longsword)
mace = Weapon("Mace", 6, 1, "bludgeoning", False, 6, 1, 8, 5)
weapon_repository.save(mace)
shortsword = Weapon("Shortsword", 6, 1, "piercing", True, 8, 1, 8, 2)
weapon_repository.save(shortsword)

pdb.set_trace()