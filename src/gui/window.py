import arcade

from src.gui.view import Chess
from src.utils.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
)


class ChessWindow(arcade.Window):

    def __init__(self):
        super().__init__(
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            title=WINDOW_TITLE,
            resizable=True,
            update_rate=1,
            draw_rate=1,
        )
        self.game = Chess()

    def start_game(self):
        self.game.setup()
        self.show_view(self.game)
