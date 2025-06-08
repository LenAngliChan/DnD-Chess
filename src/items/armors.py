from models.item import Armor
from src.utils.enums import ArmorType


class LightShield(Armor):

    def __init__(self):
        super().__init__(
            name="LightShield",
            title="Щит",
            defence=2,
            armor_type=ArmorType.light_shield.value,
        )


class MediumShield(Armor):

    def __init__(self):
        super().__init__(
            name="MediumShield",
            title="Щит",
            defence=4,
            armor_type=ArmorType.medium_shield.value,
        )


class GreatShield(Armor):

    def __init__(self):
        super().__init__(
            name="GreatShield",
            title="Щит",
            defence=6,
            armor_type=ArmorType.great_shield.value,
        )
