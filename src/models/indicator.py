from typing import TYPE_CHECKING
from arcade import SpriteList, color

from src.abstractions.indicator import BasicIndicatorBar
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.figure import BasicFigure


class IndicatorBar(BasicIndicatorBar):
    """
    Represents a bar which can display information about a sprite.

    Args:
        figure:
            The owner of this indicator bar.
        index:
            The initial position of the bar.
    """

    def __init__(
        self,
        figure: "BasicFigure",
        row: float,
        column: float,
    ):
        super().__init__(
            sprite=figure,
            row=row,
            column=column,
            width=CELL_SIZE // 2,
            height=CELL_SIZE // 25,
            border_size=CELL_SIZE // 25,
        )
