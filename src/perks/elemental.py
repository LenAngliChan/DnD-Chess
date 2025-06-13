from typing import TYPE_CHECKING

from src.models.perk import Magic
from src.utils.textures import (
    D_S_SPELL_TEXTURE,
    F_B_SPELL_TEXTURE,
    F_T_SPELL_TEXTURE,
    I_S_SPELL_TEXTURE,
    S_B_SPELL_TEXTURE,
    M_M_SPELL_TEXTURE,
)
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


class UseDivineSmite(Magic):
    """Способность - использовать заклинание Божественная Кара"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseDivineSmite",
            title="Заклинание",
            spell=DivineSmite(),
            person=person,
            texture=D_S_SPELL_TEXTURE,
        )


class UseFireBall(Magic):
    """Способность - использовать заклинание Огненный Шар"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFireBall",
            title="Заклинание",
            spell=FireBall(),
            person=person,
            texture=F_B_SPELL_TEXTURE,
        )


class UseFaerieTale(Magic):
    """Способность - использовать заклинание Сказка Феи"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseFaerieTale",
            title="Заклинание",
            spell=FaerieTale(),
            person=person,
            texture=F_T_SPELL_TEXTURE,
        )


class UseIceStorm(Magic):
    """Способность - использовать заклинание Ледяной Шторм"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseIceStorm",
            title="Заклинание",
            spell=IceStorm(),
            person=person,
            texture=I_S_SPELL_TEXTURE,
        )


class UseShadowBlade(Magic):
    """Способность - использовать заклинание Теневой Клинок"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseShadowBlade",
            title="Заклинание",
            spell=ShadowBlade(),
            person=person,
            texture=S_B_SPELL_TEXTURE,
        )


class UseMagicMissile(Magic):
    """Способность - использовать заклинание Магический Снаряд"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="UseMagicMissile",
            title="Заклинание",
            spell=MagicMissile(),
            person=person,
            texture=M_M_SPELL_TEXTURE,
        )
