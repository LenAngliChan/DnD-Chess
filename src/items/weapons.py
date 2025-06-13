from models.item import Weapon
from src.utils.enums import WeaponType
from src.models.effect import Cut, Crush, Pierce


class Dagger(Weapon):

    def __init__(self):
        effect = Pierce(
            name="Dagger",
            title="Кинжал",
            item=self,
        )
        super().__init__(
            name="Dagger",
            title="Кинжал",
            effect=effect,
            damage=4,
            weapon_type=WeaponType.light.value,
        )


class TwoDaggers(Weapon):

    def __init__(self):
        effect = Pierce(
            name="TwoDaggers",
            title="Парные Кинжалы",
            item=self,
        )
        super().__init__(
            name="TwoDaggers",
            title="Парные Кинжалы",
            effect=effect,
            damage=4,
            times=2,
            weapon_type=WeaponType.light.value,
        )


class SwordOH(Weapon):

    def __init__(self):
        effect = Cut(
            name="SwordOH",
            title="Одноручный Меч",
            item=self,
        )
        super().__init__(
            name="SwordOH",
            title="Одноручный Меч",
            effect=effect,
            damage=6,
            weapon_type=WeaponType.medium.value,
        )


class SwordBastard(Weapon):

    def __init__(self):
        effect = Cut(
            name="SwordBastard",
            title="Полуторный Меч",
            item=self,
        )
        super().__init__(
            name="SwordBastard",
            title="Полуторный Меч",
            effect=effect,
            damage=8,
            weapon_type=WeaponType.heavy.value,
        )


class SwordTH(Weapon):

    def __init__(self):
        effect = Cut(
            name="SwordTH",
            title="Двуручный Меч",
            item=self,
        )
        super().__init__(
            name="SwordTH",
            title="Двуручный Меч",
            effect=effect,
            damage=10,
            weapon_type=WeaponType.heavy.value,
        )


class Axe(Weapon):

    def __init__(self):
        effect = Cut(
            name="Axe",
            title="Секира",
            item=self,
        )
        super().__init__(
            name="Axe",
            title="Секира",
            effect=effect,
            damage=6,
            times=2,
            weapon_type=WeaponType.heavy.value,
        )


class Bow(Weapon):

    def __init__(self):
        effect = Pierce(
            name="Bow",
            title="Лук",
            item=self,
        )
        super().__init__(
            name="Bow",
            title="Лук",
            effect=effect,
            damage=6,
            weapon_type=WeaponType.ranged.value,
        )


class Fists(Weapon):

    def __init__(self):
        effect = Crush(
            name="Fists",
            title="Кулаки",
            item=self,
        )
        super().__init__(
            name="Fists",
            title="Кулаки",
            effect=effect,
            damage=4,
            times=2,
            weapon_type=WeaponType.medium.value,
        )
