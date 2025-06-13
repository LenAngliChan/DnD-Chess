from typing import TYPE_CHECKING

from src.models.perk import Magic
from src.utils.textures import (
    DIVINE_SMITE_TEXTURE,
    FIRE_BALL_TEXTURE,
    FAERY_TALE_TEXTURE,
    ICE_STORM_TEXTURE,
    SHADOW_BLADE_TEXTURE,
    MAGIC_MISSILE_TEXTURE,
    BEAR_PAWS_TEXTURE,
    FIRE_STORM_TEXTURE,
)
from src.items.spells import (
    DivineSmite,
    FireBall,
    FaerieTale,
    IceStorm,
    ShadowBlade,
    MagicMissile,
    BearPaws,
    FireStorm,
)

if TYPE_CHECKING:
    from src.abstractions.unit import BaseUnit


class UseDivineSmite(Magic):
    """Способность - использовать заклинание Божественная Кара"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseDivineSmite",
            title="Заклинание",
            spell=DivineSmite(),
            person=person,
            texture=DIVINE_SMITE_TEXTURE,
        )


class UseFireBall(Magic):
    """Способность - использовать заклинание Огненный Шар"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFireBall",
            title="Заклинание",
            spell=FireBall(),
            person=person,
            texture=FIRE_BALL_TEXTURE,
        )


class UseFaerieTale(Magic):
    """Способность - использовать заклинание Сказка Феи"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFaerieTale",
            title="Заклинание",
            spell=FaerieTale(),
            person=person,
            texture=FAERY_TALE_TEXTURE,
        )


class UseIceStorm(Magic):
    """Способность - использовать заклинание Ледяной Шторм"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseIceStorm",
            title="Заклинание",
            spell=IceStorm(),
            person=person,
            texture=ICE_STORM_TEXTURE,
        )


class UseShadowBlade(Magic):
    """Способность - использовать заклинание Теневой Клинок"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseShadowBlade",
            title="Заклинание",
            spell=ShadowBlade(),
            person=person,
            texture=SHADOW_BLADE_TEXTURE,
        )


class UseMagicMissile(Magic):
    """Способность - использовать заклинание Магический Снаряд"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseMagicMissile",
            title="Заклинание",
            spell=MagicMissile(),
            person=person,
            texture=MAGIC_MISSILE_TEXTURE,
        )


class UseBearPaws(Magic):
    """Способность - использовать заклинание Гнев Природы"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseBearPaws",
            title="Заклинание",
            spell=BearPaws(),
            person=person,
            texture=BEAR_PAWS_TEXTURE,
        )


class UseFireStorm(Magic):
    """Способность - использовать заклинание Огненный Шторм"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFireStorm",
            title="Заклинание",
            spell=FireStorm(),
            person=person,
            texture=FIRE_STORM_TEXTURE,
        )
