from typing import TYPE_CHECKING, Optional
from arcade import color

from src.models.button import Button
from src.utils.tools import info_context
from src.utils.constants import CELL_SIZE
from src.utils.messages import NEXT_DOMAIN_MSG, ACTION_CHOOSE_MSG
from src.utils.enums import ActionType

if TYPE_CHECKING:
    from src.utils.tools import Index
    from src.abstractions.board import BaseBoard
    from src.abstractions.action import BaseAction


class StartButton(Button):

    def __init__(
        self,
        index: "Index",
        board: "BaseBoard",
    ):
        super().__init__(
            name="Start_Button",
            index=index,
            text="СТАРТ",
            board=board,
        )

    def on_click(self, event) -> bool:
        """Emit a ChooseColorEvent event when clicked."""
        self._board.start_circle()
        info_context.reset(value=NEXT_DOMAIN_MSG.format(domain=self._board.time))
        return True


class CircleButton(Button):

    def __init__(
        self,
        index: "Index",
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
        if self._board.started:
            self._board.finish_circle()
            info_context.reset(value=NEXT_DOMAIN_MSG.format(domain=self._board.time))
            return True


class ActionButton(Button):

    def __init__(
        self,
        index: "Index",
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
            texture_hovered=None,
            texture_pressed=None,
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
        if self._board.started and self._action and self.visible:
            self._board.select_action(action=self._action)
            info_context.set(value=ACTION_CHOOSE_MSG.format(action=self._action.desc))
            # пропуск хода активируем сразу - и на самого себя
            if self._action.attribute == ActionType.defend.value:
                self._board.select_target(index=self._board.current_cell.index)
            return True
