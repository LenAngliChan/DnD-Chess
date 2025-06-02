from typing import TYPE_CHECKING, Optional
from arcade import color

from src.models.button import Button
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.board import BaseBoard
    from src.abstractions.action import BaseAction


class StartButton(Button):

    def __init__(
        self,
        index: tuple[int, int],
        board: "BaseBoard",
    ):
        super().__init__(
            name="Start_Button",
            index=index,
            text="Начать игру",
            board=board,
        )

    def on_click(self, event) -> bool:
        """Emit a ChooseColorEvent event when clicked."""
        self._board.start_circle()
        return True


class CircleButton(Button):

    def __init__(
        self,
        index: tuple[int, int],
        board: "BaseBoard",
    ):
        super().__init__(
            name="Circle_Button",
            index=index,
            text="Завершить ход",
            board=board,
        )

    def on_click(self, event) -> bool:
        """Emit a ChooseColorEvent event when clicked."""
        self._board.finish_circle()
        return True


class ActionButton(Button):

    def __init__(
        self,
        index: tuple[int, int],
        board: "BaseBoard",
        action: "BaseAction" = None,
        text: str = "",
        width: float = CELL_SIZE // 2,
        height: float = CELL_SIZE // 2,
    ):
        super().__init__(
            name="Action_Button",
            index=index,
            text=text,
            board=board,
            width=width,
            height=height,
            texture_hovered_path=None,
            texture_pressed_path=None,
        )
        self._action = action
        self.with_border(width=CELL_SIZE // 10, color=color.GOLD)

    @property
    def action(self) -> Optional["BaseAction"]:
        return self._action

    @action.setter
    def action(self, value: "BaseAction") -> None:
        self._action = value
        self.texture = value.texture
        # self.text = value.perk.name

    def on_click(self, event) -> bool:
        """Emit a ChooseColorEvent event when clicked."""
        if self._action and self.visible:
            self._board.select_action(action=self._action)
            return True
