from models.item import Spell
from src.utils.enums import MagicType


class DivineSmite(Spell):

    def __init__(self):
        super().__init__(
            name="DivineSmite",
            title="Божественная Кара",
            damage=6,
            magic_type=MagicType.radiant.value,
        )


class FireBall(Spell):

    def __init__(self):
        super().__init__(
            name="FireBall",
            title="Огненный Шар",
            damage=8,
            magic_type=MagicType.fire.value,
        )


class FaerieTale(Spell):

    def __init__(self):
        super().__init__(
            name="FaerieTale",
            title="Сказка Феи",
            damage=8,
            magic_type=MagicType.psychic.value,
        )


class IceStorm(Spell):

    def __init__(self):
        super().__init__(
            name="IceStorm",
            title="Ледяной Шторм",
            damage=8,
            magic_type=MagicType.ice.value,
        )


class ShadowBlade(Spell):

    def __init__(self):
        super().__init__(
            name="ShadowBlade",
            title="Теневой Клинок",
            damage=6,
            magic_type=MagicType.dark.value,
        )


class MagicMissile(Spell):

    def __init__(self):
        super().__init__(
            name="MagicMissile",
            title="Магический Снаряд",
            damage=8,
            magic_type=MagicType.force.value,
        )


class HealingHand(Spell):

    def __init__(self):
        super().__init__(
            name="HealingHand",
            title="Исцеление",
            damage=8,
            magic_type=MagicType.radiant.value,
        )
