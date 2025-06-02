from arcade import load_texture
from typing import TYPE_CHECKING

from src.abstractions.button import BaseButton
from src.abstractions.tools import SpriteCore
from src.utils.constants import (
    CELL_SIZE,
    TEXTURE_RED_BUTTON_NORMAL,
    TEXTURE_RED_BUTTON_HOVER,
    TEXTURE_RED_BUTTON_PRESS,
)

if TYPE_CHECKING:
    from src.abstractions.board import BaseBoard


class Button(BaseButton):

    def __init__(
        self,
        name: str,
        index: tuple[int, int],
        text: str,
        board: "BaseBoard",
        width: float = CELL_SIZE,
        height: float = CELL_SIZE // 2,
        texture_path: str = TEXTURE_RED_BUTTON_NORMAL,
        texture_hovered_path: str | None = TEXTURE_RED_BUTTON_HOVER,
        texture_pressed_path: str | None = TEXTURE_RED_BUTTON_PRESS,
    ):
        core = SpriteCore(
            name=name,
            index=index,
            texture_path=texture_path,
            width=width,
            height=height,
        )
        texture_hovered = (
            load_texture(file_path=texture_hovered_path) if texture_hovered_path else None
        )
        texture_pressed = (
            load_texture(file_path=texture_pressed_path) if texture_pressed_path else None
        )
        super().__init__(
            core=core,
            text=text,
            texture_hovered=texture_hovered,
            texture_pressed=texture_pressed,
        )
        self._board = board
