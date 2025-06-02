from abc import abstractmethod
from typing import TYPE_CHECKING
from arcade.gui.widgets.layout import UIAnchorLayout

from src.abstractions.sprite import BaseImage
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.tools import SpriteCore
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

    @property
    def sprite(self) -> BaseFigureSprite:
        return self._sprite

    @property
    def indicator(self) -> "BaseIndicatorBar":
        return self._indicator

    @property
    def unit(self) -> "BaseUnit":
        return self._unit

    @property
    def status(self) -> "BaseAttribute":
        return self._status

    @status.setter
    def status(self, value: "BaseAttribute") -> None:
        self._status = value

    @property
    def actions(self) -> "UserDict[str, BaseAction]":
        return self._actions

    @property
    def can_move(self) -> bool:
        return self._can_move

    @can_move.setter
    def can_move(self, value: bool) -> None:
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
    def index(self) -> tuple[int, int]:
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
    def get_action_list(self) -> "UserDict[str, BaseAction]":
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """
        pass
