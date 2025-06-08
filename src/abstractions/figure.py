from abc import abstractmethod
from typing import TYPE_CHECKING
from arcade.gui.widgets.layout import UIAnchorLayout

from src.abstractions.sprite import BaseImage
from src.utils.constants import CELL_SIZE
from src.utils.descriptions import FIGURE_LONG_DESC

if TYPE_CHECKING:
    from src.utils.tools import SpriteCore, Index
    from src.abstractions.domain import BaseDomain
    from src.abstractions.item import BaseAttribute
    from src.abstractions.unit import BaseUnit
    from src.abstractions.action import BaseAction
    from src.abstractions.indicator import BaseIndicatorBar
    from collections import UserDict


class BaseFigureSprite(BaseImage):
    """Абстрактная UI модель графики фигуры"""

    def __init__(
        self,
        core: "SpriteCore",
    ):
        """Инициализация фигуры

        Args:
            core: свойства графического объекта

        """
        super().__init__(
            core=core,
        )
        self.with_border(width=3, color=core.domain.color)

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен (запрещено для фигур)"""
        pass


class BaseFigure(UIAnchorLayout):
    """Абстрактная UI модель фигуры"""

    def __init__(
        self,
        sprite: BaseFigureSprite,
        indicator: "BaseIndicatorBar",
        unit: "BaseUnit",
        actions: "UserDict[str, BaseAction]",
        status: "BaseAttribute",
    ):
        """Инициализация фигуры

        Args:
            sprite: UI спрайт фигуры
            indicator: UI спрайт индикатора
            unit: персонаж
            actions: списсок действий фигуры
            status: статус фигуры
        """
        super().__init__(
            width=sprite.width,
            height=sprite.height,
            size_hint=(
                sprite.width / CELL_SIZE,
                sprite.height / CELL_SIZE,
            )
        )
        self._title = sprite.core.domain.title + " " + unit.title
        self._sprite = self.add(
            child=sprite,
        )
        self._indicator = self.add(
            child=indicator,
            # anchor_x="left",
            anchor_y="top",
        )
        self._unit = unit
        self._status = status
        self._actions = actions
        self._can_move = True

    def __str__(self) -> str:
        """Полное описание фигуры"""
        return FIGURE_LONG_DESC.format(title=self._title, unit=self._unit)

    @property
    def desc(self) -> str:
        """Краткое описание фигуры"""
        return self._title

    @property
    def title(self) -> str:
        """Наименование"""
        return self._title

    @property
    def sprite(self) -> BaseFigureSprite:
        """Графика фигуры"""
        return self._sprite

    @property
    def indicator(self) -> "BaseIndicatorBar":
        """Индикатор здоровья фигуры"""
        return self._indicator

    @property
    def unit(self) -> "BaseUnit":
        """Персонаж"""
        return self._unit

    @property
    def status(self) -> "BaseAttribute":
        """Статус фигуры"""
        return self._status

    @status.setter
    def status(self, value: "BaseAttribute") -> None:
        """Установить статус фигуры"""
        self._status = value

    @property
    def can_move(self) -> bool:
        """Возможность перемещаться"""
        return self._can_move

    @can_move.setter
    def can_move(self, value: bool) -> None:
        """Изменить возможность перемещаться"""
        self._can_move = value

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

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен (делигируем спрайту)"""
        self._sprite.change_domain(target=target)

    @abstractmethod
    def check_status(self):
        """Проверить статус фигуры"""
        pass

    @abstractmethod
    def end_circle(self) -> None:
        """Завершить ход"""
        pass

    @abstractmethod
    def kill_self(self) -> None:
        """Уничтожить себя"""
        pass

    @abstractmethod
    def get_actions(self) -> "UserDict[str, BaseAction]":
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """
        pass
