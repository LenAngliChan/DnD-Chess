from typing import TYPE_CHECKING

from src.abstractions.figure import BasicFigure
from src.utils.enums import FigureStatus, ActionType
from src.models.action import Action
from src.models.collection import ActionCollection
from src.models.indicator import IndicatorBar

if TYPE_CHECKING:
    from src.abstractions.domain import BasicDomain
    from src.abstractions.item import BasicAttribute
    from src.abstractions.unit import BasicUnit
    from src.abstractions.action import BasicAction
    from collections import UserDict


class Figure(BasicFigure):

    def __init__(
        self,
        domain: "BasicDomain",
        index: tuple[int, int],
        textures: str = "",
        unit: "BasicUnit" = None,
        status: "BasicAttribute" = FigureStatus.alive.value,
    ):
        name = domain.name + "_" + unit.name
        actions = self.__initialize_actions(unit=unit)
        health_bar = IndicatorBar(
            figure=self,
            row=index[0],
            column=index[1],
        )
        super().__init__(
            name=name,
            index=index,
            textures=textures,
            domain=domain,
            unit=unit,
            status=status,
            actions=actions,
            health_bar=health_bar,
        )

    def set_position(
        self,
        coord_x: int | float,
        coord_y: int | float,
    ) -> None:
        self.center_x = coord_x
        self.center_y = coord_y
        self.health_bar.position = (
            self.center_x,
            self.top,
        )

    def get_action_list(self) -> "UserDict[str, BasicAction]":
        """Получить список действий фигуры

        Returns:
            iterable: список действий
        """

        return self.actions

    def check_status(self):
        """Проверить статус фигуры"""
        self.health_bar.fullness = self.unit.current_hp / self.unit.hit_points
        if self.unit.current_hp == 0:
            self.status = FigureStatus.captive.value

    def end_circle(self) -> None:
        """Завершить ход"""
        self.unit.end_circle()
        self.can_move = True

    def kill_self(self) -> None:
        """Уничтожить себя"""
        for bar in self.health_bar.sprite_list:
            bar.kill()
        self.kill()

    def __initialize_actions(self, unit: "BasicUnit" = None) -> ActionCollection:
        """Создать список возможных действий фигуры"""

        # действие - двигаться
        move_action = Action(
            name="Move_Action",
            figure=self,
            attribute=ActionType.move.value,
        )

        # действие - пропустить ход
        pass_action = Action(
            name="Pass_Action",
            figure=self,
            attribute=ActionType.defend.value,
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
