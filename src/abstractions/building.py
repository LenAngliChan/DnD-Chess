from typing import TYPE_CHECKING

from src.abstractions.sprite import BasicSprite
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain


class BasicBuilding(BasicSprite):
    """Абстрактная модель здания"""

    def __init__(
        self,
        index: tuple[int, int],
        name: str,
        domain: "BasicDomain",
        textures: str,
        defence_bonus: int,
        figure: BasicSprite = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            index: позиция на доске
            name: имя
            domain: домен
            textures: текстура
            defence_bonus: бонус защиты
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        super().__init__(
            name=name + str(index),
            index=index,
            textures=textures,
            row=index[0],
            column=index[1],
            width=round(CELL_SIZE * 0.8),
            height=round(CELL_SIZE * 0.8),
            domain=domain,
        )
        self.color = domain.color
        self.figure = figure
        self.can_change_domain = can_change_domain
        self.defence_bonus = defence_bonus

    def change_domain(self, target: "BasicDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        self.domain = target
        self.color = target.color
