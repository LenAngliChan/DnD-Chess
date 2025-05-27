from models.item import Spell
from src.utils.enums import MagicType


class DivineSmite(Spell):

    def __init__(self):
        super().__init__(
            name="DivineSmite",
            damage=6,
            magic_type=MagicType.radiant.value,
        )


class FireBall(Spell):

    def __init__(self):
        super().__init__(
            name="FireBall",
            damage=8,
            magic_type=MagicType.fire.value,
        )


class FaerieTale(Spell):

    def __init__(self):
        super().__init__(
            name="FaerieTale",
            damage=8,
            magic_type=MagicType.psychic.value,
        )


class IceStorm(Spell):

    def __init__(self):
        super().__init__(
            name="IceStorm",
            damage=8,
            magic_type=MagicType.ice.value,
        )


class ShadowBlade(Spell):

    def __init__(self):
        super().__init__(
            name="ShadowBlade",
            damage=6,
            magic_type=MagicType.dark.value,
        )


class MagicMissile(Spell):

    def __init__(self):
        super().__init__(
            name="MagicMissile",
            damage=8,
            magic_type=MagicType.force.value,
        )


class HealingHand(Spell):

    def __init__(self):
        super().__init__(
            name="HealingHand",
            damage=8,
            magic_type=MagicType.radiant.value,
        )
