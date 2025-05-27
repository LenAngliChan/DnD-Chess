from typing import TYPE_CHECKING

from src.models.perk import Elemental, Armor, PerkCombination
from src.perks.melee import AttackWithSwordBastard
from src.perks.elemental import UseDivineSmite
from src.utils.enums import PerkType

from src.items.spells import (
    HealingHand,
)

if TYPE_CHECKING:
    from src.abstractions.unit import BasicUnit
    from src.abstractions.item import BasicItem


class UseHealingHand(Elemental):
    """Способность - использовать исцеление"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseHealingHand",
            spell=HealingHand(),
            person=person,
            attribute=PerkType.heal.value,
        )


class UseDefendStand(Armor):
    """Способность - использовать защитную стойку"""

    def __init__(
        self,
        person: "BasicUnit",
        shield: "BasicItem"
    ):
        super().__init__(
            name="UseDefendStand",
            shield=shield,
            person=person,
            attribute=PerkType.shield.value,
        )


class AttackWithSwordBySpell(PerkCombination):
    """Способность - использовать комбинацию (меч + заклинание)"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithSwordBySpell",
            main_perk=AttackWithSwordBastard(person=person),
            effects=[UseDivineSmite(person=person)],
        )
