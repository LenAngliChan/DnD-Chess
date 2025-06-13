from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.utils.descriptions import ITEM_LONG_DESC

if TYPE_CHECKING:
    from src.abstractions.effect import BaseEffect
    from src.abstractions.dice import BaseRoll
    from utils.tools import BaseAttribute
    from src.abstractions.unit import BaseUnit
    from src.utils.tools import F_spec


class BaseItem(ABC):
    """Абстрактная модель предмета"""

    def __init__(
        self,
        name: str,
        title: str,
        value: "BaseRoll",
        effect: "BaseEffect",
        attribute: "BaseAttribute",
    ):
        """Инициализация предмета

        Args:
            name: имя предмета
            title: имя предмета для отображения на gui
            value: значение предмета
            effect: эффект предмета
            attribute: тип предмета
        """
        self._name = name
        self._title = title
        self._value = value
        self._effect = effect
        self._attribute = attribute

    def __str__(self) -> str:
        """Описание предмета"""
        return ITEM_LONG_DESC.format(title=self._title, attribute=self._attribute)

    @property
    def desc(self) -> str:
        """Краткое описание предмета"""
        return self._title

    @property
    def title(self) -> str:
        """Наименование"""
        return self._title

    @property
    def attribute(self) -> "BaseAttribute":
        """Атрибут"""
        return self._attribute

    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор урона предмета

        Args:
            value: значение
        """
        self._value.modifier = value

    def charge(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Активировать предмет (выполнить эффект предмета)"""
        self._effect.apply(
            target=target,
            hit=hit,
            crit=crit,
            **kwargs,
        )

    @abstractmethod
    def deal(self, **kwargs: "F_spec.kwargs") -> int:
        """Выполнить действие предмета

        Returns:
            int: значение
        """
        pass
