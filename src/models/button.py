from typing import TYPE_CHECKING, Optional

from src.abstractions.button import BaseButton
from utils.tools import SpriteCore
from src.utils.constants import CELL_SIZE
from src.utils.textures import (
    RED_BUTTON_NORMAL_TEXTURE,
    RED_BUTTON_HOVER_TEXTURE,
    RED_BUTTON_PRESS_TEXTURE,
)

if TYPE_CHECKING:
    from src.utils.tools import Index
    from arcade import Texture
    from src.abstractions.board import BaseBoard


class Button(BaseButton):

    def __init__(
        self,
        name: str,
        index: "Index",
        text: str,
        board: "BaseBoard",
        width: float = CELL_SIZE,
        height: float = CELL_SIZE // 2,
        texture: "Texture" = RED_BUTTON_NORMAL_TEXTURE,
        texture_hovered: Optional["Texture"] = RED_BUTTON_HOVER_TEXTURE,
        texture_pressed: Optional["Texture"] = RED_BUTTON_PRESS_TEXTURE,
    ):
        core = SpriteCore(
            name=name,
            index=index,
            texture=texture,
            width=width,
            height=height,
        )
        super().__init__(
            core=core,
            text=text,
            texture_hovered=texture_hovered,
            texture_pressed=texture_pressed,
        )
        self._board = board
