from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable
from collections import UserDict

from src.utils.descriptions import DOMAIN_SHORT_DESC, DOMAIN_LONG_DESC

if TYPE_CHECKING:
    from arcade import Texture
    from arcade.types import Color
    from src.abstractions.figure import BaseFigure


class BaseDomain(ABC):
    """Абстрактная модель домена"""

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        texture: "Texture",
        domain_color: "Color",
        power: int,
        turn: bool = False,
    ):
        """Инициализация домена

        Args:
            name: имя домена
            title: имя домена для вывода на gui
            description: описание домена
            texture: текстуры
            domain_color: цвет домена
            power: мощь домена
        """
        self._name = name
        self._title = title
        self._desc = description
        self._texture = texture
        self._color = domain_color
        self._power = power
        self._turn = turn
        self._figures: UserDict[str, "BaseFigure"] = UserDict()
        self._prisoners: UserDict[str, "BaseFigure"] = UserDict()

    def __str__(self) -> str:
        """Подробное описание домена"""
        return DOMAIN_LONG_DESC.format(title=self.desc, desc=self._desc)

    @property
    def desc(self) -> str:
        """Краткое описание домена"""
        return DOMAIN_SHORT_DESC.format(title=self._title, power=self._power)

    @property
    def title(self) -> str:
        """Наименование"""
        return self._title

    @property
    def name(self) -> str:
        """Имя домена"""
        return self._name

    @property
    def texture(self) -> "Texture":
        """Текстуры домена"""
        return self._texture

    @property
    def color(self) -> "Color":
        """Цвет домена"""
        return self._color

    @property
    def power(self) -> int:
        """Мощь домена"""
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        """Установить мощь домена"""
        self._power = value

    @property
    def turn(self) -> bool:
        """Очередь домена"""
        return self._turn

    @abstractmethod
    def set_figures(self, figures: Iterable["BaseFigure"]) -> None:
        """Установить фигуры домена

        Args:
            figures: список фигур
        """
        pass

    @abstractmethod
    def kill_figure(self, figure: "BaseFigure") -> None:
        """Убить фигуру домена

        Args:
            figure: фигура
        """
        pass

    @abstractmethod
    def get_prisoner(self, figure: "BaseFigure") -> None:
        """Установить фигуру-пленника домена

        Args:
            figure: фигура
        """
        pass

    @abstractmethod
    def end_circle(self) -> None:
        """Завершить цикл ходов домена, начав новый"""
        pass

    @abstractmethod
    def end_turn(self) -> None:
        """Завершить ход домена"""
        pass
