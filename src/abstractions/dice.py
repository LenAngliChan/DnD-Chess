from abc import ABC, abstractmethod


class BaseDice(ABC):
    """Абстрактная модель кости"""

    def __init__(self, side: int):
        """Инициализация кости

        Args:
            side: количество граней кости
        """
        self._side = side

    @abstractmethod
    def roll(self) -> int:
        """Результат броска кости

        Returns:
            int: значение
        """
        pass


class BaseRoll(ABC):
    """Абстрактная модель броска кости"""

    def __init__(self, dice: BaseDice):
        """Инициализация броска кости

        Args:
            dice: кость
        """
        self._dice = dice

    @abstractmethod
    def action(self) -> int:
        """Бросить кость

        Returns:
            int: результат
        """
        pass
