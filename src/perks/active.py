from typing import TYPE_CHECKING

from src.models.perk import Magic, Armor, PerkCombination
from src.perks.melee import AttackWithSwordBastard
from src.perks.elemental import UseDivineSmite
from src.utils.enums import PerkType, ArmorType
from src.utils.textures import (
    HEALING_HAND_TEXTURE,
    LIGHT_SHIELD_TEXTURE,
    MEDIUM_SHIELD_TEXTURE,
    GREAT_SHIELD_TEXTURE,
    DS_SWORD_TEXTURE,
)
from src.items.spells import (
    HealingHand,
)

if TYPE_CHECKING:
    from src.abstractions.unit import BaseUnit
    from src.abstractions.item import BaseItem


class UseHealingHand(Magic):
    """Способность - использовать исцеление"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseHealingHand",
            title="Исцеляющее Касание",
            spell=HealingHand(),
            person=person,
            attribute=PerkType.heal.value,
            texture=HEALING_HAND_TEXTURE,
        )


class UseDefendStand(Armor):
    """Способность - использовать защитную стойку"""

    def __init__(
        self,
        person: "BaseUnit",
        shield: "BaseItem"
    ):
        if shield.attribute == ArmorType.light_shield.value:
            texture = LIGHT_SHIELD_TEXTURE
        elif shield.attribute == ArmorType.medium_shield.value:
            texture = MEDIUM_SHIELD_TEXTURE
        else:
            texture = GREAT_SHIELD_TEXTURE
        super().__init__(
            name="UseDefendStand",
            title="Защитная Стойка",
            shield=shield,
            person=person,
            attribute=PerkType.shield.value,
            texture=texture,
        )


class AttackWithSwordBySpell(PerkCombination):
    """Способность - использовать комбинацию (меч + заклинание)"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithSwordBySpell",
            main_perk=AttackWithSwordBastard(
                person=person,
                texture=DS_SWORD_TEXTURE,
            ),
            other_perks=[UseDivineSmite(person=person)],
        )
