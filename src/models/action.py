from typing import TYPE_CHECKING

from src.abstractions.action import BaseAction
from src.utils.enums import ActionType, PerkType, FigureStatus, ActionKWArgs

if TYPE_CHECKING:
    from src.abstractions.perk import BasePerk
    from src.abstractions.tools import BaseAttribute
    from src.abstractions.figure import BaseFigure
    from src.abstractions.cell import BaseCell


class Action(BaseAction):

    def __init__(
        self,
        name: str,
        figure: "BaseFigure",
        attribute: "BaseAttribute" = ActionType.move.value,
        perk: "BasePerk" = None,
        texture_path: str = None,
    ):
        """Инициализация действия

        Args:
            name: имя
            attribute: тип действия
            perk: способность
        """
        super().__init__(
            name=name,
            attribute=attribute,
            figure=figure,
            perk=perk,
            texture_path=texture_path,
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
        # Пока нет ходов, закоментировал - для тестов
        # if not self.figure.can_move:
        #     print("Персонаж не может двигаться!")
        #     return

        if self.attribute == ActionType.defend.value:
            self.figure.can_move = False
            print("Пропуск хода!")
            return
        else:
            if not target:
                print("Не выбрана цель!")
                return
            if target.figure:
                if self.attribute == ActionType.move.value:
                    print("Невозможно переместиться на клетку с другой фигурой!")
                    return
                else:
                    if (
                        self.figure == target.figure
                        and self.perk.attribute in (PerkType.melee.value, PerkType.elemental.value)
                    ):
                        print("Нельзя атаковать самого себя оружием или магией!")
                        return
            else:
                if self.attribute == ActionType.use.value:
                    print("Чтобы использовать способность нужна цель!")
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
        self.figure.can_move = False

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

        # Расчет бонусов от домена и здания
        domain_bonus = self.figure.domain.power - target.figure.domain.power
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
        current_cell.remove_figure()
        target.capture(figure=self.figure)

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
