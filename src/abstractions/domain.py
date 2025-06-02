from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable
from collections import UserDict
from arcade import load_texture

if TYPE_CHECKING:
    from arcade import Texture
    from arcade.types import Color
    from src.abstractions.figure import BasicUIFigure


class BaseDomain(ABC):
    """Абстрактная модель домена"""

    def __init__(
        self,
        name: str,
        texture_path: str,
        domain_color: "Color",
        power: int,
    ):
        """Инициализация домена

        Args:
            name: имя домена
            texture_path: путь к текстурам
            domain_color: цвет домена
            power: мощь домена
        """
        self._name = name
        self._texture = load_texture(file_path=texture_path)
        self._color = domain_color
        self._power = power
        self._figures: UserDict[tuple[int, int], "BasicUIFigure"] = UserDict()
        self._prisoners: UserDict[tuple[int, int], "BasicUIFigure"] = UserDict()

    @property
    def name(self) -> str:
        return self._name

    @property
    def texture(self) -> "Texture":
        return self._texture

    @property
    def color(self) -> "Color":
        return self._color

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        self._power = value

    @abstractmethod
    def set_figures(self, figures: Iterable["BasicUIFigure"]) -> None:
        """Установить фигуры домена

        Args:
            figures: список фигур
        """
        pass

    @abstractmethod
    def kill_figure(self, figure: "BasicUIFigure") -> None:
        """Убить фигуру домена

        Args:
            figure: фигура
        """
        pass

    @abstractmethod
    def get_prisoner(self, figure: "BasicUIFigure") -> None:
        """Установить фигуру-пленника домена

        Args:
            figure: фигура
        """
        pass

    @abstractmethod
    def end_circle(self):
        """Завершить цикл ходов домена, начав новый"""
        pass
