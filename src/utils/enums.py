from src.abstractions.tools import BaseAttribute


class MagicType(BaseAttribute):
    force = "force"
    fire = "fire"
    ice = "ice"
    psychic = "psychic"
    radiant = "radiant"
    dark = "dark"


class WeaponType(BaseAttribute):
    heavy = "heavy"
    medium = "medium"
    light = "light"
    bow = "bow"


class ArmorType(BaseAttribute):
    light_shield = "light_shield"
    medium_shield = "medium_shield"
    great_shield = "great_shield"


class PerkType(BaseAttribute):
    melee = "melee"
    ranged = "ranged"
    elemental = "elemental"
    heal = "heal"
    shield = "shield"
    effect = "effect"


class PerkStatus(BaseAttribute):
    active = "active"
    done = "done"
    blocked = "blocked"


class PerkModifier(BaseAttribute):
    standard = "standard"
    advantage = "advantage"
    vulnerability = "vulnerability"


class Time(BaseAttribute):
    day = "day"
    night = "night"


class ActionType(BaseAttribute):
    move = "move"
    use = "use"
    defend = "defend"


class FigureStatus(BaseAttribute):
    alive = "alive"
    captive = "captive"
    killed = "killed"


class ActionKWArgs(BaseAttribute):
    domain_bonus = "domain_power"
    building_bonus = "tower_defence"
