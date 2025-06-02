from typing import TYPE_CHECKING

from src.abstractions.item import BaseItem
from src.models.dice import DiceRoll, Dice, StaticDice
from src.utils.enums import MagicType, WeaponType, ArmorType

if TYPE_CHECKING:
    from src.abstractions.tools import BaseAttribute
    from src.abstractions.dice import BaseDice


class Item(BaseItem):
    """Модель предмета"""

    def __init__(
        self,
        name: str,
        value_dice: "BaseDice",
        attribute: "BaseAttribute",
        times: int = 1,
    ):
        """Инициализация предмета

        Args:
            name: имя предмета
            value_dice: кость (значение предмета)
            attribute: тип предмета
            times: количество бросков кости
        """
        value = DiceRoll(dice=value_dice, times=times)
        super().__init__(
            name=name,
            value=value,
            attribute=attribute,
        )

    def deal(self) -> int:
        """Выполнить действие предмета
        Делается бросок кости предмета

        Returns:
            int: значение
        """
        return self.value.action()


class Weapon(Item):
    """Модель оружия"""

    def __init__(
        self,
        name: str,
        damage: int = 4,
        weapon_type: "BaseAttribute" = WeaponType.medium.value,
        times: int = 1,
    ):
        """Инициализация оружия

        Args:
            name: имя оружия
            damage: урон оружия
            weapon_type: тип оружия
            times: количество бросков кости
        """
        value_dice = Dice(side=damage)
        super().__init__(
            name=name,
            value_dice=value_dice,
            attribute=weapon_type,
            times=times,
        )


class Spell(Item):
    """Модель заклинания"""

    def __init__(
        self,
        name: str,
        damage: int = 4,
        magic_type: "BaseAttribute" = MagicType.fire.value,
        times: int = 1,
    ):
        """Инициализация заклинания

        Args:
            name: имя заклинания
            damage: урон заклинания
            magic_type: тип заклинания
            times: количество бросков кости
        """
        value_dice = Dice(side=damage)
        super().__init__(
            name=name,
            value_dice=value_dice,
            attribute=magic_type,
            times=times,
        )


class Armor(Item):
    """Модель брони"""

    def __init__(
        self,
        name: str,
        defence: int = 4,
        armor_type: "BaseAttribute" = ArmorType.medium_shield.value,
    ):
        """Инициализация брони

        Args:
            name: имя брони
            defence: защита брони
            armor_type: тип брони
        """
        value_dice = StaticDice(side=defence)
        super().__init__(
            name=name,
            value_dice=value_dice,
            attribute=armor_type,
        )
