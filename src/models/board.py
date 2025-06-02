from typing import TYPE_CHECKING, Iterable, Optional
from arcade import color

from src.abstractions.board import BaseBoard
from src.models.collection import FigureCollection, CellCollection, BuildingCollection
from src.models.domain import Domain
from src.models.cell import Cell
from src.board.figures import get_figures_position
from src.board.buildings import get_buildings_position
from src.utils.enums import Time

if TYPE_CHECKING:
    from src.abstractions.cell import BaseCell
    from src.abstractions.action import BaseAction
    from collections import UserDict


class Board(BaseBoard):
    """Модель доски"""

    def __init__(self):
        """Инициализация доски"""

        blue_domain = Domain(
            name="Blue",
            texture_path=":resources:images/tiles/water.png",
            domain_color=color.BLUE,
        )
        red_domain = Domain(
            name="Red",
            texture_path=":resources:images/tiles/lava.png",
            domain_color=color.RED,
        )
        grey_domain = Domain(
            name="Gray",
            texture_path=":resources:images/tiles/brickGrey.png",
            domain_color=color.GRAY,
            power=0,
        )
        time = Time.day.value
        cells = CellCollection()
        figures = FigureCollection()
        buildings = BuildingCollection()
        super().__init__(
            blue_domain=blue_domain,
            red_domain=red_domain,
            grey_domain=grey_domain,
            time=time,
            cells=cells,
            figures=figures,
            buildings=buildings,
        )

    def initialize_cells(self):
        """Создать клетки"""
        for row in range(1, 8):
            for column in range(1, 7):
                if row <= 2:
                    domain = self._blue_domain
                elif row >= 6:
                    domain = self._red_domain
                else:
                    domain = self._grey_domain

                index = (column, row)
                new_cell = Cell(
                    index=index,
                    domain=domain,
                )
                self._cells[new_cell.index] = new_cell

    def initialize_figures(self):
        """Создать фигуры"""
        figures_position = get_figures_position()
        for cell in self._cells.values():
            figure_fabric = figures_position.get(cell.index)
            if figure_fabric:
                new_figure = figure_fabric(
                    domain=cell.domain,
                    index=cell.index,
                )
                cell.figure = new_figure
                self._figures[new_figure.name] = new_figure

    def initialize_buildings(self):
        """Создать здания"""
        for cell in self._cells.values():
            buildings_position = get_buildings_position()
            building_fabric = buildings_position.get(cell.index)
            if building_fabric:
                new_building = building_fabric(
                    index=cell.index,
                    domain=cell.domain,
                )
                cell.building = new_building
                self._buildings[new_building.index] = new_building

    def fill_domains(self):
        """Заполнить домены объектами"""
        self._blue_domain.set_figures(
            figures=[
                figure
                for figure in self._figures.values()
                if figure.domain == self._blue_domain
            ]
        )
        self._red_domain.set_figures(
            figures=[
                figure
                for figure in self._figures.values()
                if figure.domain == self._red_domain
            ]
        )

    def select_cell(
        self,
        cell: "BaseCell",
    ) -> None:
        """Выбрать клетку

        Args:
            cell: клетка
        """
        self._current_cell = cell
        try:
            # действие по умолчанию - движение
            actions = self.get_figure_action_list()
            if actions:
                self._current_action = actions["Move_Action"]
        finally:
            pass

    def select_action(
        self,
        action: "BaseAction",
    ) -> None:
        """Выбрать действие

        Args:
            action: действие
        """
        self._current_action = action

    def select_target(
        self,
        target: "BaseCell",
    ) -> None:
        """Выбрать цель действия

        Args:
            target: цель действия
        """
        self._start_action(target=target)

    def get_figure_action_list(self) -> Optional["UserDict[str, BaseAction]"]:
        """Получить список действий фигуры

        Returns:
            dict: список действий
        """
        if self._current_cell.figure:
            return self._current_cell.figure.get_action_list()

    def get_cell_neighbors(self, value: int = 1) -> Iterable["BaseCell"]:
        """Получить список допустимых клеток в качестве цели (соседей)

        Returns:
            iterable: список соседних клеток
        """
        cell_neighbors = []

        if self._current_cell:
            indexes = [
                (self._current_cell.index[0] + i, self._current_cell.index[1] + j)
                for i, j in [(-value, 0), (value, 0), (0, -value), (0, value)]
            ]

            for index in indexes:
                if index in self._cells:
                    cell_neighbors.append(self._cells.get(index))

        return cell_neighbors

    def start_circle(self):
        """Начать цикл битвы"""
        self._time = Time.day.value
        self._red_domain.end_circle()

    def finish_circle(self):
        """Завершить один цикл битвы"""
        if self._time == Time.day.value:
            self._time = Time.night.value
            self._blue_domain.end_circle()
        else:
            self._time = Time.day.value
            self._red_domain.end_circle()

    def _start_action(self, target: "BaseCell"):
        self._current_action.realise(
            current_cell=self._current_cell,
            target=target,
        )
        self._current_cell = None
        self._current_action = None
