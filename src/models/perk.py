from typing import TYPE_CHECKING, Iterable

from src.abstractions.perk import BasePerk
from src.utils.enums import PerkType, PerkStatus, PerkModifier, ActionKWArgs
from models.dice import DiceRoll, StaticDice, CritRoll, DifficultyDice
from src.utils.decorators import modify_perk_action
from src.utils.constants import WEAPON_ROLL_DIFFICULTY, SPELL_ROLL_DIFFICULTY

if TYPE_CHECKING:
    from src.abstractions.item import BaseItem
    from src.abstractions.unit import BaseUnit
    from src.abstractions.dice import BaseDice
    from src.abstractions.tools import BaseAttribute
    from src.abstractions.tools import F_spec


class Perk(BasePerk):
    """Модель способности"""

    def __init__(
        self,
        name: str,
        item: "BaseItem",
        attribute: "BaseAttribute",
        status: "BaseAttribute",
        modifier: "BaseAttribute",
        person: "BaseUnit",
        difficulty_dice: "BaseDice",
        texture_path: str = None,
    ):
        """Инициализация способности

        Args:
            name: имя
            item: предмет
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_dice: кость (сложность способности)
        """
        super().__init__(
            name=name,
            item=item,
            attribute=attribute,
            status=status,
            modifier=modifier,
            texture_path=texture_path,
        )
        self.person = person
        self.difficulty = DiceRoll(dice=difficulty_dice)
        self.crit_roll = CritRoll()

    @property
    @modify_perk_action
    def item_value(self):
        """Значение предмета

        Returns:
            int: значение
        """
        return self.item.deal()

    @property
    @modify_perk_action
    def base_hit_chance(self) -> int:
        """Сложность удара

        Returns:
            int: значение
        """
        return self.difficulty.action()

    @property
    @modify_perk_action
    def base_crit_chance(self) -> int:
        """Сложность критического удара

        Returns:
            int: значение
        """
        return self.crit_roll.action()

    def activate(self, target: "BaseUnit", **kwargs: "F_spec.kwargs"):
        """Активировать способность

         Args:
             target: цель способности
             kwargs: дополнительные параметры
         """
        if self.status != PerkStatus.active.value:
            return
        self.action(target=target, **kwargs)
        self.status = PerkStatus.done.value

    def change_attribute(self, value: "BaseAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        self.attribute = value

    def change_status(self, value: "BaseAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        self.status = value

    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        self.modifier = value

    def base_hit_resistance(self, target: "BaseUnit") -> int:
        """Сопротивляемость удару
        Рассчитывается как:
            спасбросок цели

        Args:
            target: цель способности

        Returns:
            int: value
        """
        return target.ability.save_throw(attribute=self.item.attribute)

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
        return target.crit_resistance + self.crit_roll.resistance

    def hit(self, target: "BaseUnit") -> bool:
        """Попадание
        Рассчитывается как:
            Шанс попадания > Защита цели

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        return self.hit_chance() > self.base_hit_resistance(target=target)

    def crit(self, target: "BaseUnit") -> bool:
        """Критический удар
        Рассчитывается как:
            Шанс критического удара > Защита цели от критического удара

        Args:
            target: цель способности

        Returns:
            bool: значение
        """
        return self.crit_chance() > self.base_crit_resistance(target=target)

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
                + self.person.hit_chance
                + self.person.ability.mastery(attribute=self.item.attribute)
        )

    def crit_chance(self) -> int:
        """Шанс критического удара
        Рассчитывается как:
            сложность критического удара
            + шанс персонажа нанести критический удар

        Returns:
            int: значение
        """
        return self.base_crit_chance + self.person.crit_chance

    def hit_value(self) -> int:
        """Значение удара при попадании
        Рассчитывается как:
            значение предмета
            + мастерство владения предметом

        Returns:
            int: значение
        """
        return self.item_value + self.person.ability.mastery(attribute=self.item.attribute)

    def crit_value(self) -> int:
        """Значение удара при критическом попадании
        Рассчитывается как:
            значение удара при попадании

        Returns:
            int: значение
        """
        return self.hit_value()

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
        weapon: "BaseItem",
        person: "BaseUnit",
        attribute: "BaseAttribute" = PerkType.melee.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = PerkModifier.standard.value,
        difficulty_value: int = WEAPON_ROLL_DIFFICULTY,
        texture_path: str = None,
    ):
        """Инициализация способности

        Args:
            name: имя
            weapon: оружие
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_value: сложность способности
        """
        difficulty_dice = DifficultyDice(side=difficulty_value)
        super().__init__(
            name=name,
            item=weapon,
            attribute=attribute,
            status=status,
            modifier=modifier,
            person=person,
            difficulty_dice=difficulty_dice,
            texture_path=texture_path,
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
        target_defence = (
            target.defense + self.base_hit_resistance(target=target)
        )
        return self.hit_chance() > target_defence

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель
        Оружие ближнего боя должно пройти проверку на попадание, чтобы нанести урон
        При критическом ударе кубик урона кидается дважды
        При промахе (в т.ч. критическом) ничего не произойдет
        При лечении урон будет отрицательным

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """
        # получим возможные бонусы
        domain_bonus = kwargs.get(ActionKWArgs.domain_bonus.value, 0)
        building_bonus = kwargs.get(ActionKWArgs.building_bonus.value, 0)

        hitted, critted = False, False

        # расчет урона
        value = 0
        if self.hit(target=target):
            hitted = True
            value = self.hit_value()
            if self.crit(target=target):
                critted = True
                value += self.crit_value()

        """Учет бонусов
        Разница в силе доменов прибавляется к урону
        Здания дают бонус к защите противника
        Бонусы прибавляются только в случае попадания по противнику
        Урон не может быть ниже 0
        """
        if value:
            value = max(value + domain_bonus - building_bonus, 0)

        # при лечении - урон отрицательный
        if self.attribute == PerkType.heal.value:
            value *= -1
        target.defend(damage=value)

        print(f"Персонаж {self.person.name} ударил противника {target.name} способностью {self.name}")
        print("Попал") if hitted else print("Промахнулся")
        if critted:
            print("Критическим")
        print(f"И нанес {value} урона")


class Armor(Perk):
    """Модель способности - использовать защитную стойку (требуется щит)"""

    def __init__(
        self,
        name: str,
        shield: "BaseItem",
        person: "BaseUnit",
        attribute: "BaseAttribute" = PerkType.shield.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = PerkModifier.standard.value,
        difficulty_value: int = 0,
        texture_path: str = None,
    ):
        """Инициализация способности

        Args:
            name: имя
            shield: щит
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_value: сложность способности
        """
        difficulty_dice = StaticDice(side=difficulty_value)
        super().__init__(
            name=name,
            item=shield,
            attribute=attribute,
            status=status,
            modifier=modifier,
            person=person,
            difficulty_dice=difficulty_dice,
            texture_path=texture_path,
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
        target.armor = value


class Elemental(Perk):
    """Модель способности - использование заклинания"""

    def __init__(
        self,
        name: str,
        spell: "BaseItem",
        person: "BaseUnit",
        attribute: "BaseAttribute" = PerkType.elemental.value,
        status: "BaseAttribute" = PerkStatus.active.value,
        modifier: "BaseAttribute" = PerkModifier.standard.value,
        difficulty_value: int = SPELL_ROLL_DIFFICULTY,
        texture_path: str = None,
    ):
        """Инициализация способности

        Args:
            name: имя
            spell: заклинание
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
            person: персонаж
            difficulty_value: сложность способности
        """
        difficulty_dice = StaticDice(side=difficulty_value)
        super().__init__(
            name=name,
            item=spell,
            attribute=attribute,
            status=status,
            modifier=modifier,
            person=person,
            difficulty_dice=difficulty_dice,
            texture_path=texture_path,
        )

    def action(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Воздействие на цель
        Заклинание должно пройти проверку на попадание, иначе нанесет половину урона
        Урон заклинания будет снижен защитой от магии цели (даже лечение), но не ниже 0
        При критическом ударе кубик урона кидается дважды и игнорируется защита от магии цели
        При критическом промахе урон будет нанесен самому персонажу.
        При лечении урон будет отрицательным

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """

        # получим возможные бонусы
        domain_bonus = kwargs.get(ActionKWArgs.domain_bonus.value, 0)
        building_bonus = kwargs.get(ActionKWArgs.building_bonus.value, 0)

        # расчет урона
        hitted, critted = False, False
        if self.hit(target=target):
            hitted = True
            value = max(self.hit_value() - target.magic_resistance, 0)
            if self.crit(target=target):
                critted = True
                value = self.hit_value() + self.crit_value()
        else:
            if self.crit(target=target):
                critted = True
                value = self.hit_value() + self.crit_value()
                if self.attribute == PerkType.heal.value:
                    value *= -1
                target = self.person
            else:
                value = max((self.hit_value() - target.magic_resistance) // 2, 0)

        """Учет бонусов
        Разница в силе доменов прибавляется к урону
        Здания дают бонус к защите противника
        Бонусы могут исказить заклинание и сделать урон отрицательным
        """
        value = value + domain_bonus - building_bonus

        # при лечении - урон отрицательный
        if self.attribute == PerkType.heal.value:
            value *= -1

        target.defend(damage=value)
        print(f"Персонаж {self.person.name} ударил противника {target.name} способностью {self.name}")
        print("Попал") if hitted else print("Промахнулся")
        if critted:
            print("Критическим")
        print(f"И нанес {value} урона")


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
            item=main_perk.item,
            attribute=main_perk.attribute,
            status=main_perk.status,
            modifier=main_perk.modifier,
            texture_path=main_perk.texture,
        )
        self.main_perk = main_perk
        self.effects = effects

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
        if self.status != PerkStatus.active.value:
            return
        # вызывается главная способность
        self.main_perk.change_modifier(value=self.modifier)
        self.main_perk.activate(target=target, **kwargs)
        # затем последовательно вызоваются все эффекты
        for effect in self.effects:
            effect.change_modifier(value=self.modifier)
            effect.activate(target=target, **kwargs)
        self.status = PerkStatus.done.value

    def change_attribute(self, value: "BaseAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        self.attribute = value

    def change_status(self, value: "BaseAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        self.status = value

    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        self.modifier = value
