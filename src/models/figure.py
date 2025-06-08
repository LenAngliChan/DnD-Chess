from typing import TYPE_CHECKING

from src.abstractions.figure import BaseFigure, BaseFigureSprite
from utils.tools import SpriteCore
from src.utils.enums import FigureStatus, ActionType
from src.models.action import Action, MoveAction, PassAction
from src.models.collection import ActionCollection
from src.models.indicator import IndicatorBar
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
    from arcade import Texture
    from src.utils.tools import Index
    from src.abstractions.item import BaseAttribute
    from src.abstractions.unit import BaseUnit
    from src.abstractions.action import BaseAction
    from src.abstractions.domain import BaseDomain
    from collections import UserDict


class FigureSprite(BaseFigureSprite):
    """UI модель графики фигуры"""

    def __init__(
        self,
        core: "SpriteCore",
    ):
        """Инициализация графики фигуры

        Args:
            core: свойства графического объекта

        """
        core.width = CELL_SIZE // 1.3
        core.height = CELL_SIZE // 1.3
        super().__init__(
            core=core,
        )


class Figure(BaseFigure):
    """UI модель фигуры"""

    def __init__(
        self,
        index: "Index",
        domain: "BaseDomain",
        texture: "Texture" = None,
        unit: "BaseUnit" = None,
        status: "BaseAttribute" = FigureStatus.alive.value,
    ):
        """Инициализация графики фигуры

            Args:
                index: индекс
                domain: домен
                texture: текстуры
                unit: персонаж
                status: статус
        """
        core = SpriteCore(
            name=domain.name + "_" + unit.name,
            index=index,
            texture=texture,
            domain=domain,
        )
        sprite = FigureSprite(
            core=core,
        )
        actions = self.__initialize_actions(unit=unit)
        health_bar = IndicatorBar(
            width=sprite.core.width,
            height=sprite.core.height // 10,
        )
        super().__init__(
            sprite=sprite,
            indicator=health_bar,
            unit=unit,
            actions=actions,
            status=status,
        )

    def get_actions(self) -> "UserDict[str, BaseAction]":
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """

        return self._actions

    def check_status(self):
        """Проверить статус фигуры"""
        self.indicator.value = self._unit.hp_percent
        if self._unit.is_dead:
            self.status = FigureStatus.captive.value

    def end_circle(self) -> None:
        """Завершить ход"""
        self._unit.end_circle()
        self._can_move = True

    def kill_self(self) -> None:
        """Уничтожить себя"""
        self.visible = False

    def __initialize_actions(self, unit: "BaseUnit" = None) -> ActionCollection:
        """Создать список возможных действий фигуры"""

        # действие - двигаться
        move_action = MoveAction(figure=self)

        # действие - пропустить ход
        pass_action = PassAction(figure=self)

        # список действий  - использовать способности
        use_actions = []
        if unit:
            use_actions.extend(
                [
                    Action(
                        name=perk.name + "_" + "Action",
                        figure=self,
                        texture=perk.texture,
                        attribute=ActionType.use.value,
                        perk=perk,
                    )
                    for perk in unit.get_perks().values()
                ]
            )

        use_actions.extend([move_action, pass_action])
        actions = ActionCollection(actions=use_actions)

        return actions
