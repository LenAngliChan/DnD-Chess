from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.utils.descriptions import ITEM_LONG_DESC

if TYPE_CHECKING:
    from src.abstractions.dice import BaseRoll
    from utils.tools import BaseAttribute


class BaseItem(ABC):
    """Абстрактная модель предмета"""

    def __init__(
        self,
        name: str,
        title: str,
        value: "BaseRoll",
        attribute: "BaseAttribute",
    ):
        """Инициализация предмета

        Args:
            name: имя предмета
            title: имя предмета для отображения на gui
            value: значение предмета
            attribute: тип предмета
        """
        self._name = name
        self._title = title
        self._value = value
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

    @abstractmethod
    def deal(self) -> int:
        """Выполнить действие предмета

        Returns:
            int: значение
        """
        pass
