import pdb
from models.character import Character

import repositories.character_repository as character_repository

character_repository.delete_all()

pippin = Character("Peregrin Took", 10, 15, 10, 10, 10, 10, 10, 10, 'Rogue', 'Halfling', 'The Shire')
character_repository.save(pippin)
Angmar = Character("The Witch King Angmar", 200, 20, 20, 20, 20, 20, 20, 20, 'Numenorean', 'Paladin', 'Minas Morgul')
character_repository.save(Angmar)

pdb.set_trace()