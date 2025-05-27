from collections import UserDict
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from src.abstractions.perk import BasicPerk
    from src.abstractions.sprite import BasicSprite
    from src.abstractions.action import BasicAction


class PerkCollection(UserDict):

    def __init__(
        self,
        perks: Iterable["BasicPerk"] = None,
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
        figures: Iterable["BasicSprite"] = None,
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
        cells: Iterable["BasicSprite"] = None,
    ):
        if cells:
            collection = {
                cell.index: cell
                for cell in cells
            }
        else:
            collection = cells
        super().__init__(collection)


class BuildingCollection(UserDict):

    def __init__(
        self,
        buildings: Iterable["BasicSprite"] = None,
    ):
        if buildings:
            collection = {
                building.index: building
                for building in buildings
            }
        else:
            collection = buildings
        super().__init__(collection)


class ActionCollection(UserDict):

    def __init__(
        self,
        actions: Iterable["BasicAction"] = None,
    ):
        if actions:
            collection = {
                action.name: action
                for action in actions
            }
        else:
            collection = actions
        super().__init__(collection)
