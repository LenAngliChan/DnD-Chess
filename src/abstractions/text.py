from abc import ABC
from typing import TYPE_CHECKING
from arcade import uicolor, load_texture
from arcade.gui import (
    UIAnchorLayout,
    UIImage,
    UITextArea,
)

from src.utils.constants import (
    DEFAULT_FONT_SIZE,
    DEFAULT_FONT_NAME,
    CELL_SIZE,
)

if TYPE_CHECKING:
    from utils.tools import F_spec
    from arcade.types import Color

TEX_SCROLL_DOWN = load_texture(":resources:gui_basic_assets/scroll/indicator_down.png")
TEX_SCROLL_UP = load_texture(":resources:gui_basic_assets/scroll/indicator_up.png")


class BaseScrollableTextArea(UITextArea, UIAnchorLayout, ABC):
    """This widget is a text area that can be scrolled, like a UITextLayout, but shows indicator,
    that the text can be scrolled."""

    def __init__(
        self,
        text: str,
        text_color: "Color" = uicolor.WHITE_CLOUDS,
        font_name: str = DEFAULT_FONT_NAME,
        font_size: int = DEFAULT_FONT_SIZE,
        **kwargs: "F_spec.kwargs",
    ):
        super().__init__(
            text=text,
            text_color=text_color,
            width=3 * CELL_SIZE,
            height=5 * CELL_SIZE,
            font_name=font_name,
            font_size=font_size,
            size_hint=(0.5, 0.8),
            kwargs=kwargs)

        indicator_size = 22
        self._down_indicator = UIImage(
            texture=TEX_SCROLL_DOWN,
            size_hint=None,
            width=indicator_size,
            height=indicator_size,
        )
        self._down_indicator.visible = False
        self.add(
            child=self._down_indicator,
            anchor_x="right",
            anchor_y="bottom",
            align_x=3,
        )

        self._up_indicator = UIImage(
            texture=TEX_SCROLL_UP,
            size_hint=None,
            width=indicator_size,
            height=indicator_size,
        )
        self._up_indicator.visible = False
        self.add(
            child=self._up_indicator,
            anchor_x="right",
            anchor_y="top",
            align_x=3,
        )
        self.with_border(color=uicolor.DARK_BLUE_MIDNIGHT_BLUE)
        self.with_background(color=uicolor.DARK_BLUE_MIDNIGHT_BLUE.replace(a=125))
        self.with_padding(left=5)

    def on_update(self, dt):
        self._up_indicator.visible = self.layout.view_y < 0
        self._down_indicator.visible = (
            abs(self.layout.view_y) < self.layout.content_height - self.layout.height
        )
