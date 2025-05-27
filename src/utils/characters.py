from dataclasses import dataclass

from src.utils.constants import (
    BASE_CHARACTERISTIC,
    BASE_HIT_POINTS,
    BASE_HP_COEFFICIENT,
    BASE_HIT_CHANCE,
    BASE_DEFENCE,
    BASE_CRIT_CHANCE,
    BASE_CRIT_RESISTANCE,
    BASE_MAGIC_RESISTANCE,
)


@dataclass
class Character:
    strength: int = BASE_CHARACTERISTIC
    constitution: int = BASE_CHARACTERISTIC
    dexterity: int = BASE_CHARACTERISTIC
    intelligence: int = BASE_CHARACTERISTIC
    wisdom: int = BASE_CHARACTERISTIC
    charisma: int = BASE_CHARACTERISTIC
    base_hit_points: int = BASE_HIT_POINTS
    base_hp_coefficient: int = BASE_HP_COEFFICIENT
    base_hit_chance: int = BASE_HIT_CHANCE
    base_defence: int = BASE_DEFENCE
    base_crit_chance: int = BASE_CRIT_CHANCE
    base_crit_resistance: int = BASE_CRIT_RESISTANCE
    base_magic_resistance: int = BASE_MAGIC_RESISTANCE


barbarian = Character(
    strength=16,
    constitution=16,
    dexterity=10,
    intelligence=8,
    wisdom=8,
    charisma=8,
    base_hit_points=10,
    base_hp_coefficient=5,
)
bard = Character(
    strength=8,
    constitution=8,
    dexterity=16,
    intelligence=10,
    wisdom=8,
    charisma=16,
    base_hit_points=8,
    base_hp_coefficient=4,
)
cleric = Character(
    strength=10,
    constitution=16,
    dexterity=8,
    intelligence=8,
    wisdom=16,
    charisma=8,
    base_hit_points=12,
    base_hp_coefficient=6,
)
druid = Character(
    strength=10,
    constitution=12,
    dexterity=12,
    intelligence=8,
    wisdom=8,
    charisma=16,
    base_hit_points=10,
    base_hp_coefficient=5,
)
fighter = Character(
    strength=16,
    constitution=14,
    dexterity=12,
    intelligence=8,
    wisdom=8,
    charisma=8,
    base_hit_points=10,
    base_hp_coefficient=5,
    base_crit_chance=2,
)
monk = Character(
    strength=10,
    constitution=14,
    dexterity=16,
    intelligence=8,
    wisdom=10,
    charisma=8,
    base_hit_points=10,
    base_hp_coefficient=5,
)
paladin = Character(
    strength=16,
    constitution=10,
    dexterity=10,
    intelligence=8,
    wisdom=8,
    charisma=14,
    base_hit_points=10,
    base_hp_coefficient=4,
)
ranger = Character(
    strength=10,
    constitution=12,
    dexterity=16,
    intelligence=10,
    wisdom=10,
    charisma=8,
    base_hit_points=8,
    base_hp_coefficient=4,
)
rogue = Character(
    strength=10,
    constitution=10,
    dexterity=16,
    intelligence=10,
    wisdom=10,
    charisma=10,
    base_hit_points=8,
    base_hp_coefficient=3,
    base_crit_chance=3,
)
sorcerer = Character(
    strength=8,
    constitution=12,
    dexterity=12,
    intelligence=16,
    wisdom=8,
    charisma=10,
    base_hit_points=8,
    base_hp_coefficient=3,
)
warlock = Character(
    strength=10,
    constitution=12,
    dexterity=12,
    intelligence=8,
    wisdom=16,
    charisma=8,
    base_hit_points=6,
    base_hp_coefficient=3,
    base_crit_chance=2,
)
wizard = Character(
    strength=10,
    constitution=10,
    dexterity=10,
    intelligence=16,
    wisdom=10,
    charisma=10,
    base_hit_points=8,
    base_hp_coefficient=3,
)
