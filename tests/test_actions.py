import pytest
from numpy import isclose
from typing import TYPE_CHECKING

from tests.test_data.figures import TestBarbarian, TestCleric, TestWarlock
from src.board.domains import RedDomain, BlueDomain
from src.board.buildings import Castle, Altar
from src.models.cell import Cell
from src.utils.tools import Index
from src.utils.enums import ActionType, PerkStatus, PerkType

if TYPE_CHECKING:
    from src.abstractions.domain import BaseDomain
    from src.abstractions.figure import BaseFigure
    from src.abstractions.cell import BaseCell


@pytest.fixture()
def red_domain() -> "BaseDomain":
    return RedDomain(title="Red")


@pytest.fixture()
def blue_domain() -> "BaseDomain":
    return BlueDomain(title="Blue")


@pytest.fixture()
def barbarian_cell(red_domain) -> "BaseCell":
    index = Index(row=1, column=1)
    return Cell(
        index=index,
        domain=red_domain,
    )


@pytest.fixture()
def warlock_cell(blue_domain) -> "BaseCell":
    index = Index(row=0, column=1)
    building = Altar(
        index=index,
        domain=blue_domain,
    )
    cell = Cell(
        index=index,
        domain=blue_domain,
    )
    cell.building = building

    return cell


@pytest.fixture()
def cleric_cell(red_domain) -> "BaseCell":
    index = Index(row=1, column=0)
    building = Castle(
        index=index,
        domain=red_domain,
    )
    cell = Cell(
        index=index,
        domain=red_domain,
    )
    cell.building = building

    return cell


@pytest.fixture()
def empty_cell(blue_domain) -> "BaseCell":
    index = Index(row=1, column=2)
    return Cell(
        index=index,
        domain=blue_domain,
    )


@pytest.fixture()
def barbarian_figure(barbarian_cell) -> "BaseFigure":
    figure = TestBarbarian(
        index=barbarian_cell.index,
        domain=barbarian_cell.domain,
    )
    barbarian_cell.figure = figure
    return figure


@pytest.fixture()
def warlock_figure(warlock_cell) -> "BaseFigure":
    figure = TestWarlock(
        index=warlock_cell.index,
        domain=warlock_cell.domain,
    )
    warlock_cell.figure = figure
    return figure


@pytest.fixture()
def cleric_figure(cleric_cell) -> "BaseFigure":
    figure = TestCleric(
        index=cleric_cell.index,
        domain=cleric_cell.domain,
    )
    cleric_cell.figure = figure
    return figure


def test_move_action(
    barbarian_figure,
    barbarian_cell,
    warlock_figure,
    warlock_cell,
    empty_cell,
):
    """Тест для проверки действия - движение"""
    actions = barbarian_figure.get_actions()
    if actions:
        move_action = [
            action
            for action in actions.values()
            if action.attribute == ActionType.move.value
        ][0]

        # пытаемся двигаться в клетку с другой фигурой
        move_action.realise(
            current_cell=barbarian_cell,
            target=warlock_cell,
        )
        assert barbarian_cell.figure, "Фигура не должна переместиться!"
        assert warlock_cell.figure == warlock_figure, "Фигура не должна измениться!"
        assert barbarian_figure.can_move, "Фигура не должна пропустить ход!"

        # пытаемся двигаться в клетку без фигуры
        move_action.realise(
            current_cell=barbarian_cell,
            target=empty_cell,
        )
        assert not barbarian_cell.figure, "Фигура должна переместиться!"
        assert empty_cell.figure == barbarian_figure, "Фигура должна измениться!"
        assert not barbarian_cell.figure, "Клетка должна стать пустой!"
        assert not barbarian_figure.can_move, "Фигура должна пропустить ход!"


def test_pass_action(
    barbarian_figure,
    barbarian_cell,
):
    """Тест для проверки действия - пропустить ход"""
    actions = barbarian_figure.get_actions()
    if actions:
        pass_action = [
            action
            for action in actions.values()
            if action.attribute == ActionType.defend.value
        ][0]
        pass_action.realise(
            current_cell=barbarian_cell,
        )
        assert barbarian_cell.figure, "Фигура не должна переместиться!"
        assert not barbarian_figure.can_move, "Фигура должна пропустить ход!"


def test_melee_action(
    barbarian_cell,
    barbarian_figure,
    warlock_cell,
    warlock_figure,
):
    """Тест для проверки действия - физическая атака"""
    actions = barbarian_figure.get_actions()
    if actions:
        use_action = [
            action
            for action in actions.values()
            if (
                    action.attribute == ActionType.use.value
                    and
                    action.perk.attribute == PerkType.melee.value
            )
        ][0]
        use_action.realise(
            current_cell=barbarian_cell,
            target=warlock_cell,
        )
        assert barbarian_cell.figure, "Фигура не должна переместиться!"
        assert barbarian_figure.can_move, "Фигура не должна пропустить ход!"
        assert use_action.perk.status == PerkStatus.done.value, \
            "Способность должна уйти на перезарядку!"
        assert not isclose(
            a=warlock_figure.unit.hp_percent,
            b=1.0,
        ), "Фигура должна получить урон!"


def test_magic_action(
    barbarian_cell,
    barbarian_figure,
    warlock_cell,
    warlock_figure,
    cleric_cell,
    cleric_figure,
):
    """Тест для проверки действий: магическая атака и исцеление"""
    actions = warlock_figure.get_actions()
    if actions:
        use_action = [
            action
            for action in actions.values()
            if (
                    action.attribute == ActionType.use.value
                    and
                    action.perk.attribute == PerkType.elemental.value
            )
        ][0]

        # сначала атакуем заклинанием
        use_action.realise(
            current_cell=warlock_cell,
            target=barbarian_cell,
        )
        assert warlock_cell.figure, "Фигура не должна переместиться!"
        assert warlock_figure.can_move, "Фигура не должна пропустить ход!"
        assert use_action.perk.status == PerkStatus.done.value, \
            "Способность должна уйти на перезарядку!"
        assert not isclose(
            a=barbarian_figure.unit.hp_percent,
            b=1.0,
        ), "Фигура должна получить урон!"

        actions = cleric_figure.get_actions()
        if actions:
            use_action = [
                action
                for action in actions.values()
                if (
                        action.attribute == ActionType.use.value
                        and
                        action.perk.attribute == PerkType.heal.value
                )
            ][0]

            # затем исцеляем атакованного персонажа
            use_action.realise(
                current_cell=cleric_cell,
                target=barbarian_cell,
            )
            assert cleric_cell.figure, "Фигура не должна переместиться!"
            assert cleric_figure.can_move, "Фигура не должна пропустить ход!"
            assert use_action.perk.status == PerkStatus.done.value, \
                "Способность должна уйти на перезарядку!"
            assert isclose(
                a=barbarian_figure.unit.hp_percent,
                b=1.0,
            ), "Фигура должна исцелиться!"


def test_armor_action(
    cleric_cell,
    cleric_figure,
):
    """Тест для проверки действия - защитная стойка"""
    actions = cleric_figure.get_actions()
    if actions:
        # начальная защита
        base_cleric_defence = cleric_figure.unit.defense
        use_action = [
            action
            for action in actions.values()
            if (
                    action.attribute == ActionType.use.value
                    and
                    action.perk.attribute == PerkType.shield.value
            )
        ][0]

        # прибавка защиты
        defence_buff = use_action.perk._item._value._dice._side
        use_action.realise(
            current_cell=cleric_cell,
            target=cleric_cell,
        )

        # итоговая защита
        next_cleric_defence = cleric_figure.unit.defense

        assert cleric_cell.figure, "Фигура не должна переместиться!"
        assert cleric_figure.can_move, "Фигура не должна пропустить ход!"
        assert use_action.perk.status == PerkStatus.done.value, \
            "Способность должна уйти на перезарядку!"
        assert (base_cleric_defence + defence_buff) == next_cleric_defence, \
            "Фигура должна получить урон!"


def test_building_action(
    cleric_cell,
    cleric_figure,
    warlock_cell,
    warlock_figure,
):
    # проверка исцеления от замка
    cleric_figure.unit.defend_self(damage=100)
    for index in range(3):
        base_hp_percent = cleric_figure.unit.hp_percent
        cleric_cell.building.end_turn()
        next_hp_percent = cleric_figure.unit.hp_percent
        assert not isclose(
            a=base_hp_percent,
            b=next_hp_percent,
        ), "Не сработал эффект здания!"

    # проверка дара алтаря
    for index in range(3):
        base_hp = warlock_figure.unit.hit_points
        warlock_cell.building._action.realise(
            current_cell=warlock_cell,
            target=warlock_cell,
        )
        warlock_cell.building.end_turn()
        next_hp = warlock_figure.unit.hit_points
        assert not isclose(
            a=base_hp,
            b=next_hp,
        ), "Не сработал эффект здания!"
