from src.models.perk import Passive
from src.utils.enums import PerkType
from src.utils.textures import (
    HEALING_HAND_TEXTURE,
    ALTAR_GIFT_TEXTURE,
)
from src.items.spells import (
    HealingHand,
    SacrificeEnemy,
)


class BuildingHealing(Passive):
    """Способность - исцеление от здания"""

    def __init__(self):
        super().__init__(
            name="BuildingHealing",
            title="Восстановление",
            item=HealingHand(),
            attribute=PerkType.heal.value,
            texture=HEALING_HAND_TEXTURE,
        )


class AltarGift(Passive):
    """Способность - дар алтаря"""

    def __init__(self):
        super().__init__(
            name="AltarGift",
            title="Священная жертва",
            item=SacrificeEnemy(),
            attribute=PerkType.effect.value,
            texture=ALTAR_GIFT_TEXTURE,
        )
