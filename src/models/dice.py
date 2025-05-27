from random import randint

from src.abstractions.dice import BasicDice, BasicRoll
from src.utils.constants import (
    BASE_CRITICAL_ROLL,
    CRITICAL_DICE_SIDE,
    CRITICAL_ROLL_RESISTANCE,
)


class Dice(BasicDice):
    """Модель многогранной кости"""

    def __init__(self, side: int = 4):
        """Инициализация кости

        Args:
            side: количество граней кости
        """
        super().__init__(side=side)

    def roll(self) -> int:
        """Результат броска кости
        Возвращается случайное значение от 1 до side (количество граней кости)

        Returns:
            int: значение
        """
        value = randint(a=1, b=self.side)
        return value


class DifficultyDice(BasicDice):
    """Модель многогранной кости на шанс попадания"""

    def __init__(self, side: int = 4):
        """Инициализация кости

        Args:
            side: количество граней кости
        """
        super().__init__(side=side)

    def roll(self) -> int:
        """Результат броска кости
        Возвращается случайное значение от 1 до side (количество граней кости)
        Если выпавшее значение равно side, то возвращается критическое значение
        Если выпавшее значение равно 1, то возвращается отрицательное критическое значение

        Returns:
            int: значение
        """
        value = randint(a=1, b=self.side)
        if value == self.side:
            value = BASE_CRITICAL_ROLL
        elif value == 1:
            value = -BASE_CRITICAL_ROLL
        return value


class StaticDice(BasicDice):
    """Модель статичной кости"""

    def __init__(self, side: int = 4):
        """Инициализация кости

        Args:
            side: значение кости
        """
        super().__init__(side=side)

    def roll(self) -> int:
        """Результат броска кости
        Возвращается side (значение кости)

        Returns:
            int: значение
        """
        return self.side


class DiceRoll(BasicRoll):
    """Модель броска кости"""

    def __init__(
        self,
        dice: BasicDice,
        times: int = 1,
    ):
        """Инициализация броска кости

        Args:
            dice: кость
            times: количество бросков
        """
        super().__init__(dice=dice)
        self.times = times

    def action(self) -> int:
        """Бросить кость
        Кость бросается times раз, результаты складываются

        Returns:
            int: результат
        """
        value = 0
        for time in range(1, self.times + 1):
            value += self.dice.roll()
        return value


class CritRoll(DiceRoll):
    """Модель броска кости на критический удар"""

    def __init__(self):
        dice = DifficultyDice(side=CRITICAL_DICE_SIDE)
        super().__init__(dice=dice)
        self.resistance = CRITICAL_ROLL_RESISTANCE
