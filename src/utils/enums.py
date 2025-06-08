from utils.tools import BaseAttribute


class MagicType(BaseAttribute):
    force = "Сила"
    fire = "Огонь"
    ice = "Лед"
    psychic = "Психический"
    radiant = "Свет"
    dark = "Тьма"


class WeaponType(BaseAttribute):
    heavy = "Тяжелый"
    medium = "Фехтовальный"
    light = "Легкий"
    ranged = "Дальний"


class ArmorType(BaseAttribute):
    light_shield = "Легкий"
    medium_shield = "Средний"
    great_shield = "Тяжелый"


class PerkType(BaseAttribute):
    melee = "Контакное"
    ranged = "Стрелковое"
    elemental = "Магия"
    heal = "Лечение"
    shield = "Защита"
    effect = "Эффект"


class PerkStatus(BaseAttribute):
    active = "Активный"
    done = "Использован"
    blocked = "Заблокирован"


class PerkModifier(BaseAttribute):
    standard = "Обычный"
    advantage = "Преимущество"
    vulnerability = "Уязвимость"


class Time(BaseAttribute):
    day = "Красный"
    night = "Синий"
    dragon = "Серый"


class ActionType(BaseAttribute):
    move = "Движение"
    use = "Использование"
    defend = "Пропуск хода"


class FigureStatus(BaseAttribute):
    alive = "Живой"
    captive = "Захвачен"
    killed = "Убит"


class ActionKWArgs(BaseAttribute):
    domain_bonus = "Сила Домена"
    building_bonus = "Защита Башни"
