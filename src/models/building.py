from typing import TYPE_CHECKING

from src.abstractions.building import BasicBuilding

if TYPE_CHECKING:
    from src.abstractions.board import BasicDomain
    from src.abstractions.sprite import BasicSprite


class Building(BasicBuilding):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "BasicDomain",
        name: str = "",
        textures: str = "",
        defence_bonus: int = 0,
        figure: "BasicSprite" = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            index: позиция на доске
            name: имя
            domain: домен
            textures: текстура
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        super().__init__(
            index=index,
            name=name,
            domain=domain,
            textures=textures,
            defence_bonus=defence_bonus,
            figure=figure,
            can_change_domain=can_change_domain,
        )
