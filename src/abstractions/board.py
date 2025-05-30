from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable, Optional

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain
    from src.abstractions.sprite import BasicSprite
    from src.abstractions.figure import BasicFigure
    from src.abstractions.tools import BasicAttribute
    from src.abstractions.action import BasicAction
    from collections import UserDict


class BasicBoard(ABC):
    """Абстрактная модель доски"""

    def __init__(
        self,
        blue_domain: "BasicDomain",
        red_domain: "BasicDomain",
        grey_domain: "BasicDomain",
        time: "BasicAttribute",
        cells: "UserDict[tuple[int, int], BasicSprite]" = None,
        figures: "UserDict[str, BasicFigure]" = None,
        buildings: "UserDict[tuple[int, int], BasicSprite]" = None,
    ):
        """Инициализация доски

        Args:
            blue_domain: синий домен
            red_domain: красный домен
            grey_domain: серый домен
            time: цикл времени
            cells: клетки доски
            figures: фигуры доски
            buildings: здания доски
        """
        self.blue_domain = blue_domain
        self.red_domain = red_domain
        self.grey_domain = grey_domain
        self.time = time
        self.cells = cells
        self.figures = figures
        self.buildings = buildings
        self.current_cell: BasicSprite | None = None
        self.current_action: BasicAction | None = None

    @abstractmethod
    def initialize_cells(self) -> None:
        """Создать клетки"""
        pass

    @abstractmethod
    def initialize_figures(self) -> None:
        """Создать фигуры"""
        pass

    @abstractmethod
    def initialize_buildings(self) -> None:
        """Создать здания"""
        pass

    @abstractmethod
    def fill_domains(self) -> None:
        """Заполнить домены объектами"""
        pass

    @abstractmethod
    def select_cell(
        self,
        cell: "BasicSprite",
    ) -> None:
        """Выбрать клетку

        Args:
            cell: клетка
        """
        pass

    @abstractmethod
    def select_action(
        self,
        action: "BasicAction",
    ) -> None:
        """Выбрать действие

        Args:
            action: действие
        """
        pass

    @abstractmethod
    def select_target(
        self,
        target: "BasicSprite",
    ) -> None:
        """Выбрать цель действия

        Args:
            target: цель действия
        """
        pass

    @abstractmethod
    def get_figure_action_list(self) -> Optional["UserDict[str, BasicAction]"]:
        """Получить список действий фигуры

        Returns:
            dict: список действий
        """
        pass

    @abstractmethod
    def get_cell_neighbors(self) -> Iterable["BasicSprite"]:
        """Получить список допустимых клеток в качестве цели (соседей)

        Returns:
            iterable: список соседних клеток
        """
        pass

    @abstractmethod
    def start_circle(self) -> None:
        """Начать цикл битвы"""
        pass

    @abstractmethod
    def finish_circle(self) -> None:
        """Завершить один цикл битвы"""
        pass
