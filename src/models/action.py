from typing import TYPE_CHECKING

from src.utils.tools import info_context
from src.abstractions.action import BaseAction
from src.utils.enums import ActionType, PerkType, FigureStatus
from src.utils.messages import (
    ACTION_DEFEND_MSG,
    ACTION_NO_TARGET_MSG,
    ACTION_WRONG_MOVE_MSG,
    ACTION_WRONG_USE_MSG,
    ACTION_NO_FIGURE_MSG,
    ACTION_CANNOT_MOVE_MSG,
    ACTION_USE_MSG,
    ACTION_MOVE_MSG,
    ACTION_NO_SACRIFICE_MSG,
    ACTION_SACRIFICE_MSG,
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
        texture: "Texture",
        figure: "BaseFigure" = None,
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

        # Если нет фигуры, то пропускаем
        if not self._figure:
            return

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

        # активируем способность, цель - фигура (персонаж фигуры)
        if self.perk.attribute == PerkType.shield.value:
            # если используется щит, то цель - сам персонаж
            unit = self.figure.unit
        else:
            # иначе - другой юнит
            unit = target.figure.unit
        self.perk.activate(
            target=unit,
            domain_bonus=domain_bonus,
            building_bonus=building_bonus,
        )

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


class BuildingAction(BaseAction):
    """Модель действия от зданий"""

    def __init__(
        self,
        name: str,
        texture: "Texture",
        figure: "BaseFigure" = None,
        attribute: "BaseAttribute" = ActionType.only_building.value,
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

        # Если нет фигуры, то пропускаем
        if not self._figure:
            return

        # эффект работает только на цели того же домена, что и здание
        if (
                self.attribute == ActionType.only_building.value
                and
                current_cell.domain != target.domain
        ):
            return

        # если это жертва алтарю
        if self.attribute == ActionType.sacrifice.value:
            # то потребуются жертвы
            if not current_cell.domain.prisoners:
                info_context.reset(value=ACTION_NO_SACRIFICE_MSG)
                return

        self._create_action(
            current_cell=current_cell,
            target=current_cell,
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
        # если это жертва алтарю
        if self.attribute == ActionType.sacrifice.value:
            # то потребуются жертвы
            prisoners = current_cell.domain.prisoners
            for prisoner in prisoners:
                # берем первую попавшуюся жертву
                victim = prisoners.pop(prisoner)
                info_context.set(
                    value=ACTION_SACRIFICE_MSG.format(
                        figure=self.figure.title,
                        target=victim.title,
                    )
                )
                break

        self.__use_perk(
            target=target,
        )

    def __use_perk(
        self,
        target: "BaseCell",
    ) -> None:
        """Использование способности

        Args:
            target: цель действия (клетка)
        """

        # активируем способность, цель - фигура (персонаж фигуры)
        self.perk.activate(
            target=self.figure.unit,
        )

        # если эффект здания, то можем дальше не идти
        if not self.attribute == ActionType.only_building.value:
            # проверяем статус фигуры
            target.figure.check_status()
