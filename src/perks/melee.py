from typing import TYPE_CHECKING

from src.models.perk import Melee
from src.utils.enums import PerkType
from src.utils.textures import (
    DAGGER_TEXTURE,
    TWO_DAGGERS_TEXTURE,
    SWORD_OH_TEXTURE,
    SWORD_BASTARD_TEXTURE,
    SWORD_TH_TEXTURE,
    AXE_TEXTURE,
    BOW_TEXTURE,
    FISTS_TEXTURE,
)
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
    from arcade import Texture
    from src.abstractions.unit import BaseUnit


class AttackWithDagger(Melee):
    """Способность - использовать оружие Кинжал"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithDagger",
            title="Взмах",
            weapon=Dagger(),
            person=person,
            texture=DAGGER_TEXTURE,
        )


class AttackWithTwoDaggers(Melee):
    """Способность - использовать оружие Два Кинжала"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithTwoDaggers",
            title="Двойной Укол",
            weapon=TwoDaggers(),
            person=person,
            texture=TWO_DAGGERS_TEXTURE,
        )


class AttackWithSwordOH(Melee):
    """Способность - использовать оружие Одноручный Меч"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithSwordOH",
            title="Удар",
            weapon=SwordOH(),
            person=person,
            texture=SWORD_OH_TEXTURE,
        )


class AttackWithSwordBastard(Melee):
    """Способность - использовать оружие Полуторный Меч"""

    def __init__(
        self,
        person: "BaseUnit",
        texture: "Texture" = SWORD_BASTARD_TEXTURE,
    ):
        super().__init__(
            name="AttackWithSwordBastard",
            title="Сильный Удар",
            weapon=SwordBastard(),
            person=person,
            texture=texture,
        )


class AttackWithSwordTH(Melee):
    """Способность - использовать оружие Двуручный Меч"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithSwordTH",
            title="Сильный Удар",
            weapon=SwordTH(),
            person=person,
            texture=SWORD_TH_TEXTURE,
        )


class AttackWithAxe(Melee):
    """Способность - использовать оружие Топор"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithAxe",
            title="Сильный Удар",
            weapon=Axe(),
            person=person,
            texture=AXE_TEXTURE,
        )


class AttackWithBow(Melee):
    """Способность - использовать оружие Лук
    По механике аналогичен оружию ближнего боя, но можно атаковать с соседней клетки
    """

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithBow",
            title="Выстрел",
            weapon=Bow(),
            person=person,
            attribute=PerkType.ranged.value,
            texture=BOW_TEXTURE,
        )


class AttackWithFists(Melee):
    """Способность - использовать оружие Кулаки"""

    def __init__(self, person: "BaseUnit"):
        super().__init__(
            name="AttackWithFists",
            title="Техника Пьяного Мастера",
            weapon=Fists(),
            person=person,
            texture=FISTS_TEXTURE,
        )
