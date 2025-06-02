from typing import TYPE_CHECKING

from src.abstractions.building import BaseBuilding
from src.abstractions.tools import SpriteCore
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.figure import BaseFigure
    from src.abstractions.domain import BaseDomain


class Building(BaseBuilding):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "BaseDomain",
        name: str = "",
        texture_path: str = None,
        defence_bonus: int = 0,
        figure: "BaseFigure" = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            index: свойства графического объекта
            defence_bonus: бонус защиты
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        core = SpriteCore(
            name=name + str(index),
            index=index,
            texture_path=texture_path,
            width=CELL_SIZE // 1.5,
            height=CELL_SIZE // 1.5,
            domain=domain,
        )
        super().__init__(
            core=core,
            defence_bonus=defence_bonus,
            figure=figure,
            can_change_domain=can_change_domain,
        )
