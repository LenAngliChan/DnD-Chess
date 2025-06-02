from typing import TYPE_CHECKING

from src.models.perk import Melee
from src.utils.enums import PerkType
from src.items.weapons import (
    Dagger,
    TwoDaggers,
    SwordOH,
    SwordBastard,
    SwordTH,
    Axe,
    Bow,
    Fists,
)

if TYPE_CHECKING:
    from src.abstractions.unit import BaseUnit


class AttackWithDagger(Melee):
    """Способность - использовать оружие Кинжал"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithDagger",
            weapon=Dagger(),
            person=person,
            texture_path='src/sprites/perks/w_dagger_steel.png',
        )


class AttackWithTwoDaggers(Melee):
    """Способность - использовать оружие Два Кинжала"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithTwoDaggers",
            weapon=TwoDaggers(),
            person=person,
            texture_path='src/sprites/perks/w_dagger_gold.png',
        )


class AttackWithSwordOH(Melee):
    """Способность - использовать оружие Одноручный Меч"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithSwordOH",
            weapon=SwordOH(),
            person=person,
            texture_path='src/sprites/perks/w_shortsword_steel.png',
        )


class AttackWithSwordBastard(Melee):
    """Способность - использовать оружие Полуторный Меч"""

    def __init__(
        self,
        person: "BaseUnit",
        texture_path: str = 'src/sprites/perks/w_longsword_steel.png',
    ):
        super().__init__(
            name="AttackWithSwordBastard",
            weapon=SwordBastard(),
            person=person,
            texture_path=texture_path,
        )


class AttackWithSwordTH(Melee):
    """Способность - использовать оружие Двуручный Меч"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithSwordTH",
            weapon=SwordTH(),
            person=person,
            texture_path='src/sprites/perks/w_broadsword_steel.png',
        )


class AttackWithAxe(Melee):
    """Способность - использовать оружие Топор"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithAxe",
            weapon=Axe(),
            person=person,
            texture_path='src/sprites/perks/w_axe_war_steel.png',
        )


class AttackWithBow(Melee):
    """Способность - использовать оружие Лук
    По механике аналогичен оружию ближнего боя, но можно атаковать с соседней клетки
    """

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithBow",
            weapon=Bow(),
            person=person,
            attribute=PerkType.ranged.value,
            texture_path='src/sprites/perks/archer.png',
        )


class AttackWithFists(Melee):
    """Способность - использовать оружие Кулаки"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithFists",
            weapon=Fists(),
            person=person,
            texture_path='src/sprites/perks/wind-grasp-air-1.png',
        )
