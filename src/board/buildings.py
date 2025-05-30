from typing import TYPE_CHECKING, Type

from src.models.building import Building

if TYPE_CHECKING:
    from src.models.domain import Domain


class Castle(Building):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        name = "Castle"
        textures = 'src/sprites/buildings/Castle.png'
        super().__init__(
            index=index,
            name=name,
            domain=domain,
            textures=textures,
            defence_bonus=6,
            can_change_domain=False,
        )


class Crypt(Building):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        name = "Crypt"
        textures = 'src/sprites/buildings/Crypt.png'
        super().__init__(
            index=index,
            name=name,
            domain=domain,
            textures=textures,
            defence_bonus=2,
        )


class Altar(Building):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        name = "Altar"
        textures = 'src/sprites/buildings/Altar.png'
        super().__init__(
            index=index,
            name=name,
            domain=domain,
            textures=textures,
            defence_bonus=4,
        )


def get_buildings_position() -> dict[tuple[int, int], Type[Building]]:

    buildings_position = {
        (1, 3): Castle,
        (7, 4): Castle,
        (3, 1): Altar,
        (5, 6): Altar,
        (4, 1): Crypt,
        (4, 3): Crypt,
        (4, 4): Crypt,
        (4, 6): Crypt
    }

    return buildings_position
