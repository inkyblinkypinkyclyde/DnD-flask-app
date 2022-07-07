DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS weapons;
DROP TABLE IF EXISTS turns;


CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    max_hp INT,
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
    region VARCHAR(255),
    in_encounter BOOLEAN,
    initiative INT
);

CREATE TABLE weapons(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    d_size INT,
    d_number INT,
    damage_type VARCHAR(255),
    versatile BOOLEAN,
    v_d_size INT,
    v_d_number INT,
    value INT,
    weight INT
);

CREATE TABLE turns(
    id SERIAL PRIMARY KEY,
    date DATE,
    description VARCHAR(255)
)
