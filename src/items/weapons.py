from models.item import Weapon
from src.utils.enums import WeaponType


class Dagger(Weapon):

    def __init__(self):
        super().__init__(
            name="Dagger",
            title="Кинжал",
            damage=4,
            weapon_type=WeaponType.light.value,
        )


class TwoDaggers(Weapon):

    def __init__(self):
        super().__init__(
            name="TwoDaggers",
            title="Парные Кинжалы",
            damage=4,
            times=2,
            weapon_type=WeaponType.light.value,
        )


class SwordOH(Weapon):

    def __init__(self):
        super().__init__(
            name="SwordOH",
            title="Одноручный Меч",
            damage=6,
            weapon_type=WeaponType.medium.value,
        )


class SwordBastard(Weapon):

    def __init__(self):
        super().__init__(
            name="SwordBastard",
            title="Полуторный Меч",
            damage=8,
            weapon_type=WeaponType.heavy.value,
        )


class SwordTH(Weapon):

    def __init__(self):
        super().__init__(
            name="SwordTH",
            title="Двуручный Меч",
            damage=10,
            weapon_type=WeaponType.heavy.value,
        )


class Axe(Weapon):

    def __init__(self):
        super().__init__(
            name="Axe",
            title="Секира",
            damage=6,
            times=2,
            weapon_type=WeaponType.heavy.value,
        )


class Bow(Weapon):

    def __init__(self):
        super().__init__(
            name="Bow",
            title="Лук",
            damage=6,
            weapon_type=WeaponType.ranged.value,
        )


class Fists(Weapon):

    def __init__(self):
        super().__init__(
            name="Fists",
            title="Кулаки",
            damage=4,
            times=2,
            weapon_type=WeaponType.medium.value,
        )
