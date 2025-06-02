from typing import TYPE_CHECKING

from src.models.perk import Elemental
from src.items.spells import (
    DivineSmite,
    FireBall,
    FaerieTale,
    IceStorm,
    ShadowBlade,
    MagicMissile,
)

if TYPE_CHECKING:
    from src.abstractions.unit import BaseUnit


class UseDivineSmite(Elemental):
    """Способность - использовать заклинание Божественная Кара"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseDivineSmite",
            spell=DivineSmite(),
            person=person,
            texture_path='src/sprites/perks/slice-orange-3.png',
        )


class UseFireBall(Elemental):
    """Способность - использовать заклинание Огненный Шар"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFireBall",
            spell=FireBall(),
            person=person,
            texture_path='src/sprites/perks/fireball-red-2.png',
        )


class UseFaerieTale(Elemental):
    """Способность - использовать заклинание Сказка Феи"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFaerieTale",
            spell=FaerieTale(),
            person=person,
            texture_path='src/sprites/perks/horror-eerie-3.png',
        )


class UseIceStorm(Elemental):
    """Способность - использовать заклинание Ледяной Шторм"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseIceStorm",
            spell=IceStorm(),
            person=person,
            texture_path='src/sprites/perks/ice-blue-3.png',
        )


class UseShadowBlade(Elemental):
    """Способность - использовать заклинание Теневой Клинок"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseShadowBlade",
            spell=ShadowBlade(),
            person=person,
            texture_path='src/sprites/perks/enchant-magenta-3.png',
        )


class UseMagicMissile(Elemental):
    """Способность - использовать заклинание Магический Снаряд"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseMagicMissile",
            spell=MagicMissile(),
            person=person,
            texture_path='src/sprites/perks/fire-arrows-magenta-3.png',
        )
