from typing import TYPE_CHECKING
from arcade import color, uicolor
from arcade.gui import Property, UIAnchorLayout, UISpace, bind

if TYPE_CHECKING:
    from arcade.types import Color


class BaseIndicatorBar(UIAnchorLayout):
    """A custom progress bar widget.

    A UIAnchorLayout is a layout that arranges its children in a specific way.
    The actual bar is a UISpace that fills the parent widget from left to right.
    """

    value = Property(0.0)

    def __init__(
        self,
        width: float,
        height: float,
        value: float = 1.0,
        bar_color: "Color" = color.GREEN,
        border_color: "Color" = uicolor.BLACK,
        background_color: "Color" = uicolor.GRAY_CONCRETE,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            size_hint=None,  # disable size hint, so it just uses the size given
        )
        self.with_background(color=background_color)
        self.with_border(color=border_color)

        self._bar = UISpace(
            color=bar_color,
            size_hint=(value, 1),
        )
        self.add(
            self._bar,
            anchor_x="left",
            anchor_y="top",
        )
        self.value = value

        # update the bar when the value changes
        bind(self, "value", self._update_bar)

    def _update_bar(self):
        self._bar.size_hint = (self.value, 1)
        self._bar.visible = self.value > 0
