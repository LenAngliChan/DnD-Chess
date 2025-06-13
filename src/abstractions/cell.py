from abc import abstractmethod
from typing import TYPE_CHECKING, Optional
from arcade import color
from arcade.gui.widgets.layout import UIAnchorLayout

from src.abstractions.sprite import BaseImage
from src.utils.descriptions import CELL_SHORT_DESC, CELL_LONG_DESC

if TYPE_CHECKING:
    from src.utils.tools import SpriteCore, Index
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure
    from src.abstractions.building import BaseBuilding
    from src.abstractions.action import BaseAction
    from collections import UserDict


class BaseCellSprite(BaseImage):
    """Абстрактная UI модель графики клетки игральной доски"""

    def __init__(
        self,
        core: "SpriteCore",
    ):
        """Инициализация клетки

        Args:
            core: свойства графического объекта
        """
        super().__init__(
            core=core,
        )
        self.with_border(color=color.BLACK, width=1)

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        # убрать бонус мощи для текущего домена
        self._core.domain.power -= 1
        # сменить домен, текстуры и прибавить бонус мощи для нового домена
        self._core.domain = target
        self.texture = self._core.domain.texture
        self._core.domain.power += 1


class BaseCell(UIAnchorLayout):
    """Абстрактная UI модель клетки игральной доски"""

    def __init__(
        self,
        sprite: BaseCellSprite,
        building: "BaseBuilding" = None,
        figure: "BaseFigure" = None,
    ):
        """Инициализация клетки

        Args:
            sprite: UI спрайт клетки
            building: здание клетки
            figure: фигура клетки
        """
        super().__init__(
            width=sprite.width,
            height=sprite.height,
        )
        self._sprite = self.add(
            child=sprite,
        )
        if building:
            self.add(
                child=building,
            )
        if figure:
            self.add(
                child=figure,
            )
        self._building = building
        self._figure = figure
        self._title = "Клетка"

    def __str__(self) -> str:
        """Полное описание клетки"""
        has_building = self._building if self._building else "Пусто"
        return CELL_LONG_DESC.format(title=self.desc, building=has_building)

    @property
    def desc(self) -> str:
        """Краткое описание клетки"""
        return CELL_SHORT_DESC.format(index=self._sprite.core.index)

    @property
    def title(self) -> str:
        """Краткое описание клетки"""
        return self._title

    @property
    def sprite(self) -> BaseCellSprite:
        """Доступ к графике клетки"""
        return self._sprite

    @property
    def building(self) -> Optional["BaseBuilding"]:
        """Здание на клетке (при наличии)"""
        return self._building

    @building.setter
    def building(self, value: "BaseBuilding") -> None:
        """Установить здание (допускается только при инициализации доски)"""
        self._building = self.add(
            child=value,
        )

    @property
    def figure(self) -> Optional["BaseFigure"]:
        """Фигура на клетке (при наличии)"""
        return self._figure

    @figure.setter
    def figure(self, value: "BaseFigure") -> None:
        """Установить фигуру на клетке"""
        self._figure = self.add(
            child=value,
        )
        if self._building:
            self._building.figure = self._figure

    def remove_figure(self) -> None:
        """Удалить фигуру с клетки"""
        if self._figure:
            self.remove(
                child=self._figure,
            )
            self._figure = None
            if self._building:
                self._building.figure = None

    @property
    def domain(self) -> "BaseDomain":
        """Напрямую извлечь домен спрайта"""
        return self._sprite.core.domain

    @property
    def name(self) -> str:
        """Напрямую извлечь имя спрайта"""
        return self._sprite.core.name

    @property
    def index(self) -> "Index":
        """Напрямую извлечь индекс спрайта"""
        return self._sprite.core.index

    @abstractmethod
    def capture(self, figure: "BaseFigure") -> None:
        """Захватить клетку фигурой"""
        pass

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        if self._building:
            if self._building.can_change_domain:
                self._sprite.change_domain(target=target)
                self._building.change_domain(target=target)
        else:
            self._sprite.change_domain(target=target)

    @abstractmethod
    def get_figure_actions(self) -> "UserDict[str, BaseAction]":
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """
        pass
