import pdb
from models.character import Character

import repositories.character_repository as character_repository

character_repository.delete_all()

pippin = Character("Peregrin Took", 10, 15, 10, 10, 10, 10, 10, 10, 'Rogue', 'Halfling', 'The Shire')
character_repository.save(pippin)
Angmar = Character("The Witch King Angmar", 200, 20, 20, 20, 20, 20, 20, 20, 'Numenorean', 'Paladin', 'Minas Morgul')
character_repository.save(Angmar)
gimli = Character("Gimli son of Gloin", 18, 15, 17, 10, 19, 11, 9, 11, 'Fighter', 'Dwarf', 'Mines of Moria')
character_repository.save(gimli)
aragorn = Character("Aragorn son or Arathorn", 16, 15, 12, 17, 16, 19, 17, 14, 'Ranger', 'Human', 'The Woods')
character_repository.save(aragorn)

pdb.set_trace()