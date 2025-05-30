from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.utils.constants import BASE_CHARACTERISTIC

if TYPE_CHECKING:
    from src.abstractions.item import BasicAttribute
    from src.utils.characters import Character
    from src.abstractions.perk import BasicPerk
    from collections import UserDict


class BasicAbility(ABC):
    """Абстрактная модель характеристик персонажа"""

    def __init__(
        self,
        character: "Character",
    ):
        """Инициализация характеристик персонажа

        Args:
            character: базовые характиристики персонажа
        """
        self.base_characteristic = BASE_CHARACTERISTIC
        self.strength = character.strength
        self.constitution = character.constitution
        self.dexterity = character.dexterity
        self.intelligence = character.intelligence
        self.wisdom = character.wisdom
        self.charisma = character.charisma
        self.base_hit_points = character.base_hit_points
        self.base_hp_coefficient = character.base_hp_coefficient
        self.base_hit_chance = character.base_hit_chance
        self.base_defence = character.base_defence
        self.base_crit_chance = character.base_hit_chance
        self.base_crit_resistance = character.base_crit_resistance
        self.base_magic_resistance = character.base_magic_resistance

    @abstractmethod
    def save_throw(self, attribute: "BasicAttribute") -> int:
        """Спасбросок

        Args:
            attribute: тип спасброска

        Returns:
            int: значение спасброска
        """
        pass

    @abstractmethod
    def mastery(self, attribute: "BasicAttribute" = None) -> int:
        """Мастерство

        Args:
            attribute: тип проверки на мастерство

        Returns:
            int: значение мастерства
        """
        pass


class BasicUnit(ABC):
    """Абстрактная модель персонажа"""

    def __init__(
        self,
        name: str,
        ability: BasicAbility,
        perks: "UserDict[str, BasicPerk]" = None,
        level: int = 1,
    ):
        """Инициализация персонажа

        Args:
            name: имя персонажа
            ability: характеристики персонажа
            perks: список способностей
            level: уровень персонажа
        """
        self.name = name
        self.ability = ability
        self.perks = perks
        self.level = level
        self.current_hp = 0 + self.hit_points
        self.armor = 0

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
    def defend(self, damage: int = 0) -> None:
        """Действие - защищаться (получить урон от другого персонажа)

        Args:
            damage: урон
        """
        pass

    @abstractmethod
    def end_circle(self) -> None:
        """Завершить ход"""
        pass
