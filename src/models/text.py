from arcade import resources
from src.abstractions.text import BaseScrollableTextArea


resources.load_kenney_fonts()


class ScrollableTextArea(BaseScrollableTextArea):

    def __init__(
        self,
        text: str = "",
    ):
        super().__init__(
            text=text,
        )
