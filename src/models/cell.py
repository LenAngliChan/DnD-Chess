from typing import TYPE_CHECKING

from src.abstractions.cell import BasicCell

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain
    from src.abstractions.sprite import BasicSprite
    from src.abstractions.figure import BasicFigure


class Cell(BasicCell):
    """Модель клетки игральной доски"""

    def __init__(
        self,
        index: tuple[int, int],
        domain: "BasicDomain",
        building: "BasicSprite" = None,
        figure: "BasicFigure" = None,
    ):
        """Инициализация клетки

        Args:
            index: позиция на доске
            domain: домен
            figure: фигура
        """
        super().__init__(
            index=index,
            domain=domain,
            figure=figure,
            building=building,
        )

    def capture(self, figure: "BasicFigure"):
        self.figure = figure
        self.change_domain(target=figure.domain)
