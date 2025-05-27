from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.abstractions.perk import BasicPerk
    from src.abstractions.tools import BasicAttribute
    from src.abstractions.figure import BasicFigure
    from src.abstractions.cell import BasicCell


class BasicAction(ABC):
    """Абстрактная модель действия"""

    def __init__(
        self,
        name: str,
        attribute: "BasicAttribute",
        figure: "BasicFigure",
        perk: "BasicPerk" = None,
    ):
        """Инициализация действия

        Args:
            name: имя
            attribute: тип действия
            figure: фигура
            perk: способность
        """
        self.name = name
        self.attribute = attribute
        self.figure = figure
        self.perk = perk

    @abstractmethod
    def realise(
        self,
        current_cell: "BasicCell",
        target: "BasicCell" = None
    ) -> None:
        """Совершить действие

        Args:
            current_cell: исходная клетка
            target: цель действия (графический объект)
        """
        pass
