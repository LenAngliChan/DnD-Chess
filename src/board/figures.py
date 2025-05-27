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
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitBarbarian()
        textures = 'src/sprites/Barbarian.png'
        super().__init__(
            domain=domain,
            index=index,
            textures=textures,
            unit=unit,
        )


class Bard(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitBard()
        textures = 'src/sprites/Bard.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Cleric(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitCleric()
        textures = 'src/sprites/Cleric.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Druid(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitDruid()
        textures = 'src/sprites/Druid.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Fighter(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitFighter()
        textures = 'src/sprites/Fighter.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Monk(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitMonk()
        textures = 'src/sprites/Monk.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Paladin(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitPaladin()
        textures = 'src/sprites/Paladin.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Ranger(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitRanger()
        textures = 'src/sprites/Ranger.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Rogue(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitRogue()
        textures = 'src/sprites/Rogue.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Sorcerer(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitSorcerer()
        textures = 'src/sprites/Sorcerer.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Warlock(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitWarlock()
        textures = 'src/sprites/Warlock.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


class Wizard(Figure):

    def __init__(
        self,
        domain: "Domain",
        index: tuple[int, int],
    ):
        unit = UnitWizard()
        textures = 'src/sprites/Wizard.png'
        super().__init__(
            domain=domain,
            textures=textures,
            index=index,
            unit=unit,
        )


def get_figures_position() -> dict[tuple[int, int], Type[Figure]]:
    figures_position: dict[tuple[int, int], Type[Figure]] = {}
    for row in range(1, 8):
        for column in range(1, 7):
            index = (row, column)
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
