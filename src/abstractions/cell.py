from abc import abstractmethod
from typing import TYPE_CHECKING

from src.abstractions.sprite import BasicSprite
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain
    from src.abstractions.figure import BasicFigure
    from src.abstractions.building import BasicBuilding


class BasicCell(BasicSprite):
    """Абстрактная модель клетки игральной доски"""

    def __init__(
        self,
        index: tuple[int, int],
        domain: "BasicDomain",
        building: "BasicBuilding" = None,
        figure: "BasicFigure" = None,
    ):
        """Инициализация клетки

        Args:
            index: позиция на доске
            domain: домен
            figure: фигура
            building: здание
        """
        super().__init__(
            name="CELL" + str(index),
            index=index,
            textures=domain.texture,    # допускает path или arcade.Texture
            row=index[0],
            column=index[1],
            width=CELL_SIZE,
            height=CELL_SIZE,
            domain=domain,
        )
        self.figure = figure
        self.building = building

    @abstractmethod
    def capture(self, figure: "BasicFigure"):
        """Захватить клетку"""
        pass

    def change_domain(self, target: "BasicDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        if self.building:
            if self.building.can_change_domain:
                self.__switch_domain(target=target)
                self.building.change_domain(target=target)
        else:
            self.__switch_domain(target=target)

    def __switch_domain(self, target: "BasicDomain"):
        """Сменить домен на новый

        Args:
            target: домен
        """
        # убрать бонус мощи для текущего домена
        self.domain.power -= 1
        # сменить домен, текстуры и прибавить бонус мощи для нового домена
        self.domain = target
        self.texture = self.domain.texture
        self.domain.power += 1
