DROP TABLE IF EXISTS characters;

CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    hp INT,
    ac INT,
    strength INT,
    dexterity INT,
    constitution INT,
    intelligence INT,
    wisdom INT,
    charisma INT,
    character_class VARCHAR(255),
    race VARCHAR(255),
    region VARCHAR(255)
);