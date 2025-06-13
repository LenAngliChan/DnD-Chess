from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

from src.utils.descriptions import ACTION_SHORT_DESC

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.perk import BasePerk
    from utils.tools import BaseAttribute
    from src.abstractions.figure import BaseFigure
    from src.abstractions.cell import BaseCell


class BaseAction(ABC):
    """Абстрактная модель действия"""

    def __init__(
        self,
        name: str,
        attribute: "BaseAttribute",
        texture: "Texture",
        figure: "BaseFigure" = None,
        perk: "BasePerk" = None,
    ):
        """Инициализация действия

        Args:
            name: имя действия
            attribute: тип действия
            figure: фигура
            perk: способность
        """
        self._name = name
        self._attribute = attribute
        self._figure = figure
        self._perk = perk
        self._texture = texture
        self._radius = perk.radius if perk else 1

    def __str__(self) -> str:
        """Полное описание действия"""
        return self._perk.desc

    @property
    def desc(self) -> str:
        """Краткое описание действия"""
        perk_name = self._perk.title if self._perk else ""
        return ACTION_SHORT_DESC.format(
            type=self._attribute,
            perk=perk_name,
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def attribute(self) -> "BaseAttribute":
        return self._attribute

    @property
    def figure(self) -> Optional["BaseFigure"]:
        return self._figure

    @figure.setter
    def figure(self, value: Optional["BaseFigure"]) -> None:
        self._figure = value
        if self._perk and self._figure:
            self._perk.person = self._figure.unit

    @property
    def perk(self) -> "BasePerk":
        return self._perk

    @property
    def texture(self) -> "Texture":
        return self._texture

    @property
    def radius(self) -> int:
        return self._radius

    @abstractmethod
    def realise(
        self,
        current_cell: "BaseCell",
        target: "BaseCell" = None
    ) -> None:
        """Совершить действие

        Args:
            current_cell: исходная клетка
            target: цель действия (графический объект)
        """
        pass
