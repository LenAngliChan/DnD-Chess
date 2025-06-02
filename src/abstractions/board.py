from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterable, Optional

if TYPE_CHECKING:
    from src.abstractions.domain import BaseDomain
    from src.abstractions.sprite import BaseImage
    from src.abstractions.cell import BaseCell
    from src.abstractions.figure import BaseFigure
    from src.abstractions.tools import BaseAttribute
    from src.abstractions.action import BaseAction
    from collections import UserDict


class BaseBoard(ABC):
    """Абстрактная модель доски"""

    def __init__(
        self,
        blue_domain: "BaseDomain",
        red_domain: "BaseDomain",
        grey_domain: "BaseDomain",
        time: "BaseAttribute",
        cells: "UserDict[tuple[int, int], BaseCell]" = None,
        figures: "UserDict[str, BaseFigure]" = None,
        buildings: "UserDict[tuple[int, int], BaseImage]" = None,
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
        self._blue_domain = blue_domain
        self._red_domain = red_domain
        self._grey_domain = grey_domain
        self._time = time
        self._cells = cells
        self._figures = figures
        self._buildings = buildings
        self._current_cell: Optional["BaseCell"] = None
        self._current_action: Optional["BaseAction"] = None

    @property
    def current_cell(self) -> Optional["BaseCell"]:
        return self._current_cell

    @property
    def current_action(self) -> Optional["BaseAction"]:
        return self._current_action

    def get_cells(self) -> "UserDict[tuple[int, int], BaseCell]":
        """Получить список клеток доски

        Returns:
            dict: список клеток
        """
        return self._cells

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
        cell: "BaseCell",
    ) -> None:
        """Выбрать клетку

        Args:
            cell: клетка
        """
        pass

    @abstractmethod
    def select_action(
        self,
        action: "BaseAction",
    ) -> None:
        """Выбрать действие

        Args:
            action: действие
        """
        pass

    @abstractmethod
    def select_target(
        self,
        target: "BaseCell",
    ) -> None:
        """Выбрать цель действия

        Args:
            target: цель действия
        """
        pass

    @abstractmethod
    def get_figure_action_list(self) -> Optional["UserDict[str, BaseAction]"]:
        """Получить список действий фигуры

        Returns:
            dict: список действий
        """
        pass

    @abstractmethod
    def get_cell_neighbors(self, value: int = 1) -> Iterable["BaseCell"]:
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
