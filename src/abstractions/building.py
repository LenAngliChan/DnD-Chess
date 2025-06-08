from typing import TYPE_CHECKING, Optional

from src.abstractions.sprite import BaseImage
from src.utils.descriptions import BUILDING_SHORT_DESC, BUILDING_LONG_DESC

if TYPE_CHECKING:
    from src.utils.tools import SpriteCore, Index
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure


class BaseBuilding(BaseImage):
    """Абстрактная UI модель здания"""

    def __init__(
        self,
        core: "SpriteCore",
        title: str,
        description: str,
        defence_bonus: int = 0,
        figure: "BaseFigure" = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            core: свойства графического объекта
            defence_bonus: бонус защиты
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        super().__init__(
            core=core,
        )
        self.with_border(width=3, color=core.domain.color)
        self._figure = figure
        self._can_change_domain = can_change_domain
        self._defence_bonus = defence_bonus
        self._title = title
        self._description = description

    def __str__(self) -> str:
        """Полное описание здания"""
        return BUILDING_LONG_DESC.format(title=self.desc, desc=self._description)

    @property
    def desc(self) -> str:
        """Краткое описание здания"""
        return BUILDING_SHORT_DESC.format(title=self._title, index=self.core.index)

    @property
    def title(self) -> str:
        """Название"""
        return self._title

    @property
    def defence(self) -> int:
        """Защита здания"""
        return self._defence_bonus

    @property
    def figure(self) -> Optional["BaseFigure"]:
        """Фигура в здании"""
        return self._figure

    @figure.setter
    def figure(self, value: BaseImage) -> None:
        """Установить фигуру внутри здания"""
        self._figure = value

    @property
    def can_change_domain(self) -> bool:
        """Может ли клетка с этим зданием сменить домен
        Некоторые здания (крепости) запрещают менять домен клетки
        """
        return self._can_change_domain

    @property
    def name(self) -> str:
        """Напрямую извлечь имя спрайта"""
        return self._core.name

    @property
    def index(self) -> "Index":
        """Напрямую извлечь индекс спрайта"""
        return self._core.index

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        self._core.domain = target
        self.with_border(width=3, color=self._core.domain.color)
