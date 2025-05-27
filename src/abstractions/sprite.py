from abc import ABC, abstractmethod
from arcade import Sprite
from arcade.types import PathOrTexture
from typing import TYPE_CHECKING

from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain


class BasicSprite(Sprite, ABC):
    """Абстрактная модель спрайта (графического объекта)"""

    def __init__(
        self,
        name: str,
        index: tuple[int, int],
        textures: PathOrTexture,
        row: int,
        column: int,
        width: int,
        height: int,
        domain: "BasicDomain",
    ):
        """Инициализация спрайта

        Args:
            name: имя
            index: позиция на доске
            textures: текстура
            row: позиция по оси Y
            column: позиция по оси X
            width: ширина
            height: высота
            domain: домен
        """
        super().__init__(
            path_or_texture=textures,
            center_x=column * CELL_SIZE,
            center_y=row * CELL_SIZE,
        )
        self.name = name
        self.index = index
        self.width = width
        self.height = height
        self.domain = domain

    @abstractmethod
    def change_domain(self, target: "BasicDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        pass
