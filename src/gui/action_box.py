from typing import TYPE_CHECKING, List
from arcade.gui import UIBoxLayout

from src.gui.button import ActionButton
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.board import BaseBoard


class ActionBox(UIBoxLayout):

    def __init__(
        self,
        board: "BaseBoard",
    ):
        super().__init__(
            width=3 * CELL_SIZE,
            height=CELL_SIZE // 2,
            vertical=False,
        )
        self._board = board
        self._actions: List["ActionButton"] = []

    def prepare_buttons(self) -> None:
        """Подготовить панель кнопок действия"""
        row = 0
        for column in range(1, 13):
            action = self.add(
                child=ActionButton(
                    index=(row, column),
                    board=self._board,
                ),
            )
            action.visible = False
            self._actions.append(action)

    def show_actions(self) -> None:
        """Показать список возможных действий"""
        if self._board.current_cell:
            actions = self._board.get_figure_action_list()
            if actions:
                for index, action in enumerate(iterable=actions.values()):
                    self._actions[index].action = action
                    self._actions[index].visible = True

    def hide_actions(self) -> None:
        """Скрыть список возможных действий"""
        if self._actions:
            for action in self._actions:
                action.visible = False
