from typing import TYPE_CHECKING, Iterable

from src.utils.tools import info_context
from src.abstractions.perk import BasePerk
from src.utils.enums import PerkType, PerkStatus, PerkModifier, ActionKWArgs
from models.dice import DiceRoll, StaticDice, CritRoll, DifficultyDice
from src.utils.decorators import modify_perk_action
from src.utils.constants import WEAPON_ROLL_DIFFICULTY, SPELL_ROLL_DIFFICULTY
from src.utils.messages import (
    PERK_STATUS_DONE_MSG,
    PERK_STATUS_BLOCKED_MSG,
    PERK_HIT_CHANCE_MSG,
    PERK_HIT_VALUE_MSG,
    PERK_CRIT_CHANCE_MSG,
    PERK_CRIT_VALUE_MSG,
    PERK_ACTIVATE_MSG,
    PERK_BONUS_MSG,
    PERK_ATTACK_MSG,
    PERK_SHIELD_MSG,
    PERK_HEAL_MSG,
)

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.item import BaseItem
    from src.abstractions.unit import BaseUnit
    from src.abstractions.dice import BaseDice
    from utils.tools import BaseAttribute
    from utils.tools import F_spec


class Perk(BasePerk):
    """Модель способности"""

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
        self._difficulty = DiceRoll(dice=difficulty_dice)
        self._crit_roll = CritRoll()

    @property
    @modify_perk_action
    def item_value(self):
        """Значение предмета

        Returns:
            int: значение
        """
        return self._item.deal()

    @property
    @modify_perk_action
    def base_hit_chance(self) -> int:
        """Сложность удара

        Returns:
            int: значение
        """
        return self._difficulty.action()

    @property
    @modify_perk_action
    def base_crit_chance(self) -> int:
        """Сложность критического удара

        Returns:
            int: значение
        """
        return self._crit_roll.action()

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

    def base_hit_resistance(self, target: "BaseUnit") -> int:
        """Сопротивляемость удару
        Рассчитывается как:
            спасбросок цели

        Args:
            target: цель способности

        Returns:
            int: value
        """
        return target.save_throw(attribute=self._item.attribute)

    def base_crit_resistance(self, target: "BaseUnit") -> int:
        """Сопротивляемость критическому удару
        Рассчитывается как:
            сопротивляемость цели критическому удару
            + базовая сопротивляемость критическому удару

        Args:
            target: цель способности

        Returns:
            int: value
        """
        return target.crit_resistance + self._crit_roll.resistance

    def hit(self, target: "BaseUnit") -> bool:
        """Попадание
        Рассчитывается как:
            Шанс попадания > Защита цели

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        success = self.hit_chance()
        failure = self.base_hit_resistance(target=target)
        hit = success > failure
        hit_message = "Попадание!" if hit else "Промах!"
        info_context.update(
            value=PERK_HIT_CHANCE_MSG.format(
                success=success,
                failure=failure,
                hit=hit_message,
            )
        )
        return hit

    def crit(self, target: "BaseUnit") -> bool:
        """Критический удар
        Рассчитывается как:
            Шанс критического удара > Защита цели от критического удара

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        success = self.crit_chance()
        failure = self.base_crit_resistance(target=target)
        crit = success > failure
        crit_message = "Критический удар!" if crit else "Провал!"
        info_context.update(
            value=PERK_CRIT_CHANCE_MSG.format(
                success=success,
                failure=failure,
                crit=crit_message,
            )
        )
        return crit

    def hit_chance(self) -> int:
        """Шанс попадания
        Рассчитывается как:
            сложность удара
            + шанс попадания персонажа
            + мастерство владения предметом

        Returns:
            int: значение
        """
        return (
                self.base_hit_chance
                + self._person.hit_chance
                + self._person.mastery(attribute=self._item.attribute)
        )

    def crit_chance(self) -> int:
        """Шанс критического удара
        Рассчитывается как:
            сложность критического удара
            + шанс персонажа нанести критический удар

        Returns:
            int: значение
        """
        return self.base_crit_chance + self._person.crit_chance

    def hit_value(self) -> int:
        """Значение удара при попадании
        Рассчитывается как:
            значение предмета
            + мастерство владения предметом

        Returns:
            int: значение
        """
        value = self.item_value
        mastery = self._person.mastery(attribute=self._item.attribute)
        info_context.update(
            value=PERK_HIT_VALUE_MSG.format(value=value, mastery=mastery)
        )
        return value + mastery

    def crit_value(self) -> int:
        """Значение удара при критическом попадании
        Рассчитывается как:
            значение удара при попадании

        Returns:
            int: значение
        """
        value = self.item_value
        info_context.update(
            value=PERK_CRIT_VALUE_MSG.format(value=value)
        )
        return value

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """
        pass


class Melee(Perk):
    """Модель способности - атака в ближнем бою"""

    def __init__(
        self,
        name: str,
        title: str,
        weapon: "BaseItem",
        person: "BaseUnit",
        texture: "Texture",
        attribute: "BaseAttribute" = PerkType.melee.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = PerkModifier.standard.value,
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
        difficulty_dice = DifficultyDice(side=difficulty_value)
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

    def hit(self, target: "BaseUnit") -> bool:
        """Попадание
        Рассчитывается как:
            Шанс попадания > Защита цели
            Защита цели:
                сопротивляемость цели
                + спасбросок

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        success = self.hit_chance()
        failure = (
            target.defense + self.base_hit_resistance(target=target)
        )
        hit = success > failure
        hit_message = "Попадание!" if hit else "Промах!"
        info_context.update(
            value=PERK_HIT_CHANCE_MSG.format(
                success=success,
                failure=failure,
                hit=hit_message,
            )
        )
        return hit

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель
        Оружие ближнего боя должно пройти проверку на попадание, чтобы нанести урон
        При критическом ударе кубик урона кидается дважды
        При промахе (в т.ч. критическом) ничего не произойдет

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """

        # расчет урона
        value = 0
        if self.hit(target=target):
            value = self.hit_value()
            if self.crit(target=target):
                value += self.crit_value()

        """Учет бонусов
        Разница в силе доменов прибавляется к урону
        Здания дают бонус к защите противника
        Бонусы прибавляются только в случае попадания по противнику
        Урон не может быть ниже 0
        """
        if value:
            domain_bonus = kwargs.get(ActionKWArgs.domain_bonus.value, 0)
            building_bonus = kwargs.get(ActionKWArgs.building_bonus.value, 0)
            value = max(value + domain_bonus - building_bonus, 0)
            info_context.update(
                value=PERK_BONUS_MSG.format(
                    domain=domain_bonus,
                    building=building_bonus,
                    resist=0,
                )
            )

        if self._attribute == PerkType.heal.value:
            target.heal_self(value=value)
            info_context.update(
                value=PERK_HEAL_MSG.format(
                    result=value,
                    name=target.title,
                )
            )
        else:
            target.defend_self(damage=value)
            info_context.update(
                value=PERK_ATTACK_MSG.format(
                    result=value,
                    type=self._attribute,
                    name=target.title,
                )
            )


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
        modifier: "BaseAttribute" = PerkModifier.standard.value,
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

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель
        Щит используется для активации защитной стойки
        Добавляет дополнительную броню, но тратит ход

        Args:
            target: цель способности (сам персонаж)
            kwargs: дополнительные параметры (игнорируются для брони)
        """
        value = self.hit_value()
        target.shield_self(value=value)
        info_context.update(
            value=PERK_SHIELD_MSG.format(
                result=value,
                name=target.title,
            )
        )


class Elemental(Perk):
    """Модель способности - использование заклинания"""

    def __init__(
        self,
        name: str,
        title: str,
        spell: "BaseItem",
        person: "BaseUnit",
        texture: "Texture",
        attribute: "BaseAttribute" = PerkType.elemental.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = PerkModifier.standard.value,
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
        )

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель
        Заклинание должно пройти проверку на попадание, иначе нанесет половину урона
        Урон заклинания будет снижен защитой от магии цели (даже лечение), но не ниже 0
        При критическом ударе кубик урона кидается дважды и игнорируется защита от магии цели
        При критическом промахе урон будет нанесен самому персонажу.

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """

        """Учет бонусов
        Разница в силе доменов прибавляется к урону
        Здания дают бонус к защите противника
        """
        domain_bonus = kwargs.get(ActionKWArgs.domain_bonus.value, 0)
        building_bonus = kwargs.get(ActionKWArgs.building_bonus.value, 0)

        # расчет урона
        value = self.hit_value()
        resist = target.magic_resistance
        if self.hit(target=target):
            if self.crit(target=target):
                value += self.crit_value()
            value = max(
                value + domain_bonus - building_bonus - resist,
                0
            )
            info_context.update(
                value=PERK_BONUS_MSG.format(
                    domain=domain_bonus,
                    building=building_bonus,
                    resist=resist,
                )
            )
        else:
            if self.crit(target=target):
                target = self._person
                resist = target.magic_resistance
                value = max(
                    value + self.crit_value() + domain_bonus - resist,
                    0
                )
                # при критическом промахе исцеления - будет нанесен урон персонажу
                if self._attribute == PerkType.heal.value:
                    value *= -1
                info_context.update(
                    value=PERK_BONUS_MSG.format(
                        domain=domain_bonus,
                        building=0,
                        resist=resist,
                    )
                )
            else:
                value = max(
                    (value + domain_bonus - building_bonus - resist) // 2,
                    0
                )
                info_context.update(
                    value=PERK_BONUS_MSG.format(domain_bonus, building_bonus, resist)
                )

        if self._attribute == PerkType.heal.value:
            target.heal_self(value=value)
            info_context.update(
                value=PERK_HEAL_MSG.format(
                    result=value,
                    name=target.title,
                )
            )
        else:
            target.defend_self(damage=value)
            info_context.update(
                value=PERK_ATTACK_MSG.format(
                    result=value,
                    type=self._attribute,
                    name=target.title,
                )
            )


class PerkCombination(BasePerk):
    """Модель способности - комбинированная атака (оружие + заклинание)"""

    def __init__(
        self,
        name: str,
        main_perk: BasePerk,
        effects: Iterable[BasePerk],
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
        self._effects = effects

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
            # вызывается главная способность
            info_context.update(
                value=PERK_ACTIVATE_MSG.format(
                    name=self._main_perk._item.title,
                    target=target.title,
                    modifier=self._modifier,
                )
            )
            self._main_perk.change_modifier(value=self._modifier)
            self._main_perk.activate(target=target, **kwargs)
            # затем последовательно вызоваются все эффекты
            for effect in self._effects:
                info_context.update(
                    value=PERK_ACTIVATE_MSG.format(
                        name=effect._item.title,
                        target=target.title,
                        modifier=self._modifier,
                    )
                )
                effect.change_modifier(value=self._modifier)
                effect.activate(target=target, **kwargs)
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
