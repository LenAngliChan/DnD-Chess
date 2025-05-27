from models.item import Weapon
from src.utils.enums import WeaponType


class Dagger(Weapon):

    def __init__(self):
        super().__init__(
            name="Dagger",
            damage=4,
            weapon_type=WeaponType.light.value,
        )


class TwoDaggers(Weapon):

    def __init__(self):
        super().__init__(
            name="TwoDaggers",
            damage=4,
            times=2,
            weapon_type=WeaponType.light.value,
        )


class SwordOH(Weapon):

    def __init__(self):
        super().__init__(
            name="SwordOH",
            damage=6,
            weapon_type=WeaponType.medium.value,
        )


class SwordBastard(Weapon):

    def __init__(self):
        super().__init__(
            name="SwordBastard",
            damage=8,
            weapon_type=WeaponType.heavy.value,
        )


class SwordTH(Weapon):

    def __init__(self):
        super().__init__(
            name="SwordTH",
            damage=10,
            weapon_type=WeaponType.heavy.value,
        )


class Axe(Weapon):

    def __init__(self):
        super().__init__(
            name="Axe",
            damage=6,
            times=2,
            weapon_type=WeaponType.heavy.value,
        )


class Bow(Weapon):

    def __init__(self):
        super().__init__(
            name="Bow",
            damage=6,
            weapon_type=WeaponType.bow.value,
        )


class Fists(Weapon):

    def __init__(self):
        super().__init__(
            name="Fists",
            damage=4,
            times=2,
            weapon_type=WeaponType.medium.value,
        )
