from collections import UserDict
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from src.abstractions.cell import BaseCell
    from src.abstractions.building import BaseBuilding
    from src.abstractions.figure import BaseFigure
    from src.abstractions.perk import BasePerk
    from src.abstractions.action import BaseAction


class PerkCollection(UserDict):

    def __init__(
        self,
        perks: Iterable["BasePerk"] = None,
    ):
        if perks:
            collection = {
                perk.name: perk
                for perk in perks
            }
        else:
            collection = perks
        super().__init__(collection)


class FigureCollection(UserDict):

    def __init__(
        self,
        figures: Iterable["BaseFigure"] = None,
    ):
        if figures:
            collection = {
                figure.name: figure
                for figure in figures
            }
        else:
            collection = figures
        super().__init__(collection)


class CellCollection(UserDict):

    def __init__(
        self,
        cells: Iterable["BaseCell"] = None,
    ):
        if cells:
            collection = {
                cell.index.name: cell
                for cell in cells
            }
        else:
            collection = cells
        super().__init__(collection)


class BuildingCollection(UserDict):

    def __init__(
        self,
        buildings: Iterable["BaseBuilding"] = None,
    ):
        if buildings:
            collection = {
                building.index.name: building
                for building in buildings
            }
        else:
            collection = buildings
        super().__init__(collection)


class ActionCollection(UserDict):

    def __init__(
        self,
        actions: Iterable["BaseAction"] = None,
    ):
        if actions:
            collection = {
                action.name: action
                for action in actions
            }
        else:
            collection = actions
        super().__init__(collection)
