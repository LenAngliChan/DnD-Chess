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
    from src.abstractions.unit import BasicUnit


class AttackWithDagger(Melee):
    """Способность - использовать оружие Кинжал"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithDagger",
            weapon=Dagger(),
            person=person,
        )


class AttackWithTwoDaggers(Melee):
    """Способность - использовать оружие Два Кинжала"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithTwoDaggers",
            weapon=TwoDaggers(),
            person=person,
        )


class AttackWithSwordOH(Melee):
    """Способность - использовать оружие Одноручный Меч"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithSwordOH",
            weapon=SwordOH(),
            person=person,
        )


class AttackWithSwordBastard(Melee):
    """Способность - использовать оружие Полуторный Меч"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithSwordBastard",
            weapon=SwordBastard(),
            person=person,
        )


class AttackWithSwordTH(Melee):
    """Способность - использовать оружие Двуручный Меч"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithSwordTH",
            weapon=SwordTH(),
            person=person,
        )


class AttackWithAxe(Melee):
    """Способность - использовать оружие Топор"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithAxe",
            weapon=Axe(),
            person=person,
        )


class AttackWithBow(Melee):
    """Способность - использовать оружие Лук
    По механике аналогичен оружию ближнего боя, но можно атаковать с соседней клетки
    """

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithBow",
            weapon=Bow(),
            person=person,
            attribute=PerkType.ranged.value,
        )


class AttackWithFists(Melee):
    """Способность - использовать оружие Кулаки"""

    def __init__(self, person: "BasicUnit"):
        super().__init__(
            name="AttackWithFists",
            weapon=Fists(),
            person=person,
        )
