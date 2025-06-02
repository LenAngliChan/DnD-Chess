from typing import TYPE_CHECKING, Type

from src.models.figure import Figure
from src.units.units import (
    UnitBarbarian,
    UnitBard,
    UnitCleric,
    UnitDruid,
    UnitFighter,
    UnitMonk,
    UnitPaladin,
    UnitRanger,
    UnitRogue,
    UnitSorcerer,
    UnitWarlock,
    UnitWizard,
)

if TYPE_CHECKING:
    from src.models.domain import Domain


class Barbarian(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitBarbarian()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Barbarian.png',
            unit=unit,
        )


class Bard(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitBard()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Bard.png',
            unit=unit,
        )


class Cleric(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitCleric()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Cleric.png',
            unit=unit,
        )


class Druid(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitDruid()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Druid.png',
            unit=unit,
        )


class Fighter(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitFighter()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Fighter.png',
            unit=unit,
        )


class Monk(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitMonk()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Monk.png',
            unit=unit,
        )


class Paladin(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitPaladin()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Paladin.png',
            unit=unit,
        )


class Ranger(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitRanger()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Ranger.png',
            unit=unit,
        )


class Rogue(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitRogue()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Rogue.png',
            unit=unit,
        )


class Sorcerer(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitSorcerer()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Sorcerer.png',
            unit=unit,
        )


class Warlock(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitWarlock()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Warlock.png',
            unit=unit,
        )


class Wizard(Figure):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        unit = UnitWizard()
        super().__init__(
            index=index,
            domain=domain,
            texture_path='src/sprites/units/Wizard.png',
            unit=unit,
        )


def get_figures_position() -> dict[tuple[int, int], Type[Figure]]:
    figures_position: dict[tuple[int, int], Type[Figure]] = {}
    for row in range(1, 8):
        for column in range(1, 7):
            index = (column, row)
            if row in (1, 7):
                if column == 1:
                    figures_position[index] = Druid
                elif column == 2:
                    figures_position[index] = Bard
                elif column == 3:
                    figures_position[index] = Sorcerer
                elif column == 4:
                    figures_position[index] = Wizard
                elif column == 5:
                    figures_position[index] = Warlock
                else:
                    figures_position[index] = Cleric
            if row in (2, 6):
                if column == 1:
                    figures_position[index] = Ranger
                elif column == 2:
                    figures_position[index] = Monk
                elif column == 3:
                    figures_position[index] = Fighter
                elif column == 4:
                    figures_position[index] = Barbarian
                elif column == 5:
                    figures_position[index] = Paladin
                else:
                    figures_position[index] = Rogue

    return figures_position
