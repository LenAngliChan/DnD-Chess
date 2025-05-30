from typing import TYPE_CHECKING, Iterable, Optional
from arcade import color

from src.abstractions.board import BasicBoard
from src.models.collection import FigureCollection, CellCollection, BuildingCollection
from src.models.domain import Domain
from src.models.cell import Cell
from src.models.text import GameText
from src.board.figures import get_figures_position
from src.board.buildings import get_buildings_position
from src.utils.enums import Time

if TYPE_CHECKING:
    from src.abstractions.action import BasicAction
    from src.abstractions.sprite import BasicSprite
    from collections import UserDict


class Board(BasicBoard):
    """Модель доски"""

    def __init__(self):
        """Инициализация доски"""

        blue_domain = Domain(
            name="Blue",
            textures=":resources:images/tiles/water.png",
            domain_color=color.BLUE,
        )
        red_domain = Domain(
            name="Red",
            textures=":resources:images/tiles/lava.png",
            domain_color=color.RED,
        )
        grey_domain = Domain(
            name="Gray",
            textures=":resources:images/tiles/brickGrey.png",
            domain_color=color.GRAY,
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

        # информационное табло
        self.info_text = GameText(
            title="Game_Info",
            index=(4, 7),
            text="Информация Информация Информация Информация Информация Информация",
        )

    def initialize_cells(self):
        """Создать клетки"""
        for row in range(1, 8):
            for column in range(1, 7):
                if row <= 2:
                    domain = self.blue_domain
                elif row >= 6:
                    domain = self.red_domain
                else:
                    domain = self.grey_domain

                index = (row, column)
                new_cell = Cell(
                    index=index,
                    domain=domain,
                )
                self.cells[new_cell.index] = new_cell

    def initialize_figures(self):
        """Создать фигуры"""
        figures_position = get_figures_position()
        for cell in self.cells.values():
            figure_fabric = figures_position.get(cell.index)
            if figure_fabric:
                new_figure = figure_fabric(
                    domain=cell.domain,
                    index=cell.index,
                )
                cell.figure = new_figure
                self.figures[new_figure.name] = new_figure

    def initialize_buildings(self):
        """Создать здания"""
        for cell in self.cells.values():
            buildings_position = get_buildings_position()
            building_fabric = buildings_position.get(cell.index)
            if building_fabric:
                new_building = building_fabric(
                    index=cell.index,
                    domain=cell.domain,
                )
                cell.building = new_building
                self.buildings[new_building.index] = new_building

    def fill_domains(self):
        """Заполнить домены объектами"""
        self.blue_domain.set_figures(
            figures=[
                figure
                for figure in self.figures.values()
                if figure.domain == self.blue_domain
            ]
        )
        self.red_domain.set_figures(
            figures=[
                figure
                for figure in self.figures.values()
                if figure.domain == self.red_domain
            ]
        )

    def select_cell(
        self,
        cell: Cell,
    ) -> None:
        """Выбрать клетку

        Args:
            cell: клетка
        """
        self.current_cell = cell
        try:
            actions = self.get_figure_action_list()
            if actions:
                self.current_action = actions["Move_Action"]
        finally:
            pass

    def select_action(
        self,
        action: "BasicAction",
    ) -> None:
        """Выбрать действие

        Args:
            action: действие
        """
        self.current_action = action

    def select_target(
        self,
        target: Cell,
    ) -> None:
        """Выбрать цель действия

        Args:
            target: цель действия
        """
        self._start_action(target=target)

    def get_figure_action_list(self) -> Optional["UserDict[str, BasicAction]"]:
        """Получить список действий фигуры

        Returns:
            dict: список действий
        """
        if self.current_cell.figure:
            return self.current_cell.figure.get_action_list()

    def get_cell_neighbors(self) -> Iterable["BasicSprite"]:
        """Получить список допустимых клеток в качестве цели (соседей)

        Returns:
            iterable: список соседних клеток
        """
        cell_neighbors = []

        if self.current_cell:
            indexes = [
                (self.current_cell.index[0] + i, self.current_cell.index[1] + j)
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            ]

            for index in indexes:
                if index in self.cells:
                    cell_neighbors.append(self.cells.get(index))

        return cell_neighbors

    def start_circle(self):
        """Начать цикл битвы"""
        self.time = Time.day.value
        self.red_domain.end_circle()

    def finish_circle(self):
        """Завершить один цикл битвы"""
        if self.time == Time.day.value:
            self.time = Time.night.value
            self.blue_domain.end_circle()
        else:
            self.time = Time.day.value
            self.red_domain.end_circle()

    def _start_action(self, target: Cell):
        self.current_action.realise(
            current_cell=self.current_cell,
            target=target,
        )
        self.current_cell = None
        self.current_action = None
