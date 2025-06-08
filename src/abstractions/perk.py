from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.utils.descriptions import PERK_LONG_DESC

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.item import BaseItem
    from utils.tools import BaseAttribute
    from src.abstractions.unit import BaseUnit
    from utils.tools import F_spec


class BasePerk(ABC):
    """Абстрактная модель способности"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
        attribute: "BaseAttribute",
        status: "BaseAttribute",
        modifier: "BaseAttribute",
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
            texture: иконка способности
        """
        self._name = name
        self._title = title
        self._item = item
        self._attribute = attribute
        self._status = status
        self._modifier = modifier
        self._texture = texture

    def __str__(self) -> str:
        """Полное описание способности"""
        return PERK_LONG_DESC.format(
            title=self._title,
            item=self._item.title,
            type=self._item.attribute,
        )

    @property
    def desc(self) -> str:
        """Краткое описание способности"""
        return self._title

    @property
    def name(self) -> str:
        """Имя способности"""
        return self._name

    @property
    def title(self) -> str:
        """Наименование"""
        return self._title

    @property
    def texture(self) -> "Texture":
        """Текстуры"""
        return self._texture

    @property
    def attribute(self) -> "BaseAttribute":
        """Атрибут"""
        return self._attribute

    @property
    def modifier(self) -> "BaseAttribute":
        return self._modifier

    @property
    def status(self) -> "BaseAttribute":
        return self._status

    @abstractmethod
    def activate(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Активировать способность

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """
        pass

    @abstractmethod
    def change_attribute(self, value: "BaseAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def change_status(self, value: "BaseAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        pass
