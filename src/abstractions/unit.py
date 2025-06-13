from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.utils.constants import BASE_CHARACTERISTIC
from src.utils.descriptions import ABILITY_LONG_DESC, UNIT_LONG_DESC

if TYPE_CHECKING:
    from src.abstractions.item import BaseAttribute
    from src.utils.characters import Characteristic
    from src.abstractions.perk import BasePerk
    from collections import UserDict


class BaseAbility(ABC):
    """Абстрактная модель характеристик персонажа"""

    def __init__(
        self,
        characteristic: "Characteristic",
    ):
        """Инициализация характеристик персонажа

        Args:
            characteristic: базовые характиристики персонажа
        """
        self._base_characteristic = BASE_CHARACTERISTIC
        self._strength = characteristic.strength
        self._constitution = characteristic.constitution
        self._dexterity = characteristic.dexterity
        self._intelligence = characteristic.intelligence
        self._wisdom = characteristic.wisdom
        self._charisma = characteristic.charisma
        self._base_hit_points = characteristic.base_hit_points
        self._base_hp_coefficient = characteristic.base_hp_coefficient
        self._base_hit_chance = characteristic.base_hit_chance
        self._base_defence = characteristic.base_defence
        self._base_crit_chance = characteristic.base_crit_chance
        self._base_crit_resistance = characteristic.base_crit_resistance
        self._base_magic_resistance = characteristic.base_magic_resistance

    def __str__(self) -> str:
        """Полное описание характеристик"""
        return ABILITY_LONG_DESC.format(
            strength=self._strength,
            constitution=self._constitution,
            dexterity=self._dexterity,
            intelligence=self._intelligence,
            wisdom=self._wisdom,
            charisma=self._charisma,
        )

    @property
    def base_hit_points(self) -> int:
        """Базовые очки здоровья"""
        return self._base_hit_points

    @property
    def base_hp_coefficient(self) -> int:
        """Базовый коэффициент здоровья"""
        return self._base_hp_coefficient

    @property
    def base_hit_chance(self) -> int:
        """Базовый шанс попадания"""
        return self._base_hit_chance

    @property
    def base_defence(self) -> int:
        """Базовый шанс уклонения"""
        return self._base_defence

    @property
    def base_crit_chance(self) -> int:
        """Базовый шанс критического удара"""
        return self._base_crit_chance

    @property
    def base_crit_resistance(self) -> int:
        """Базовое сопротивление критическому удару"""
        return self._base_crit_resistance

    @property
    def base_magic_resistance(self) -> int:
        """Базовое магическое сопротивление"""
        return self._base_magic_resistance

    @abstractmethod
    def save_throw(self, attribute: "BaseAttribute") -> int:
        """Спасбросок

        Args:
            attribute: тип спасброска

        Returns:
            int: значение спасброска
        """
        pass

    @abstractmethod
    def mastery(self, attribute: "BaseAttribute" = None) -> int:
        """Мастерство

        Args:
            attribute: тип проверки на мастерство

        Returns:
            int: значение мастерства
        """
        pass


class BaseUnit(ABC):
    """Абстрактная модель персонажа"""

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        ability: BaseAbility,
        perks: "UserDict[str, BasePerk]" = None,
        level: int = 1,
    ):
        """Инициализация персонажа

        Args:
            name: имя персонажа
            title: имя персонажа для отображения на gui
            description: описание персонажа
            ability: характеристики персонажа
            perks: список способностей
            level: уровень персонажа
        """
        self._name = name
        self._title = title
        self._description = description
        self._ability = ability
        self._perks = perks
        self._level = level
        self._current_hp = 0 + self.hit_points
        self._armor = 0

    def __str__(self) -> str:
        """Полное описание персонажа"""
        return UNIT_LONG_DESC.format(
            title=self.title,
            description=self._description,
            ability=self._ability,
            current_hp=self._current_hp,
            defence=self.defense,
            perks_title=self.perks_title,
        )

    @property
    def desc(self) -> str:
        """Краткое описание персонажа"""
        return f"Персонаж {self._title} {self._level} уровня"

    @property
    def name(self) -> str:
        """Имя персонажа"""
        return self._name

    @property
    def title(self) -> str:
        """Наименование"""
        return self._title

    @property
    def hp_percent(self) -> float:
        """Остаток здоровья"""
        return self._current_hp / self.hit_points

    @property
    def is_dead(self) -> bool:
        """Статус персонажа"""
        return self._current_hp == 0

    @property
    def perks_title(self) -> str:
        """Описание способностей"""
        perks_desc = [
            f"{perk}"
            for perk in self._perks.values()
        ]
        return "\n".join(perks_desc)

    def save_throw(self, attribute: "BaseAttribute") -> int:
        """Спасбросок

        Args:
            attribute: тип спасброска

        Returns:
            int: значение спасброска
        """
        return self._ability.save_throw(attribute=attribute)

    def mastery(self, attribute: "BaseAttribute" = None) -> int:
        """Мастерство

        Args:
            attribute: тип проверки на мастерство

        Returns:
            int: значение мастерства
        """
        return self._ability.mastery(attribute=attribute)

    def get_perks(self) -> "UserDict[str, BasePerk]":
        return self._perks

    @property
    @abstractmethod
    def hit_chance(self) -> int:
        """Шанс попадания персонажа

        Returns:
            int: значение
        """
        pass

    @property
    @abstractmethod
    def defense(self) -> int:
        """Защита персонажа (шанс уклонения)

        Returns:
            int: значение
        """
        pass

    @property
    @abstractmethod
    def crit_chance(self) -> int:
        """Шанс критического удара персонажа

        Returns:
            int: значение
        """
        pass

    @property
    @abstractmethod
    def crit_resistance(self) -> int:
        """Защита от критического удара персонажа (шанс избежать крит. удара)

        Returns:
            int: значение
        """
        pass

    @property
    @abstractmethod
    def magic_resistance(self) -> int:
        """Защита от магии персонажа (сопротивление маг. урону)

        Returns:
            int: значение
        """
        pass

    @property
    @abstractmethod
    def hit_points(self) -> int:
        """Очки здоровья персонажа

        Returns:
            int: значение
        """
        pass

    @abstractmethod
    def level_up(self) -> None:
        """Повысить уровень персонажа (на 1 пункт)"""
        pass

    @abstractmethod
    def defend_self(self, damage: int = 0) -> None:
        """Действие - защищаться (получить урон от другого персонажа)

        Args:
            damage: урон
        """
        pass

    @abstractmethod
    def shield_self(self, value: int = 0) -> None:
        """Действие - укрыться щитом

        Args:
            value: значение брони
        """
        pass

    @abstractmethod
    def heal_self(self, value: int = 0) -> None:
        """Действие - исцелиться

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def end_circle(self) -> None:
        """Завершить ход"""
        pass
