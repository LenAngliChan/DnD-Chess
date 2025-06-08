from typing import TYPE_CHECKING, Iterable
from arcade import color

from src.abstractions.domain import BaseDomain
from src.models.collection import FigureCollection
from src.utils.constants import BASE_DOMAIN_POWER

if TYPE_CHECKING:
    from arcade import Texture
    from arcade.types import Color
    from src.abstractions.figure import BaseFigure


class Domain(BaseDomain):
    """Модель домена"""

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        texture: "Texture",
        domain_color: "Color" = color.GRAY,
        power: int = BASE_DOMAIN_POWER,
        turn: bool = False,
    ):
        """Инициализация домена

        Args:
            name: имя
            title: имя домена для вывода на gui
            description: описание домена
            texture: текстуры
            domain_color: цвет домена
            power: мощь домена
            turn: очередь домена
        """
        super().__init__(
            name=name,
            title=title,
            description=description,
            texture=texture,
            domain_color=domain_color,
            power=power,
            turn=turn,
        )

    def set_figures(self, figures: Iterable["BaseFigure"]) -> None:
        """Установить фигуры домена

        Args:
            figures: список фигур
        """
        self._figures = FigureCollection(figures=figures)
        self._prisoners = FigureCollection()

    def kill_figure(self, figure: "BaseFigure") -> None:
        """Убить фигуру домена

        Args:
            figure: фигура
        """
        figure = self._figures.pop(figure.name)
        figure.kill_self()

    def get_prisoner(self, figure: "BaseFigure") -> None:
        """Установить фигуру-пленника домена

        Args:
            figure: фигура
        """
        self._prisoners[figure.name] = figure

    def end_circle(self):
        """Завершить цикл ходов домена, начав новый"""
        self._turn = True
        for figure in self._figures.values():
            figure.end_circle()

    def end_turn(self) -> None:
        """Завершить ход домена"""
        self._turn = False
        for figure in self._figures.values():
            figure.can_move = False
