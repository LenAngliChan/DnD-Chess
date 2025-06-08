import arcade
from arcade.gui import UIView
from typing import Any

from src.gui.grid import BoardGrid
from src.models.board import Board
from src.utils.tools import info_context, Index
from src.utils.constants import CELL_SIZE


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
        if not self._board.started:
            return

        index = Index(
            x=x,
            y=y,
        )
        if button == arcade.MOUSE_BUTTON_LEFT:
            self._grid.actions.hide_actions()
            selection = self._board.select_cell(index=index)
            if selection:
                self._grid.actions.show_actions()

        if button == arcade.MOUSE_BUTTON_RIGHT:
            selection = self._board.select_target(index=index)
            if selection:
                self._grid.actions.hide_actions()

    def on_update(self, delta_time: float) -> None:
        if self._board.started:
            self._grid.info_text.text = info_context.get()
