from typing import TYPE_CHECKING

from src.abstractions.item import BaseItem
from src.models.dice import DiceRoll, Dice, StaticDice
from src.utils.enums import MagicType, WeaponType, ArmorType, RollModifier

if TYPE_CHECKING:
    from src.abstractions.effect import BaseEffect
    from utils.tools import BaseAttribute
    from src.abstractions.dice import BaseDice
    from src.utils.tools import F_spec


class Item(BaseItem):
    """Модель предмета"""

    def __init__(
        self,
        name: str,
        title: str,
        value_dice: "BaseDice",
        effect: "BaseEffect",
        attribute: "BaseAttribute",
        modifier: "BaseAttribute" = RollModifier.standard.value,
        radius: int = 1,
        times: int = 1,
    ):
        """Инициализация предмета

        Args:
            name: имя предмета
            title: имя предмета для отображения на gui
            value_dice: кость (значение предмета)
            effect: эффект предмета
            attribute: тип предмета
            modifier: модификатор предмета
            radius: радиус действия
            times: количество бросков кости
        """
        value = DiceRoll(
            dice=value_dice,
            modifier=modifier,
            times=times,
        )
        super().__init__(
            name=name,
            title=title,
            value=value,
            effect=effect,
            attribute=attribute,
            radius=radius,
        )

    def deal(self, **kwargs: "F_spec.kwargs") -> int:
        """Выполнить действие предмета
        Делается бросок кости предмета

        Returns:
            int: значение
        """
        return self._value.action(**kwargs)


class Weapon(Item):
    """Модель оружия"""

    def __init__(
        self,
        name: str,
        title: str,
        effect: "BaseEffect",
        damage: int = 4,
        weapon_type: "BaseAttribute" = WeaponType.medium.value,
        radius: int = 1,
        times: int = 1,
    ):
        """Инициализация оружия

        Args:
            name: имя оружия
            title: имя предмета для отображения на gui
            effect: эффект предмета
            damage: урон оружия
            weapon_type: тип оружия
            radius: радиус действия
            times: количество бросков кости
        """
        value_dice = Dice(side=damage)
        super().__init__(
            name=name,
            title=title,
            value_dice=value_dice,
            effect=effect,
            attribute=weapon_type,
            radius=radius,
            times=times,
        )


class Spell(Item):
    """Модель заклинания"""

    def __init__(
        self,
        name: str,
        title: str,
        effect: "BaseEffect",
        damage: int = 4,
        magic_type: "BaseAttribute" = MagicType.fire.value,
        radius: int = 1,
        times: int = 1,
    ):
        """Инициализация заклинания

        Args:
            name: имя заклинания
            title: имя предмета для отображения на gui
            effect: эффект предмета
            damage: урон заклинания
            magic_type: тип заклинания
            radius: радиус действия
            times: количество бросков кости
        """
        value_dice = Dice(side=damage)
        super().__init__(
            name=name,
            title=title,
            value_dice=value_dice,
            effect=effect,
            attribute=magic_type,
            radius=radius,
            times=times,
        )


class Armor(Item):
    """Модель брони"""

    def __init__(
        self,
        name: str,
        title: str,
        effect: "BaseEffect",
        defence: int = 4,
        radius: int = 1,
        armor_type: "BaseAttribute" = ArmorType.medium_shield.value,
    ):
        """Инициализация брони

        Args:
            name: имя брони
            title: имя предмета для отображения на gui
            effect: эффект предмета
            defence: защита брони
            radius: радиус действия
            armor_type: тип брони
        """
        value_dice = StaticDice(side=defence)
        super().__init__(
            name=name,
            title=title,
            value_dice=value_dice,
            effect=effect,
            attribute=armor_type,
            radius=radius,
        )
