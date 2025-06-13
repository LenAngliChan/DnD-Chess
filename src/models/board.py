from typing import TYPE_CHECKING, Iterable, Optional
from arcade import color

from src.abstractions.board import BaseBoard
from src.models.collection import FigureCollection, CellCollection, BuildingCollection
from src.models.cell import Cell
from src.board.figures import get_figures_position
from src.board.buildings import get_buildings_position
from src.board.domains import RedDomain, BlueDomain, GrayDomain
from src.utils.enums import Time
from src.utils.tools import info_context, Index
from src.utils.messages import (
    CELL_SELECT_MSG,
    FIGURE_SELECT_MSG,
    NO_CELL_MSG,
    WRONG_DOMAIN_MSG,
    NO_FIGURE_MSG,
    WRONG_RADIUS_MSG,
)

if TYPE_CHECKING:
    from src.abstractions.cell import BaseCell
    from src.abstractions.action import BaseAction
    from collections import UserDict


class Board(BaseBoard):
    """Модель доски"""

    def __init__(self):
        """Инициализация доски"""

        blue_domain = BlueDomain(
            title=Time.night.value,
        )
        red_domain = RedDomain(
            title=Time.day.value,
        )
        grey_domain = GrayDomain(
            title=Time.dragon.value,
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

                index = Index(column=column, row=row)
                new_cell = Cell(
                    index=index,
                    domain=domain,
                )
                self._cells[new_cell.index.name] = new_cell

    def initialize_buildings(self):
        """Создать здания"""
        for cell in self._cells.values():
            buildings_position = get_buildings_position()
            building_fabric = buildings_position.get(cell.index.name)
            if building_fabric:
                new_building = building_fabric(
                    index=cell.index,
                    domain=cell.domain,
                )
                cell.building = new_building
                self._buildings[new_building.index.name] = new_building

    def initialize_figures(self):
        """Создать фигуры"""
        figures_position = get_figures_position()
        for cell in self._cells.values():
            figure_fabric = figures_position.get(cell.index.name)
            if figure_fabric:
                new_figure = figure_fabric(
                    index=cell.index,
                    domain=cell.domain,
                )
                cell.figure = new_figure
                self._figures[new_figure.name] = new_figure

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
        index: Index,
    ) -> bool:
        """Выбрать клетку

        Args:
            index: индекс клетки

        Returns:
            bool: успешно выбрана
        """
        cell = self._cells.get(index.name)
        if cell:
            self._current_cell = cell
            info_context.set(value=CELL_SELECT_MSG.format(cell=cell))
            if cell.figure:
                info_context.update(value=FIGURE_SELECT_MSG.format(figure=cell.figure))
                if cell.figure.domain.turn:
                    # действие по умолчанию - движение
                    actions = self.get_figure_action_list()
                    if actions:
                        self._current_action = actions["Move_Action"]

                    return True

        return False

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
        index: Index,
    ) -> bool:
        """Выбрать цель действия

        Args:
            index: индекс цели

        Returns:
            bool: успешно выбрана
        """
        if not self._current_cell:
            info_context.set(value=NO_CELL_MSG)
        elif not self._current_cell.figure.domain.turn:
            info_context.set(value=WRONG_DOMAIN_MSG.format(domain=self._time))
        elif not self._current_action:
            info_context.set(value=NO_FIGURE_MSG)
        else:
            if index.name in self.get_cell_neighbors(
                radius=self._current_action.radius,
            ):
                cell = self._cells.get(index.name)
                self._start_action(target=cell)
                return True
            else:
                info_context.set(value=WRONG_RADIUS_MSG)

        return False

    def get_figure_action_list(self) -> Optional["UserDict[str, BaseAction]"]:
        """Получить список действий фигуры

        Returns:
            dict: список действий
        """
        if self._current_cell.figure:
            return self._current_cell.get_figure_actions()

    def get_cell_neighbors(self, radius: int = 1) -> Iterable[str]:
        """Получить список индексов допустимых клеток в качестве цели (соседей)

        Returns:
            iterable: список индексов соседних клеток
        """

        if self._current_cell:
            indexes = []
            for r in range(1, radius + 1):
                indexes.extend([(-r, 0), (r, 0), (0, -r), (0, r)])
            cell_neighbors = [
                Index(
                    column=self._current_cell.index.column + i,
                    row=self._current_cell.index.row + j,
                ).name
                for i, j in indexes
            ]
            cell_neighbors.append(self._current_cell.index.name)
        else:
            cell_neighbors = []

        return cell_neighbors

    def start_circle(self):
        """Начать цикл битвы"""
        self._started = True
        self._time = Time.day.value
        self._red_domain.end_circle()

    def finish_circle(self):
        """Завершить один цикл битвы"""
        # в зависимости от цикла дня, пропускаем ходы доменов
        if self._time == Time.day.value:
            self._time = Time.night.value
            self._red_domain.end_turn()
            self._blue_domain.end_circle()
        else:
            self._time = Time.day.value
            self._blue_domain.end_turn()
            self._red_domain.end_circle()
        # активируем эффекты зданий
        for buildings in self._buildings.values():
            buildings.end_turn()
        # проверяем статусы фигур
        for figure in self._figures.values():
            figure.check_status()

    def _start_action(self, target: "BaseCell"):
        self._current_action.realise(
            current_cell=self._current_cell,
            target=target,
        )
        self._current_cell = None
        self._current_action = None
