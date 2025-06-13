from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.utils.tools import BaseAttribute
    from src.utils.tools import F_spec


class BaseDice(ABC):
    """Абстрактная модель кости"""

    def __init__(
        self,
        side: int,
        lower: int = 0,
        higher: int = 0,
    ):
        """Инициализация кости

        Args:
            side: количество граней кости
            lower: минимальное значение
            higher: максимальное значение
        """
        self._side = side
        self._lower = lower
        self._higher = higher

    @abstractmethod
    def roll(self) -> int:
        """Результат броска кости

        Returns:
            int: значение
        """
        pass

    @property
    def lower(self) -> int:
        """Минимальное значение"""
        return self._lower

    @property
    def higher(self) -> int:
        """Максимальное значение"""
        return self._higher


class BaseRoll(ABC):
    """Абстрактная модель броска кости"""

    def __init__(
        self,
        dice: BaseDice,
        modifier: "BaseAttribute",
        resistance: BaseDice | int = 0,
    ):
        """Инициализация броска кости

        Args:
            dice: кость
            modifier: модификатор броска
            resistance: базовый шанс на провал (для бросков на попадание)
        """
        self._dice = dice
        self._modifier = modifier
        self._resistance = resistance

    @abstractmethod
    def action(self, **kwargs: "F_spec.kwargs") -> int | bool:
        """Бросить кость

        Returns:
            int: результат
        """
        pass

    @property
    def modifier(self) -> "BaseAttribute":
        return self._modifier

    @modifier.setter
    def modifier(self, value: "BaseAttribute") -> None:
        self._modifier = value

    @property
    def resistance(self) -> int:
        if isinstance(self._resistance, BaseDice):
            return self._resistance.roll()
        else:
            return self._resistance
