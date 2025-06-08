from typing import TYPE_CHECKING, Type

from src.models.figure import Figure
from src.utils.tools import Index
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
from src.utils.characters import (
    barbarian,
    bard,
    cleric,
    druid,
    fighter,
    monk,
    paladin,
    ranger,
    rogue,
    sorcerer,
    warlock,
    wizard,
)

if TYPE_CHECKING:
    from src.models.domain import Domain


class Barbarian(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitBarbarian(
            name=barbarian.name,
            title=barbarian.title,
            description=barbarian.description,
            characteristic=barbarian.characteristic,
        )
        texture = barbarian.textures.day if domain.name == "Red" else barbarian.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Bard(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitBard(
            name=bard.name,
            title=bard.title,
            description=bard.description,
            characteristic=bard.characteristic,
        )
        texture = bard.textures.day if domain.name == "Red" else bard.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Cleric(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitCleric(
            name=cleric.name,
            title=cleric.title,
            description=cleric.description,
            characteristic=cleric.characteristic,
        )
        texture = cleric.textures.day if domain.name == "Red" else cleric.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Druid(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitDruid(
            name=druid.name,
            title=druid.title,
            description=druid.description,
            characteristic=druid.characteristic,
        )
        texture = druid.textures.day if domain.name == "Red" else druid.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Fighter(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitFighter(
            name=fighter.name,
            title=fighter.title,
            description=fighter.description,
            characteristic=fighter.characteristic,
        )
        texture = fighter.textures.day if domain.name == "Red" else fighter.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Monk(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitMonk(
            name=monk.name,
            title=monk.title,
            description=monk.description,
            characteristic=monk.characteristic,
        )
        texture = monk.textures.day if domain.name == "Red" else monk.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Paladin(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitPaladin(
            name=paladin.name,
            title=paladin.title,
            description=paladin.description,
            characteristic=paladin.characteristic,
        )
        texture = paladin.textures.day if domain.name == "Red" else paladin.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Ranger(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitRanger(
            name=ranger.name,
            title=ranger.title,
            description=ranger.description,
            characteristic=ranger.characteristic,
        )
        texture = ranger.textures.day if domain.name == "Red" else ranger.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Rogue(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitRogue(
            name=rogue.name,
            title=rogue.title,
            description=rogue.description,
            characteristic=rogue.characteristic,
        )
        texture = rogue.textures.day if domain.name == "Red" else rogue.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Sorcerer(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitSorcerer(
            name=sorcerer.name,
            title=sorcerer.title,
            description=sorcerer.description,
            characteristic=sorcerer.characteristic,
        )
        texture = sorcerer.textures.day if domain.name == "Red" else sorcerer.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Warlock(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitWarlock(
            name=warlock.name,
            title=warlock.title,
            description=warlock.description,
            characteristic=warlock.characteristic,
        )
        texture = warlock.textures.day if domain.name == "Red" else warlock.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


class Wizard(Figure):

    def __init__(
        self,
        index: Index,
        domain: "Domain",
    ):
        unit = UnitWizard(
            name=wizard.name,
            title=wizard.title,
            description=wizard.description,
            characteristic=wizard.characteristic,
        )
        texture = wizard.textures.day if domain.name == "Red" else wizard.textures.night
        super().__init__(
            index=index,
            domain=domain,
            texture=texture,
            unit=unit,
        )


def get_figures_position() -> dict[str, Type[Figure]]:
    figures_position: dict[str, Type[Figure]] = {}
    for row in range(1, 8):
        for column in range(1, 7):
            index = Index(row=row, column=column)
            if row in (1, 7):
                if column == 1:
                    figures_position[index.name] = Druid
                elif column == 2:
                    figures_position[index.name] = Bard
                elif column == 3:
                    figures_position[index.name] = Sorcerer
                elif column == 4:
                    figures_position[index.name] = Wizard
                elif column == 5:
                    figures_position[index.name] = Warlock
                else:
                    figures_position[index.name] = Cleric
            if row in (2, 6):
                if column == 1:
                    figures_position[index.name] = Ranger
                elif column == 2:
                    figures_position[index.name] = Monk
                elif column == 3:
                    figures_position[index.name] = Fighter
                elif column == 4:
                    figures_position[index.name] = Barbarian
                elif column == 5:
                    figures_position[index.name] = Paladin
                else:
                    figures_position[index.name] = Rogue

    return figures_position
