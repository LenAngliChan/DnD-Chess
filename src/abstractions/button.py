from typing import TYPE_CHECKING
from arcade.gui import (
    UITextureButton,
)

if TYPE_CHECKING:
    from arcade import Texture
    from utils.tools import SpriteCore


class BaseButton(UITextureButton):

    def __init__(
        self,
        core: "SpriteCore",
        text: str,
        texture_hovered: "Texture" = None,
        texture_pressed: "Texture" = None,
    ):
        super().__init__(
            text=text,
            width=core.width,
            height=core.height,
            texture=core.texture,
            texture_hovered=texture_hovered,
            texture_pressed=texture_pressed,
            multiline=True,
        )
        self._core = core

    @property
    def core(self) -> "SpriteCore":
        return self._core
