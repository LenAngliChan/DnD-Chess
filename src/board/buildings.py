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
        super().__init__(
            index=index,
            name="Castle",
            domain=domain,
            texture_path='src/sprites/buildings/Castle.png',
            defence_bonus=6,
            can_change_domain=False,
        )


class Crypt(Building):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        super().__init__(
            index=index,
            name="Crypt",
            domain=domain,
            texture_path='src/sprites/buildings/Crypt.png',
            defence_bonus=2,
        )


class Altar(Building):

    def __init__(
        self,
        index: tuple[int, int],
        domain: "Domain",
    ):
        super().__init__(
            index=index,
            name="Altar",
            domain=domain,
            texture_path='src/sprites/buildings/Altar.png',
            defence_bonus=4,
        )


def get_buildings_position() -> dict[tuple[int, int], Type[Building]]:

    buildings_position = {
        (3, 1): Castle,
        (4, 7): Castle,
        (1, 3): Altar,
        (6, 5): Altar,
        (1, 4): Crypt,
        (3, 4): Crypt,
        (4, 4): Crypt,
        (6, 4): Crypt
    }

    return buildings_position
