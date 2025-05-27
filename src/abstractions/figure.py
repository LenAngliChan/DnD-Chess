from abc import abstractmethod
from typing import TYPE_CHECKING, Iterable

from src.abstractions.sprite import BasicSprite
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain
    from src.abstractions.item import BasicAttribute
    from src.abstractions.unit import BasicUnit
    from src.abstractions.action import BasicAction
    from collections import UserDict


class BasicFigure(BasicSprite):
    """Абстрактная модель фигуры"""

    def __init__(
        self,
        name: str,
        index: tuple[int, int],
        textures: str,
        domain: "BasicDomain",
        unit: "BasicUnit",
        status: "BasicAttribute",
        actions: "UserDict[str, BasicAction]",
    ):
        """Инициализация фигуры

        Args:
            domain: домен
            name: имя
            index: позиция на доске
            textures: текстура
            unit: персонаж
            status: статус фигуры
        """
        super().__init__(
            name=name,
            index=index,
            textures=textures,
            row=index[0],
            column=index[1],
            width=CELL_SIZE // 2,
            height=CELL_SIZE // 2,
            domain=domain,
        )
        self.color = domain.color
        self.status = status
        self.unit = unit
        self.actions = actions
        self.can_move = True

    @abstractmethod
    def set_position(
        self,
        coord_x: int | float,
        coord_y: int | float,
    ) -> None:
        """Установить позицию фигуры

        Args:
            coord_x: координаты по оси X
            coord_y: координаты по оси Y
        """
        pass

    @abstractmethod
    def get_action_list(self) -> Iterable["BasicAction"]:
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """
        pass

    def change_domain(self, target: "BasicDomain") -> None:
        """Установить новый домен (запрещено для фигур)"""
        pass

    @abstractmethod
    def check_status(self):
        """Проверить статус фигуры"""
        pass

    @abstractmethod
    def end_circle(self) -> None:
        """Завершить ход"""
        pass
