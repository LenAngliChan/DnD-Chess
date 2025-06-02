from abc import abstractmethod
from typing import TYPE_CHECKING
from arcade import color
from arcade.gui.widgets.layout import UIAnchorLayout

from src.abstractions.sprite import BaseImage

if TYPE_CHECKING:
    from src.abstractions.tools import SpriteCore
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure
    from src.abstractions.building import BaseBuilding


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
        self.core.domain.power -= 1
        # сменить домен, текстуры и прибавить бонус мощи для нового домена
        self.core.domain = target
        self.texture = self.core.domain.texture
        self.core.domain.power += 1


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

    @property
    def sprite(self) -> BaseCellSprite:
        return self._sprite

    @property
    def building(self) -> "BaseBuilding":
        return self._building

    @building.setter
    def building(self, value: "BaseBuilding") -> None:
        self._building = self.add(
            child=value,
        )

    @property
    def figure(self) -> "BaseFigure":
        return self._figure

    @figure.setter
    def figure(self, value: "BaseFigure") -> None:
        self._figure = self.add(
            child=value,
        )

    def remove_figure(self) -> None:
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
        return self.sprite.core.domain

    @property
    def name(self) -> str:
        """Напрямую извлечь имя спрайта"""
        return self.sprite.core.name

    @property
    def index(self) -> tuple[int, int]:
        """Напрямую извлечь индекс спрайта"""
        return self.sprite.core.index

    @abstractmethod
    def capture(self, figure: "BaseFigure") -> None:
        """Захватить клетку"""
        pass

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        if self.building:
            if self.building.can_change_domain:
                self.sprite.change_domain(target=target)
                self.building.change_domain(target=target)
        else:
            self.sprite.change_domain(target=target)
