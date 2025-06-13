from random import randint
from typing import TYPE_CHECKING

from src.abstractions.dice import BaseDice, BaseRoll
from src.utils.enums import RollModifier
from src.utils.decorators import modify_roll
from src.utils.tools import info_context
from src.utils.constants import (
    CRITICAL_DICE_SIDE,
    CRITICAL_ROLL_RESISTANCE,
)
from src.utils.messages import (
    DICE_ROLL_MSG,
    CHECK_ROLL_MSG,
    CRIT_SUCCESS_MSG,
    CRIT_FAILURE_MSG,
)

if TYPE_CHECKING:
    from src.utils.tools import BaseAttribute


class Dice(BaseDice):
    """Модель многогранной кости"""

    def __init__(self, side: int = 4):
        """Инициализация кости

        Args:
            side: количество граней кости
        """
        super().__init__(
            side=side,
            lower=1,
            higher=side,
        )

    def roll(self) -> int:
        """Результат броска кости
        Возвращается случайное значение от 1 до side (количество граней кости)

        Returns:
            int: значение
        """
        value = randint(a=1, b=self._side)
        return value


class StaticDice(BaseDice):
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
        return self._side


class DiceRoll(BaseRoll):
    """Модель броска кости"""

    def __init__(
        self,
        dice: BaseDice,
        modifier: "BaseAttribute" = RollModifier.standard.value,
        times: int = 1,
    ):
        """Инициализация броска кости

        Args:
            dice: кость
            modifier: модификатор броска
            times: количество бросков
        """
        super().__init__(
            dice=dice,
            modifier=modifier,
        )
        self._times = times

    def action(self, bonus: int = 0, penalty: int = 0) -> int:
        """Бросить кость

        Args:
            bonus: бонус (только для погашения штрафа)
            penalty: штраф (уменьшает конечное значение)

        Returns:
            int: результат
        """
        value = self._action()
        real_bonus = max(bonus, 0)
        real_penalty = min(real_bonus - penalty, 0)
        info_context.update(
            value=DICE_ROLL_MSG.format(
                value=value,
                penalty=real_penalty,
            )
        )
        return value + real_penalty

    @modify_roll
    def _action(self) -> int:
        """Бросить кость
        Кость бросается times раз, результаты складываются

        Returns:
            int: результат
        """
        value = 0
        for time in range(1, self._times + 1):
            value += self._dice.roll()
        return value


class DifficultyRoll(BaseRoll):
    """Модель броска многогранной кости на шанс попадания"""

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
        """
        super().__init__(
            dice=dice,
            modifier=modifier,
            resistance=resistance,
        )

    def action(self, bonus: int = 0, penalty: int = 0) -> bool:
        """Бросить кость на попадание
        Кость бросается 1 раз, складываются бонусы
        Сравнивается со значением, препятствующим попаданию
        При критическом успехе автоматически возвращается ДА
        При критическом провале автоматически возвращается НЕТ

        Args:
            bonus: бонус (увеличивает шанс попадания)
            penalty: штраф (уменьшает шанс попадания)

        Returns:
            bool: результат (да/нет)
        """
        value = self._action()
        success = value + bonus
        failure = penalty + self.resistance
        if value == self._dice.lower:
            info_context.update(
                value=CRIT_FAILURE_MSG.format(value=value)
            )
            return False
        elif value == self._dice.higher:
            info_context.update(
                value=CRIT_SUCCESS_MSG.format(value=value)
            )
            return True
        else:
            result = success >= failure
            info_context.update(
                value=CHECK_ROLL_MSG.format(
                    success=success,
                    failure=failure,
                    result="Успех!" if result else "Провал!"
                )
            )
            return result

    @modify_roll
    def _action(self) -> int:
        """Бросить кость
        Кость бросается 1 раз

        Returns:
            int: результат
        """
        value = self._dice.roll()
        return value


class CritRoll(DifficultyRoll):
    """Модель броска кости на критический удар"""

    def __init__(
        self,
        modifier: "BaseAttribute",
    ):
        """Инициализация броска кости

        Args:
            modifier: модификатор броска
        """
        dice = Dice(side=CRITICAL_DICE_SIDE)
        super().__init__(
            dice=dice,
            modifier=modifier,
            resistance=CRITICAL_ROLL_RESISTANCE,
        )

