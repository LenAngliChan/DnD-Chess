from typing import TYPE_CHECKING

from src.models.perk import Elemental, Armor, PerkCombination
from src.perks.melee import AttackWithSwordBastard
from src.perks.elemental import UseDivineSmite
from src.utils.enums import PerkType, ArmorType

from src.items.spells import (
    HealingHand,
)

if TYPE_CHECKING:
    from src.abstractions.unit import BaseUnit
    from src.abstractions.item import BaseItem


class UseHealingHand(Elemental):
    """Способность - использовать исцеление"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseHealingHand",
            spell=HealingHand(),
            person=person,
            attribute=PerkType.heal.value,
            texture_path='src/sprites/perks/heal-jade-3.png',
        )


class UseDefendStand(Armor):
    """Способность - использовать защитную стойку"""

    def __init__(
        self,
        person: "BaseUnit",
        shield: "BaseItem"
    ):
        if shield.attribute == ArmorType.light_shield.value:
            texture_path = 'src/sprites/perks/protect-sky-1.png'
        elif shield.attribute == ArmorType.medium_shield.value:
            texture_path = 'src/sprites/perks/protect-sky-2.png'
        else:
            texture_path = 'src/sprites/perks/protect-sky-3.png'
        super().__init__(
            name="UseDefendStand",
            shield=shield,
            person=person,
            attribute=PerkType.shield.value,
            texture_path=texture_path,
        )


class AttackWithSwordBySpell(PerkCombination):
    """Способность - использовать комбинацию (меч + заклинание)"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithSwordBySpell",
            main_perk=AttackWithSwordBastard(
                person=person,
                texture_path='src/sprites/perks/w_longsword_gold.png',
            ),
            effects=[UseDivineSmite(person=person)],
        )
