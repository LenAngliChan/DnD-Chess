from typing import TYPE_CHECKING

from src.utils.tools import info_context
from src.abstractions.action import BaseAction
from src.utils.enums import ActionType, PerkType, FigureStatus, ActionKWArgs
from src.utils.messages import (
    ACTION_DEFEND_MSG,
    ACTION_NO_TARGET_MSG,
    ACTION_WRONG_MOVE_MSG,
    ACTION_WRONG_USE_MSG,
    ACTION_NO_FIGURE_MSG,
    ACTION_CANNOT_MOVE_MSG,
    ACTION_USE_MSG,
    ACTION_MOVE_MSG,
)
from src.utils.textures import MOVE_ACTION_TEXTURE, PASS_ACTION_TEXTURE

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.perk import BasePerk
    from utils.tools import BaseAttribute
    from src.abstractions.figure import BaseFigure
    from src.abstractions.cell import BaseCell


class Action(BaseAction):
    """Модель действия"""

    def __init__(
        self,
        name: str,
        figure: "BaseFigure",
        texture: "Texture",
        attribute: "BaseAttribute" = ActionType.move.value,
        perk: "BasePerk" = None,
    ):
        """Инициализация действия

        Args:
            name: имя
            figure: фигура
            attribute: тип действия
            perk: способность
            texture: иконка действия
        """
        super().__init__(
            name=name,
            attribute=attribute,
            figure=figure,
            perk=perk,
            texture=texture,
        )

    def realise(
        self,
        current_cell: "BaseCell",
        target: "BaseCell" = None
    ) -> None:
        """Совершить действие

        Args:
            current_cell: исходная клетка
            target: цель действия (графический объект)
        """

        if self.attribute == ActionType.defend.value:
            self.figure.can_move = False
            info_context.update(
                value=ACTION_DEFEND_MSG.format(figure=self.figure.title)
            )
            return
        else:
            if not target:
                info_context.reset(value=ACTION_NO_TARGET_MSG)
                return
            if target.figure:
                if self.attribute == ActionType.move.value:
                    info_context.reset(value=ACTION_WRONG_MOVE_MSG)
                    return
                else:
                    if (
                        self.figure == target.figure
                        and self.perk.attribute in (PerkType.melee.value, PerkType.elemental.value)
                    ):
                        info_context.reset(value=ACTION_WRONG_USE_MSG)
                        return
            else:
                if self.attribute == ActionType.use.value:
                    info_context.reset(value=ACTION_NO_FIGURE_MSG)
                    return
            self._create_action(
                current_cell=current_cell,
                target=target,
            )

    def _create_action(
        self,
        current_cell: "BaseCell",
        target: "BaseCell",
    ) -> None:
        """Процесс совершения действия

        Args:
            current_cell: исходная клетка
            target: цель действия (клетка)
        """
        if self.attribute == ActionType.use.value:
            # if self.perk.attribute == PerkType.melee.value:
            #     self.__create_convergence(target=target)
            self.__use_perk(
                current_cell=current_cell,
                target=target,
            )
        else:
            self.__create_move(
                current_cell=current_cell,
                target=target,
            )

    def __use_perk(
        self,
        current_cell: "BaseCell",
        target: "BaseCell",
    ) -> None:
        """Использование способности

        Args:
            current_cell: исходная клетка
            target: цель действия (клетка)
        """
        info_context.set(
            value=ACTION_USE_MSG.format(
                figure=self.figure.title,
                action=self.perk.title,
                target=target.figure.title,
            )
        )

        # Расчет бонусов от домена и здания
        domain_bonus = (self.figure.domain.power - target.figure.domain.power) // 2
        building_bonus = target.building.defence if target.building else 0
        action_kwargs = {
            ActionKWArgs.domain_bonus.value: domain_bonus,
            ActionKWArgs.building_bonus.value: building_bonus,
        }

        # активируем способность, цель - фигура (персонаж фигуры)
        if self.perk.attribute == PerkType.shield.value:
            # если используется щит, то цель - сам персонаж
            unit = self.figure.unit
        else:
            # иначе - другой юнит
            unit = target.figure.unit
        self.perk.activate(target=unit, **action_kwargs)

        # проверяем статус фигуры
        target.figure.check_status()

        # если фигура мертва
        if target.figure.status == FigureStatus.captive.value:
            figure = target.figure
            target.remove_figure()
            target.domain.kill_figure(figure=figure)
            self.figure.domain.get_prisoner(figure=figure)
            # если атака ближнего боя - перемещаемся на клетку
            if self.perk.attribute == PerkType.melee.value:
                self.__create_move(
                    current_cell=current_cell,
                    target=target,
                )

    def __create_move(
        self,
        current_cell: "BaseCell",
        target: "BaseCell",
    ) -> None:
        """Перемещение фигуры

        Args:
            current_cell: исходная клетка
            target: цель действия (клетка)
        """
        info_context.update(
            value=ACTION_MOVE_MSG.format(
                figure=self.figure.title,
                cell=target.title,
            )
        )

        if not self.figure.can_move:
            info_context.set(value=ACTION_CANNOT_MOVE_MSG)
            return
        current_cell.remove_figure()
        target.capture(figure=self.figure)
        self.figure.can_move = False

    def __create_convergence(
        self,
        target: "BaseCell",
    ) -> None:
        """Сближение фигуры для ближнего боя

        Args:
            target: цель действия (клетка)
        """

        # если цель слева
        if self.figure.center_x > target.center_x:
            new_coord_x = target.right
        # если цель справа
        elif self.figure.center_x < target.center_x:
            new_coord_x = target.left
        # если цель на той же оси X
        else:
            new_coord_x = self.figure.center_x

        # если цель сверху
        if self.figure.center_y > target.center_x:
            new_coord_y = target.bottom
        # если цель снизу
        elif self.figure.center_y < target.center_x:
            new_coord_y = target.top
        # если цель на той же оси Y
        else:
            new_coord_y = self.figure.center_y


class MoveAction(Action):
    """Модель действия - движение"""
    def __init__(
        self,
        figure: "BaseFigure",
    ):
        super().__init__(
            name="Move_Action",
            figure=figure,
            texture=MOVE_ACTION_TEXTURE,
        )


class PassAction(Action):
    """Модель действия - пропустить ход"""
    def __init__(
        self,
        figure: "BaseFigure",
    ):
        super().__init__(
            name="Pass_Action",
            figure=figure,
            attribute=ActionType.defend.value,
            texture=PASS_ACTION_TEXTURE,
        )
