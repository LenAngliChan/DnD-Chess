from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable
from collections import UserDict
from arcade import color
from arcade.texture import default_texture_cache

if TYPE_CHECKING:
    from src.abstractions.figure import BasicFigure


class BasicDomain(ABC):
    """Абстрактная модель домена"""

    def __init__(
        self,
        name: str,
        textures: str,
        domain_color: color,
        power: int,
    ):
        """Инициализация домена

        Args:
            name: имя
            textures: текстура
            domain_color: цвет домена
            power: мощь домена
        """
        self.name = name
        self.texture = default_texture_cache.load_or_get_texture(file_path=textures)
        self.color = domain_color
        self.power = power
        self.figures: UserDict[tuple[int, int], "BasicFigure"] = UserDict()
        self.prisoners: UserDict[tuple[int, int], "BasicFigure"] = UserDict()

    @abstractmethod
    def set_figures(self, figures: Iterable["BasicFigure"]) -> None:
        """Установить фигуры домена

        Args:
            figures: список фигур
        """
        pass

    @abstractmethod
    def kill_figure(self, figure: "BasicFigure") -> None:
        """Убить фигуру домена

        Args:
            figure: фигура
        """
        pass

    @abstractmethod
    def get_prisoner(self, figure: "BasicFigure") -> None:
        """Установить фигуру-пленника домена

        Args:
            figure: фигура
        """
        pass

    @abstractmethod
    def end_circle(self):
        """Завершить цикл ходов домена, начав новый"""
        pass
