from typing import TYPE_CHECKING

from src.models.figure import Figure
from src.units.units import (
    UnitBarbarian,
    UnitCleric,
    UnitWarlock,
    UnitMonk,
)
from src.utils.characters import (
    barbarian,
    cleric,
    warlock,
    monk,
)

if TYPE_CHECKING:
    from src.abstractions.domain import BaseDomain
    from src.utils.tools import Index


class TestBarbarian(Figure):

    def __init__(
        self,
        index: "Index",
        domain: "BaseDomain",
    ):
        barbarian.characteristic.base_hit_points = 1000
        barbarian.characteristic.base_hit_chance = 1000
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


class TestCleric(Figure):

    def __init__(
        self,
        index: "Index",
        domain: "BaseDomain",
    ):
        cleric.characteristic.charisma = 1000
        cleric.characteristic.base_hit_points = 1000
        cleric.characteristic.base_hit_chance = 1000
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


class TestWarlock(Figure):

    def __init__(
        self,
        index: "Index",
        domain: "BaseDomain",
    ):
        warlock.characteristic.base_hit_points = 1000
        warlock.characteristic.base_hit_chance = 1000
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


class TestMonkey(Figure):

    def __init__(
        self,
        index: "Index",
        name: str,
        domain: "BaseDomain",
    ):
        unit = UnitMonk(
            name=name,
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
