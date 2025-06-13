from models.item import Spell
from src.utils.enums import MagicType
from src.models.effect import Elemental, Heal, Sacrifice


class DivineSmite(Spell):

    def __init__(self):
        effect = Elemental(
            name="DivineSmite",
            title="Божественная Кара",
            item=self,
        )
        super().__init__(
            name="DivineSmite",
            title="Божественная Кара",
            effect=effect,
            damage=6,
            magic_type=MagicType.radiant.value,
        )


class FireBall(Spell):

    def __init__(self):
        effect = Elemental(
            name="FireBall",
            title="Огненный Шар",
            item=self,
        )
        super().__init__(
            name="FireBall",
            title="Огненный Шар",
            effect=effect,
            damage=8,
            magic_type=MagicType.fire.value,
            radius=2,
        )


class FaerieTale(Spell):

    def __init__(self):
        effect = Elemental(
            name="FaerieTale",
            title="Сказка Феи",
            item=self,
        )
        super().__init__(
            name="FaerieTale",
            title="Сказка Феи",
            effect=effect,
            damage=8,
            magic_type=MagicType.psychic.value,
        )


class IceStorm(Spell):

    def __init__(self):
        effect = Elemental(
            name="IceStorm",
            title="Ледяной Шторм",
            item=self,
        )
        super().__init__(
            name="IceStorm",
            title="Ледяной Шторм",
            effect=effect,
            damage=8,
            magic_type=MagicType.ice.value,
            radius=2,
        )


class ShadowBlade(Spell):

    def __init__(self):
        effect = Elemental(
            name="ShadowBlade",
            title="Теневой Клинок",
            item=self,
        )
        super().__init__(
            name="ShadowBlade",
            title="Теневой Клинок",
            effect=effect,
            damage=6,
            magic_type=MagicType.dark.value,
        )


class MagicMissile(Spell):

    def __init__(self):
        effect = Elemental(
            name="MagicMissile",
            title="Магический Снаряд",
            item=self,
        )
        super().__init__(
            name="MagicMissile",
            title="Магический Снаряд",
            effect=effect,
            damage=8,
            magic_type=MagicType.force.value,
            radius=2,
        )


class HealingHand(Spell):

    def __init__(self):
        effect = Heal(
            name="HealingHand",
            title="Исцеление",
            item=self,
        )
        super().__init__(
            name="HealingHand",
            title="Исцеление",
            effect=effect,
            damage=8,
            magic_type=MagicType.force.value,
        )


class SacrificeEnemy(Spell):

    def __init__(self):
        effect = Sacrifice(
            name="SacrificeEnemy",
            title="Пожертвовать",
            item=self,
        )
        super().__init__(
            name="SacrificeEnemy",
            title="Пожертвовать",
            effect=effect,
            damage=1,
            magic_type=MagicType.force.value,
        )
