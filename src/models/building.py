from typing import TYPE_CHECKING

from src.abstractions.building import BaseBuilding
from src.utils.tools import SpriteCore
from src.utils.constants import CELL_SIZE
from src.utils.descriptions import BUILDING_NAME

if TYPE_CHECKING:
    from arcade import Texture
    from src.utils.tools import Index
    from src.abstractions.figure import BaseFigure
    from src.abstractions.domain import BaseDomain
    from src.abstractions.action import BaseAction


class Building(BaseBuilding):

    def __init__(
        self,
        index: "Index",
        domain: "BaseDomain",
        action: "BaseAction" = None,
        name: str = None,
        title: str = None,
        description: str = None,
        texture: "Texture" = None,
        defence_bonus: int = 0,
        figure: "BaseFigure" = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            index: свойства графического объекта
            domain: домен
            action: действие (эффект здания)
            defence_bonus: бонус защиты
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        core = SpriteCore(
            name=BUILDING_NAME.format(name=name, index=index),
            index=index,
            texture=texture,
            width=CELL_SIZE // 1.1,
            height=CELL_SIZE // 1.1,
            domain=domain,
        )
        super().__init__(
            core=core,
            title=title,
            description=description,
            action=action,
            defence_bonus=defence_bonus,
            figure=figure,
            can_change_domain=can_change_domain,
        )
