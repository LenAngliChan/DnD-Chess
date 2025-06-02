from typing import TYPE_CHECKING

from src.abstractions.sprite import BaseImage

if TYPE_CHECKING:
    from src.abstractions.tools import SpriteCore
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure


class BaseBuilding(BaseImage):
    """Абстрактная UI модель здания"""

    def __init__(
        self,
        core: "SpriteCore",
        defence_bonus: int = 0,
        figure: "BaseFigure" = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            core: свойства графического объекта
            defence_bonus: бонус защиты
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        super().__init__(
            core=core,
        )
        self.with_border(width=3, color=core.domain.color)
        self._figure = figure
        self._can_change_domain = can_change_domain
        self._defence_bonus = defence_bonus

    @property
    def defence(self) -> int:
        return self._defence_bonus

    @property
    def figure(self) -> "BaseFigure":
        return self._figure

    @figure.setter
    def figure(self, value: BaseImage) -> None:
        self._figure = value

    @property
    def can_change_domain(self) -> bool:
        return self._can_change_domain

    @property
    def name(self) -> str:
        """Напрямую извлечь имя спрайта"""
        return self.core.name

    @property
    def index(self) -> tuple[int, int]:
        """Напрямую извлечь индекс спрайта"""
        return self.core.index

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        self.core.domain = target
        self.with_border(width=3, color=self.core.domain.color)
