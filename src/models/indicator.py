from src.abstractions.indicator import BaseIndicatorBar


class IndicatorBar(BaseIndicatorBar):

    def __init__(
        self,
        width: float,
        height: float,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
        )
