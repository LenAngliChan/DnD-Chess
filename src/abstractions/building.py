from typing import TYPE_CHECKING, Optional

from src.abstractions.sprite import BaseImage
from src.utils.descriptions import BUILDING_SHORT_DESC, BUILDING_LONG_DESC
from src.utils.enums import ActionType, PerkStatus

if TYPE_CHECKING:
    from src.utils.tools import SpriteCore, Index
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure
    from src.abstractions.action import BaseAction
    from src.abstractions.cell import BaseCell


class BaseBuilding(BaseImage):
    """Абстрактная UI модель здания"""

    def __init__(
        self,
        core: "SpriteCore",
        title: str,
        description: str,
        action: "BaseAction" = None,
        defence_bonus: int = 0,
        figure: "BaseFigure" = None,
        can_change_domain: bool = True,
    ):
        """Инициализация здания

        Args:
            core: свойства графического объекта
            title: наименование для gui
            description: описание
            action: действие (эффект здания)
            defence_bonus: бонус защиты
            figure: фигура
            can_change_domain: возможность сменить домен
        """
        super().__init__(
            core=core,
        )
        self.with_border(width=3, color=core.domain.color)
        self._figure = figure
        self._action = action
        self._can_change_domain = can_change_domain
        self._defence_bonus = defence_bonus
        self._title = title
        self._description = description

    def __str__(self) -> str:
        """Полное описание здания"""
        return BUILDING_LONG_DESC.format(title=self.desc, desc=self._description)

    @property
    def desc(self) -> str:
        """Краткое описание здания"""
        return BUILDING_SHORT_DESC.format(title=self._title, index=self.core.index)

    @property
    def title(self) -> str:
        """Название"""
        return self._title

    @property
    def defence(self) -> int:
        """Защита здания"""
        return self._defence_bonus

    @property
    def figure(self) -> Optional["BaseFigure"]:
        """Фигура в здании"""
        return self._figure

    @figure.setter
    def figure(self, value: Optional["BaseFigure"]) -> None:
        """Установить фигуру внутри здания"""
        # убрать действие с текущей фигуры
        if self._figure and self._action:
            self._action.figure = None
            # если действие не для использования только зданиями
            if not self._action.attribute == ActionType.only_building.value:
                current_actions = self._figure.get_actions()
                current_actions.pop(self._action.name)
        # установить новую фигуру
        self._figure = value
        if self._action:
            self._action.figure = self._figure
            # добавить новой фигуре действие
            if self._figure:
                # если действие не для использования только зданиями
                if not self._action.attribute == ActionType.only_building.value:
                    current_actions = self._figure.get_actions()
                    current_actions[self._action.name] = self._action

    @property
    def can_change_domain(self) -> bool:
        """Может ли клетка с этим зданием сменить домен
        Некоторые здания (крепости) запрещают менять домен клетки
        """
        return self._can_change_domain

    @property
    def name(self) -> str:
        """Напрямую извлечь имя спрайта"""
        return self._core.name

    @property
    def index(self) -> "Index":
        """Напрямую извлечь индекс спрайта"""
        return self._core.index

    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        self._core.domain = target
        self.with_border(width=3, color=self._core.domain.color)

    def end_turn(self) -> None:
        """Завершить ход и активировать действие, уникальное для зданий"""
        if self._action:
            if self._action.attribute == ActionType.only_building.value:
                if self.parent:
                    parent: "BaseCell" = self.parent
                    self._action.realise(
                        current_cell=parent,
                        target=parent,
                    )
            self._action.perk.change_status(value=PerkStatus.active.value)
