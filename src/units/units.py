from src.models.unit import Unit
from src.utils.characters import (
    barbarian,
    bard,
    cleric,
    druid,
    fighter,
    monk,
    paladin,
    ranger,
    rogue,
    sorcerer,
    warlock,
    wizard,
)
from models.collection import PerkCollection
from src.perks.active import UseHealingHand, AttackWithSwordBySpell, UseDefendStand
from src.perks.melee import (
    AttackWithTwoDaggers,
    AttackWithSwordOH,
    AttackWithSwordTH,
    AttackWithAxe,
    AttackWithBow,
    AttackWithFists,
)
from src.perks.elemental import (
    UseFireBall,
    UseFaerieTale,
    UseIceStorm,
    UseShadowBlade,
)
from src.items.armors import MediumShield


class UnitBarbarian(Unit):

    def __init__(self):
        main_action = AttackWithAxe(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Barbarian",
            character=barbarian,
            perks=perks,
        )


class UnitBard(Unit):

    def __init__(self):
        main_action = UseFaerieTale(person=self)
        second_action = AttackWithSwordOH(person=self)
        perks = PerkCollection(perks=[main_action, second_action])
        super().__init__(
            name="Bard",
            character=bard,
            perks=perks,
        )


class UnitCleric(Unit):

    def __init__(self):
        main_action = UseHealingHand(person=self)
        second_action = AttackWithSwordOH(person=self)
        third_action = UseDefendStand(
            person=self,
            shield=MediumShield(),
        )
        perks = PerkCollection(perks=[main_action, second_action, third_action])
        super().__init__(
            name="Cleric",
            character=cleric,
            perks=perks,
        )


class UnitDruid(Unit):

    def __init__(self):
        main_action = UseFaerieTale(person=self)
        second_action = AttackWithSwordOH(person=self)
        third_action = UseHealingHand(person=self)
        perks = PerkCollection(perks=[main_action, second_action, third_action])
        super().__init__(
            name="Druid",
            character=druid,
            perks=perks,
        )


class UnitFighter(Unit):

    def __init__(self):
        main_action = AttackWithSwordTH(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Fighter",
            character=fighter,
            perks=perks,
        )


class UnitMonk(Unit):

    def __init__(self):
        main_action = AttackWithFists(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Monk",
            character=monk,
            perks=perks,
        )


class UnitPaladin(Unit):

    def __init__(self):
        main_action = AttackWithSwordBySpell(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Paladin",
            character=paladin,
            perks=perks,
        )


class UnitRanger(Unit):

    def __init__(self):
        main_action = AttackWithBow(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Ranger",
            character=ranger,
            perks=perks,
        )


class UnitRogue(Unit):

    def __init__(self):
        main_action = AttackWithTwoDaggers(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Rogue",
            character=rogue,
            perks=perks,
        )


class UnitSorcerer(Unit):

    def __init__(self):
        main_action = UseFireBall(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Sorcerer",
            character=sorcerer,
            perks=perks,
        )


class UnitWarlock(Unit):

    def __init__(self):
        main_action = UseShadowBlade(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Warlock",
            character=warlock,
            perks=perks,
        )


class UnitWizard(Unit):

    def __init__(self):
        main_action = UseIceStorm(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name="Wizard",
            character=wizard,
            perks=perks,
        )
