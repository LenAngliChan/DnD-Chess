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
    from src.abstractions.unit import BasicUnit


class UseDivineSmite(Elemental):
    """Способность - использовать заклинание Божественная Кара"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseDivineSmite",
            spell=DivineSmite(),
            person=person,
        )


class UseFireBall(Elemental):
    """Способность - использовать заклинание Огненный Шар"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseFireBall",
            spell=FireBall(),
            person=person,
        )


class UseFaerieTale(Elemental):
    """Способность - использовать заклинание Сказка Феи"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseFaerieTale",
            spell=FaerieTale(),
            person=person,
        )


class UseIceStorm(Elemental):
    """Способность - использовать заклинание Ледяной Шторм"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseIceStorm",
            spell=IceStorm(),
            person=person,
        )


class UseShadowBlade(Elemental):
    """Способность - использовать заклинание Теневой Клинок"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseShadowBlade",
            spell=ShadowBlade(),
            person=person,
        )


class UseMagicMissile(Elemental):
    """Способность - использовать заклинание Магический Снаряд"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="UseMagicMissile",
            spell=MagicMissile(),
            person=person,
        )
