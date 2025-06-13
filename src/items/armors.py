from models.item import Armor
from src.utils.enums import ArmorType
from src.models.effect import Shield


class LightShield(Armor):

    def __init__(self):
        effect = Shield(
            name="LightShield",
            title="Щит",
            item=self,
        )
        super().__init__(
            name="LightShield",
            title="Щит",
            effect=effect,
            defence=2,
            armor_type=ArmorType.light_shield.value,
        )


class MediumShield(Armor):

    def __init__(self):
        effect = Shield(
            name="MediumShield",
            title="Щит",
            item=self,
        )
        super().__init__(
            name="MediumShield",
            title="Щит",
            effect=effect,
            defence=4,
            armor_type=ArmorType.medium_shield.value,
        )


class GreatShield(Armor):

    def __init__(self):
        effect = Shield(
            name="GreatShield",
            title="Щит",
            item=self,
        )
        super().__init__(
            name="GreatShield",
            title="Щит",
            effect=effect,
            defence=6,
            armor_type=ArmorType.great_shield.value,
        )
