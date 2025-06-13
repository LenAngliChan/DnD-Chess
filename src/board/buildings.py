from typing import TYPE_CHECKING, Type

from src.models.building import Building
from src.utils.tools import Index
from src.models.action import BuildingAction
from src.perks.passive import BuildingHealing, AltarGift
from src.utils.enums import ActionType
from src.utils.descriptions import ALTAR_DESC, CRYPT_DESC, CASTLE_DESC
from src.utils.textures import ALTAR_TEXTURE, CASTLE_TEXTURE, CRYPT_TEXTURE

if TYPE_CHECKING:
    from src.abstractions.domain import BaseDomain


class Castle(Building):

    def __init__(
        self,
        index: Index,
        domain: "BaseDomain",
    ):
        perk = BuildingHealing()
        action = BuildingAction(
            name=perk.name + "_" + "Action",
            texture=perk.texture,
            attribute=ActionType.only_building.value,
            perk=perk,
        )
        super().__init__(
            index=index,
            domain=domain,
            action=action,
            name="Castle",
            title="Замок",
            description=CASTLE_DESC,
            texture=CASTLE_TEXTURE,
            defence_bonus=6,
            can_change_domain=False,
        )


class Crypt(Building):

    def __init__(
        self,
        index: Index,
        domain: "BaseDomain",
    ):
        super().__init__(
            index=index,
            domain=domain,
            name="Crypt",
            title="Гробница",
            description=CRYPT_DESC,
            texture=CRYPT_TEXTURE,
            defence_bonus=2,
        )


class Altar(Building):

    def __init__(
        self,
        index: Index,
        domain: "BaseDomain",
    ):
        perk = AltarGift()
        action = BuildingAction(
            name=perk.name + "_" + "Action",
            texture=perk.texture,
            attribute=ActionType.sacrifice.value,
            perk=perk,
        )
        super().__init__(
            index=index,
            domain=domain,
            action=action,
            name="Altar",
            title="Алтарь",
            description=ALTAR_DESC,
            texture=ALTAR_TEXTURE,
            defence_bonus=4,
        )


def get_buildings_position() -> dict[str, Type[Building]]:

    buildings_position = {
        Index(row=1, column=3).name: Castle,
        Index(row=7, column=4).name: Castle,
        Index(row=3, column=1).name: Altar,
        Index(row=5, column=6).name: Altar,
        Index(row=5, column=1).name: Crypt,
        Index(row=3, column=3).name: Crypt,
        Index(row=3, column=4).name: Crypt,
        Index(row=3, column=6).name: Crypt
    }

    return buildings_position
