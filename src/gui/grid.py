from typing import TYPE_CHECKING, NamedTuple, Dict
from arcade.gui import UIGridLayout

from src.gui.button import StartButton, CircleButton
from models.text import ScrollableTextArea
from src.gui.action_box import ActionBox
from src.utils.constants import (
    CELL_SIZE,
    GRID_ROW_COUNT,
    GRID_COLUMN_COUNT,
)

if TYPE_CHECKING:
    from arcade.gui.widgets import UIWidget
    from src.abstractions.board import BaseBoard
    from src.abstractions.text import BaseScrollableTextArea


class Entry(NamedTuple):
    child: "UIWidget"
    data: Dict


class BoardGrid(UIGridLayout):
    """Сетка игрового поля, куда будут размещены все графические объекты"""
    def __init__(
        self,
        board: "BaseBoard",
    ):
        super().__init__(
            column_count=GRID_COLUMN_COUNT,
            row_count=GRID_ROW_COUNT,
            width=GRID_COLUMN_COUNT * CELL_SIZE,
            height=GRID_ROW_COUNT * CELL_SIZE,
        )
        self._board = board
        self.rect = self.rect.at_position(position=(0, 0))
        self._actions: ActionBox = self.fill_actions(board=board)
        # информационное табло
        self._info_text = self.add(
            child=ScrollableTextArea(
                text="Game_Info",
            ),
            row=3,
            column=8,
            align_center_x=True,
            align_center_y=True,
        )

    @property
    def actions(self) -> ActionBox:
        return self._actions

    @property
    def info_text(self) -> ScrollableTextArea:
        return self._info_text

    def do_layout(self):
        """Переопределим метод расположения детей
        Потому что оригинал делает это как кусок говна
        """

        # детишки
        lookup: dict[tuple[int, int], Entry] = {}
        for entry in self._children:
            col_num = entry.data["column"]
            row_num = entry.data["row"]
            lookup[(col_num, row_num)] = entry

        # формируем координаты
        start_y = 0
        for row_num in range(self.row_count):
            start_x = 0
            for col_num in range(self.column_count):
                entry = lookup.get((col_num, row_num))
                if entry:
                    # коробка ребенка
                    child = entry.child
                    data = entry.data
                    # получаем коробку и расположение
                    new_rect = child.rect
                    align_center_x = data.get("align_center_x")
                    align_center_y = data.get("align_center_y")
                    # смещаем по координатам
                    if align_center_x:
                        # расположим по центру клетки
                        new_rect = new_rect.align_center_x(
                            value=start_x + CELL_SIZE // 2,
                        )
                    else:
                        # иначе - угол к углу
                        new_rect = new_rect.align_left(value=start_x)
                    if align_center_y:
                        # расположим по центру клетки
                        new_rect = new_rect.align_center_y(
                            value=start_y + CELL_SIZE // 2,
                        )
                    else:
                        # иначе - угол к углу
                        new_rect = new_rect.align_bottom(value=start_y)
                    child.rect = new_rect

                start_x += CELL_SIZE
            start_y += CELL_SIZE

    def fill_cells(self) -> None:
        """Заполнить поле клетками"""
        for cell in self._board.get_cells().values():
            self.add(
                child=cell,
                # align_x=cell.index[1] * CELL_SIZE,
                # align_y=cell.index[0] * CELL_SIZE,
                row=cell.index[1],
                column=cell.index[0],
            )

    def fill_buttons(self) -> None:
        """Заполнить поле кнопками"""
        self.add(
            child=StartButton(
                index=(7, 8),
                board=self._board,
            ),
            # align_x=start_index[1] * CELL_SIZE,
            # align_y=start_index[0] * CELL_SIZE,
            row=7,
            column=8,
            align_center_y=True,
            # column_span=2,
        )
        self.add(
            child=CircleButton(
                index=(6, 8),
                board=self._board,
            ),
            row=6,
            column=8,
            align_center_y=True,
        )

    def fill_actions(self, board: "BaseBoard") -> ActionBox:
        """Показать список возможных действий"""
        action_box = self.add(
            child=ActionBox(
                board=board,
            ),
            row=0,
            column=1,
            align_center_y=True,
        )
        return action_box
