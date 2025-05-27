from typing import TYPE_CHECKING, Iterable
from arcade import color

from src.abstractions.domain import BasicDomain
from src.models.collection import FigureCollection
from src.utils.constants import BASE_DOMAIN_POWER

if TYPE_CHECKING:
    from src.abstractions.sprite import BasicSprite


class Domain(BasicDomain):
    """Модель домена"""

    def __init__(
        self,
        name: str,
        textures: str,
        domain_color: color = color.GRAY,
        power: int = BASE_DOMAIN_POWER,
    ):
        """Инициализация домена

        Args:
            name: имя
            textures: текстура
            domain_color: цвет домена
            power: мощь домена
        """
        super().__init__(
            name=name,
            textures=textures,
            domain_color=domain_color,
            power=power,
        )

    def set_figures(self, figures: Iterable["BasicSprite"]) -> None:
        """Установить фигуры домена

        Args:
            figures: список фигур
        """
        self.figures = FigureCollection(figures=figures)
        self.prisoners = FigureCollection()

    def kill_figure(self, figure: "BasicSprite") -> None:
        """Убить фигуру домена

        Args:
            figure: фигура
        """
        figure = self.figures.pop(figure.name)
        figure.kill()
        return figure

    def get_prisoner(self, figure: "BasicSprite") -> None:
        """Установить фигуру-пленника домена

        Args:
            figure: фигура
        """
        self.prisoners[figure.name] = figure

    def end_circle(self):
        """Завершить цикл ходов домена, начав новый"""
        for figure in self.figures.values():
            figure.end_circle()
