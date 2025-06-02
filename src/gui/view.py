import arcade
from arcade.gui import (
    UIGridLayout,
    UIView,
    UIBoxLayout,
    UILabel,
    UISpace,
)
from typing import Any

from src.gui.grid import BoardGrid
from models.text import ScrollableTextArea
from src.models.board import Board, Cell
from src.utils.enums import ActionType
from src.utils.constants import DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE, CELL_SIZE


class Chess(UIView):
    """Модель игры"""

    def __init__(self):
        """Инициализация игры"""

        super().__init__()
        # цвет фона
        self.background_color = arcade.color.GRAY
        # камера
        self.camera = arcade.Camera2D()
        # инициализация доски
        self._board = Board()
        # сетка игральной доски
        self._grid = self.add_widget(
            widget=BoardGrid(
                board=self._board,
            )
        )

    def setup(self):
        """Начало игры"""

        # заполнение игральной доски
        self._board.initialize_cells()
        self._board.initialize_buildings()
        self._board.initialize_figures()
        self._board.fill_domains()

        # заполнение сетки игры
        self._grid.fill_cells()
        self._grid.fill_buttons()
        self._grid.actions.prepare_buttons()
        self._grid.info_text.text = "Выберите фигуру!"

    def on_resize(self, width, height):
        """Resize window"""
        super().on_resize(width, height)
        self.camera.match_window()

    def on_mouse_press(
        self,
        x: int,
        y: int,
        button: int,
        key_modifiers: Any,
    ):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            index = (
                x // CELL_SIZE,
                y // CELL_SIZE,
            )
            self._grid.actions.hide_actions()
            cells = self._board.get_cells()
            if index in cells:
                cell = cells[index]
                self._board.select_cell(cell=cell)
                self._grid.actions.show_actions()
                cell_text = f"Выберна клетка {self._board.current_cell.index}!\n"
                figure_text = (
                    f"С фигурой {self._board.current_cell.figure.name}\n"
                    if self._board.current_cell.figure
                    else "Без фигуры!\n"
                )
                self._grid.info_text.clear()
                self._grid.info_text.text = cell_text + figure_text

        if button == arcade.MOUSE_BUTTON_RIGHT:
            if not self._board.current_cell:
                self._grid.info_text.clear()
                self._grid.info_text.text = "Сначала нужно выбрать клетку!"
            elif not self._board.current_action:
                self._grid.info_text.clear()
                self._grid.info_text.text = "Сначала нужно выбрать фигуру!"
            else:
                neighbours = self._board.get_cell_neighbors()
                index = (
                    x // CELL_SIZE,
                    y // CELL_SIZE,
                )
                cells = self._board.get_cells()
                if index in cells:
                    target = cells[index]
                    if target in neighbours:
                        self._grid.actions.hide_actions()
                        self._board.select_target(target=target)
                    else:
                        self._grid.info_text.clear()
                        self._grid.info_text.text = (
                            "Необходимо выбрать клетку в пределах "
                            "доступа (по горизонтали или вертикали)"
                        )
