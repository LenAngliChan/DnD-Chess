from src.abstractions.tools import BasicAttribute


class MagicType(BasicAttribute):
    force = "force"
    fire = "fire"
    ice = "ice"
    psychic = "psychic"
    radiant = "radiant"
    dark = "dark"


class WeaponType(BasicAttribute):
    heavy = "heavy"
    medium = "medium"
    light = "light"
    bow = "bow"


class ArmorType(BasicAttribute):
    shield = "shield"


class PerkType(BasicAttribute):
    melee = "melee"
    ranged = "ranged"
    elemental = "elemental"
    heal = "heal"
    shield = "shield"
    effect = "effect"


class PerkStatus(BasicAttribute):
    active = "active"
    done = "done"
    blocked = "blocked"


class PerkModifier(BasicAttribute):
    standard = "standard"
    advantage = "advantage"
    vulnerability = "vulnerability"


class Time(BasicAttribute):
    day = "day"
    night = "night"


class ActionType(BasicAttribute):
    move = "move"
    use = "use"
    defend = "defend"


class FigureStatus(BasicAttribute):
    alive = "alive"
    captive = "captive"
    killed = "killed"


class ActionKWArgs(BasicAttribute):
    domain_bonus = "domain_power"
    building_bonus = "tower_defence"
