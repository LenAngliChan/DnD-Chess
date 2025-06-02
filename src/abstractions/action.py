from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

from arcade import load_texture

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.perk import BasePerk
    from src.abstractions.tools import BaseAttribute
    from src.abstractions.figure import BaseFigure
    from src.abstractions.cell import BaseCell


class BaseAction(ABC):
    """Абстрактная модель действия"""

    def __init__(
        self,
        name: str,
        attribute: "BaseAttribute",
        figure: "BaseFigure",
        perk: "BasePerk" = None,
        texture_path: str = None,
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
        self._texture = self._create_texture(
            perk=perk,
            texture_path=texture_path,
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def attribute(self) -> "BaseAttribute":
        return self._attribute

    @property
    def figure(self) -> "BaseFigure":
        return self._figure

    @property
    def perk(self) -> "BasePerk":
        return self._perk

    @property
    def texture(self) -> Optional["Texture"]:
        return self._texture

    @staticmethod
    def _create_texture(
        perk: "BasePerk" = None,
        texture_path: str = None,
    ) -> Optional["Texture"]:
        if perk:
            return perk.texture
        elif texture_path:
            return load_texture(file_path=texture_path)

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
