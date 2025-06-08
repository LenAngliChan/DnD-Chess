from typing import TYPE_CHECKING

from src.abstractions.cell import BaseCell, BaseCellSprite
from src.utils.tools import SpriteCore
from src.utils.descriptions import CELL_NAME

if TYPE_CHECKING:
    from src.utils.tools import Index
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure
    from src.abstractions.building import BaseBuilding


class CellSprite(BaseCellSprite):
    """Абстрактная UI модель клетки игральной доски"""

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


class Cell(BaseCell):
    """UI модель клетки игральной доски"""

    def __init__(
        self,
        index: "Index",
        domain: "BaseDomain",
        building: "BaseBuilding" = None,
        figure: "BaseFigure" = None,
    ):
        """Инициализация клетки

        Args:
            index: свойства графического объекта
            building: здание клетки
            figure: фигура клетки
        """
        core = SpriteCore(
            name=CELL_NAME.format(index=index),
            index=index,
            texture=domain.texture,
            domain=domain,
        )
        sprite = CellSprite(
            core=core,
        )
        super().__init__(
            sprite=sprite,
            building=building,
            figure=figure,
        )

    def capture(self, figure: "BaseFigure") -> None:
        """Захватить клетку"""
        self.figure = figure    # через setter, там доп. логика
        self.change_domain(target=figure.domain)
