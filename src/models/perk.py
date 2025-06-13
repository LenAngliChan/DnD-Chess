from typing import TYPE_CHECKING, Iterable, Union

from src.utils.tools import info_context
from src.abstractions.perk import BasePerk
from src.utils.enums import PerkType, PerkStatus, RollModifier, ActionKWArgs
from models.dice import (
    StaticDice,
    CritRoll,
    Dice,
    DifficultyRoll,
)
from src.utils.constants import (
    WEAPON_ROLL_DIFFICULTY,
    SPELL_ROLL_DIFFICULTY,
    SPELL_ROLL_RESISTANCE,
)
from src.utils.messages import (
    PERK_STATUS_DONE_MSG,
    PERK_STATUS_BLOCKED_MSG,
    PERK_ACTIVATE_MSG,
    PERK_HIT_CHANCE_MSG,
    PERK_CRIT_CHANCE_MSG,
)

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.item import BaseItem
    from src.abstractions.unit import BaseUnit
    from src.abstractions.dice import BaseDice
    from utils.tools import BaseAttribute
    from utils.tools import F_spec


class Perk(BasePerk):
    """Модель способности
    Способность отвечает за броски попадания и критического удара
    Также способность вызывает определенный эффект, связанный с предметом
    """

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
        attribute: "BaseAttribute",
        status: "BaseAttribute",
        modifier: "BaseAttribute",
        person: "BaseUnit",
        difficulty_dice: "BaseDice",
        texture: "Texture",
        resistance_dice: Union["BaseDice", int] = 0,
    ):
        """Инициализация способности

        Args:
            name: имя способности
            title: имя способности для отображения на gui
            item: предмет
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_dice: кость (сложность способности)
            texture: иконка способности
            resistance_dice: кость/значение (сопротивление способности)
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
            attribute=attribute,
            status=status,
            modifier=modifier,
            texture=texture,
        )
        self._person = person
        self._difficulty = DifficultyRoll(
            dice=difficulty_dice,
            modifier=modifier,
            resistance=resistance_dice,
        )
        self._crit_roll = CritRoll(modifier=modifier)

    @property
    def base_hit_chance(self) -> int:
        """Базовый шанс попадания
        Рассчитывается как:
            шанс попадания персонажа
            + мастерство владения предметом

        Returns:
            int: значение
        """

        return (
                self._person.hit_chance
                + self._person.mastery(attribute=self._item.attribute)
        )

    def base_hit_resistance(self, target: "BaseUnit") -> int:
        """Базовая сопротивляемость удару
        Рассчитывается как:
            спасбросок цели

        Args:
            target: цель способности

        Returns:
            int: value
        """
        return target.save_throw(attribute=self._item.attribute)

    def hit(self, target: "BaseUnit") -> bool:
        """Попадание
        Рассчитывается как:
            Шанс попадания > Защита цели

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        bonus = self.base_hit_chance
        penalty = self.base_hit_resistance(target=target)
        info_context.update(value=PERK_HIT_CHANCE_MSG)
        return self._difficulty.action(
            bonus=bonus,
            penalty=penalty,
        )

    @property
    def base_crit_chance(self) -> int:
        """Базовый шанс критического удара
        Рассчитывается как:
            шанс персонажа нанести критический удар

        Returns:
            int: значение
        """
        return self._person.crit_chance

    @staticmethod
    def base_crit_resistance(target: "BaseUnit") -> int:
        """Базовая сопротивляемость критическому удару
        Рассчитывается как:
            сопротивляемость цели критическому удару

        Args:
            target: цель способности

        Returns:
            int: value
        """
        return target.crit_resistance

    def crit(self, target: "BaseUnit") -> bool:
        """Критический удар
        Рассчитывается как:
            Шанс критического удара > Защита цели от критического удара

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        bonus = self.base_crit_chance
        penalty = self.base_crit_resistance(target=target)
        info_context.update(value=PERK_CRIT_CHANCE_MSG)
        return self._crit_roll.action(
            bonus=bonus,
            penalty=penalty,
        )

    def activate(self, target: "BaseUnit", **kwargs: "F_spec.kwargs"):
        """Активировать способность

         Args:
             target: цель способности
             kwargs: дополнительные параметры
         """
        if self._status == PerkStatus.done.value:
            info_context.update(
                value=PERK_STATUS_DONE_MSG.format(name=self._item.title)
            )
            return
        elif self._status == PerkStatus.blocked.value:
            info_context.update(
                value=PERK_STATUS_BLOCKED_MSG.format(name=self._item.title)
            )
            return
        else:
            info_context.update(
                value=PERK_ACTIVATE_MSG.format(
                    name=self._item.title,
                    target=target.title,
                    modifier=self._modifier,
                )
            )
            self.action(target=target, **kwargs)
            self._status = PerkStatus.done.value

    def change_attribute(self, value: "BaseAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        self._attribute = value

    def change_status(self, value: "BaseAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        self._status = value

    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        self._modifier = value
        self._item.change_modifier(value=value)
        self._difficulty.modifier = value
        self._crit_roll.modifier = value

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """
        hit = self.hit(target=target)
        crit = self.crit(target=target)
        mastery = self._person.mastery(attribute=self._item.attribute)
        self._item.charge(
            target=target,
            hit=hit,
            crit=crit,
            mastery=mastery,
            **kwargs,
        )


class Melee(Perk):
    """Модель способности - физическая атака"""

    def __init__(
        self,
        name: str,
        title: str,
        weapon: "BaseItem",
        person: "BaseUnit",
        texture: "Texture",
        attribute: "BaseAttribute" = PerkType.melee.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = RollModifier.standard.value,
        difficulty_value: int = WEAPON_ROLL_DIFFICULTY,
    ):
        """Инициализация способности

        Args:
            name: имя способности
            title: имя способности для отображения на gui
            weapon: оружие
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_value: сложность способности
            texture: иконка способности
        """
        difficulty_dice = Dice(side=difficulty_value)
        super().__init__(
            name=name,
            title=title,
            item=weapon,
            attribute=attribute,
            status=status,
            modifier=modifier,
            person=person,
            difficulty_dice=difficulty_dice,
            texture=texture,
        )

    def base_hit_resistance(self, target: "BaseUnit") -> int:
        """Базовая сопротивляемость удару
        Рассчитывается как:
            сопротивляемость цели
            + спасбросок цели

        Args:
            target: цель способности

        Returns:
            int: value
        """
        return target.defense + target.save_throw(attribute=self._item.attribute)


class Armor(Perk):
    """Модель способности - использовать защитную стойку (требуется щит)"""

    def __init__(
        self,
        name: str,
        title: str,
        shield: "BaseItem",
        person: "BaseUnit",
        texture: "Texture",
        attribute: "BaseAttribute" = PerkType.shield.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = RollModifier.standard.value,
        difficulty_value: int = 0,
    ):
        """Инициализация способности

        Args:
            name: имя способности
            title: имя способности для отображения на gui
            shield: щит
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_value: сложность способности
            texture: иконка способности
        """
        difficulty_dice = StaticDice(side=difficulty_value)
        super().__init__(
            name=name,
            title=title,
            item=shield,
            attribute=attribute,
            status=status,
            modifier=modifier,
            person=person,
            difficulty_dice=difficulty_dice,
            texture=texture,
        )


class Magic(Perk):
    """Модель способности - использование магии"""

    def __init__(
        self,
        name: str,
        title: str,
        spell: "BaseItem",
        person: "BaseUnit",
        texture: "Texture",
        attribute: "BaseAttribute" = PerkType.elemental.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = RollModifier.standard.value,
        difficulty_value: int = SPELL_ROLL_DIFFICULTY,
    ):
        """Инициализация способности

        Args:
            name: имя способности
            title: имя способности для отображения на gui
            spell: заклинание
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_value: сложность способности
            texture: иконка способности
        """
        difficulty_dice = StaticDice(side=difficulty_value)
        resistance_dice = Dice(side=SPELL_ROLL_RESISTANCE)
        super().__init__(
            name=name,
            title=title,
            item=spell,
            attribute=attribute,
            status=status,
            modifier=modifier,
            person=person,
            difficulty_dice=difficulty_dice,
            texture=texture,
            resistance_dice=resistance_dice,
        )


class PerkCombination(BasePerk):
    """Модель способности - комбинированная атака (оружие + заклинание)"""

    def __init__(
        self,
        name: str,
        main_perk: BasePerk,
        other_perks: Iterable[BasePerk],
    ):
        """Инициализация способности

        Args:
            name: имя
            main_perk: главная способность
            effects: список эффектов (дополнительных способностей)
        """
        super().__init__(
            name=name,
            title=main_perk._title,
            item=main_perk._item,
            attribute=main_perk._attribute,
            status=main_perk._status,
            modifier=main_perk._modifier,
            texture=main_perk._texture,
        )
        self._main_perk = main_perk
        self._other_perks = other_perks

    def activate(self, target: "BaseUnit", **kwargs: "F_spec.kwargs"):
        """Воздействие на цель
        Заклинание должно пройти проверку на попадание, иначе нанесет половину урона
        При критическом ударе кубик урона кидается дважды
        При критическом промахе урон будет нанесен самому персонажу.
        При лечении урон будет отрицательным

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """

        # вызывается главная способность
        self._main_perk.activate(target=target, **kwargs)

        # затем последовательно вызоваются все эффекты
        for next_perk in self._other_perks:
            next_perk.activate(target=target, **kwargs)

        self.change_status(value=PerkStatus.done.value)

    def change_attribute(self, value: "BaseAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        self._attribute = value
        self._main_perk.change_attribute(value=value)
        for next_perk in self._other_perks:
            next_perk.change_attribute(value=value)

    def change_status(self, value: "BaseAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        self._status = value
        self._main_perk.change_status(value=value)
        for next_perk in self._other_perks:
            next_perk.change_status(value=value)

    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        self._modifier = value
        self._main_perk.change_modifier(value=value)
        for next_perk in self._other_perks:
            next_perk.change_modifier(value=value)
