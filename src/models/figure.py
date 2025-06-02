from typing import TYPE_CHECKING

from src.abstractions.figure import BaseFigure, BaseFigureSprite
from src.abstractions.tools import SpriteCore
from src.utils.enums import FigureStatus, ActionType
from src.models.action import Action
from src.models.collection import ActionCollection
from src.models.indicator import IndicatorBar
from src.utils.constants import CELL_SIZE

if TYPE_CHECKING:
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
        core.width = CELL_SIZE // 2
        core.height = CELL_SIZE // 2
        super().__init__(
            core=core,
        )


class Figure(BaseFigure):
    """UI модель фигуры"""

    def __init__(
        self,
        index: tuple[int, int],
        domain: "BaseDomain",
        texture_path: str = None,
        unit: "BaseUnit" = None,
        status: "BaseAttribute" = FigureStatus.alive.value,
    ):
        """Инициализация графики фигуры

            Args:
                index: свойства графического объекта
                domain:
                texture_path:
                unit:
                status:
        """
        core = SpriteCore(
            name=domain.name + "_" + unit.name,
            index=index,
            texture_path=texture_path,
            domain=domain,
        )
        sprite = FigureSprite(
            core=core,
        )
        actions = self.__initialize_actions(unit=unit)
        health_bar = IndicatorBar(
            width=sprite.core.width,
            height=sprite.core.height // 8,
        )
        super().__init__(
            sprite=sprite,
            indicator=health_bar,
            unit=unit,
            actions=actions,
            status=status,
        )

    def get_action_list(self) -> "UserDict[str, BaseAction]":
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """

        return self.actions

    def check_status(self):
        """Проверить статус фигуры"""
        self.indicator.value = self.unit.current_hp / self.unit.hit_points
        if self.unit.current_hp == 0:
            self.status = FigureStatus.captive.value

    def end_circle(self) -> None:
        """Завершить ход"""
        self.unit.end_circle()
        self.can_move = True

    def kill_self(self) -> None:
        """Уничтожить себя"""
        self.visible = False

    def __initialize_actions(self, unit: "BaseUnit" = None) -> ActionCollection:
        """Создать список возможных действий фигуры"""

        # действие - двигаться
        move_action = Action(
            name="Move_Action",
            figure=self,
            attribute=ActionType.move.value,
            texture_path='src/sprites/perks/blazing-feet.png',
        )

        # действие - пропустить ход
        pass_action = Action(
            name="Pass_Action",
            figure=self,
            attribute=ActionType.defend.value,
            texture_path='src/sprites/perks/armor-0.png',
        )

        # список действий  - использовать способности
        use_actions = []
        if unit:
            use_actions.extend(
                [
                    Action(
                        name=perk.name + "_" + "Action",
                        figure=self,
                        attribute=ActionType.use.value,
                        perk=perk,
                    )
                    for perk in unit.perks.values()
                ]
            )

        use_actions.extend([move_action, pass_action])
        actions = ActionCollection(actions=use_actions)

        return actions
