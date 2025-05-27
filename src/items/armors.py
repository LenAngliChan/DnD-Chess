from models.item import Armor
from src.utils.enums import ArmorType


class LightShield(Armor):

    def __init__(self):
        super().__init__(
            name="LightShield",
            defence=2,
            armor_type=ArmorType.shield.value,
        )


class MediumShield(Armor):

    def __init__(self):
        super().__init__(
            name="MediumShield",
            defence=4,
            armor_type=ArmorType.shield.value,
        )


class GreatShield(Armor):

    def __init__(self):
        super().__init__(
            name="GreatShield",
            defence=6,
            armor_type=ArmorType.shield.value,
        )
