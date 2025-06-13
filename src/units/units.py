from typing import TYPE_CHECKING

from src.models.unit import Unit
from models.collection import PerkCollection
from src.items.armors import MediumShield, GreatShield
from src.perks.active import (
    UseHealingHand,
    AttackWithSwordBySpell,
    UseDefendStand,
)
from src.perks.melee import (
    AttackWithTwoDaggers,
    AttackWithDagger,
    AttackWithSwordOH,
    AttackWithSwordBastard,
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
    UseBearPaws,
    UseMagicMissile,
    UseDivineSmite,
    UseFireStorm,
)

if TYPE_CHECKING:
    from src.utils.tools import Characteristic


class UnitBarbarian(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = AttackWithAxe(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitBard(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = UseFaerieTale(person=self)
        second_action = AttackWithSwordOH(person=self)
        perks = PerkCollection(perks=[main_action, second_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitCleric(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = UseHealingHand(person=self)
        second_action = AttackWithSwordOH(person=self)
        third_action = UseDivineSmite(person=self)
        fourth_action = UseDefendStand(
            person=self,
            shield=GreatShield(),
        )
        perks = PerkCollection(
            perks=[
                main_action, second_action, third_action, fourth_action
            ]
        )
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitDruid(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = UseBearPaws(person=self)
        second_action = UseHealingHand(person=self)
        perks = PerkCollection(perks=[main_action, second_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitFighter(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = AttackWithSwordTH(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitMonk(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = AttackWithFists(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitPaladin(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = AttackWithSwordBySpell(person=self)
        second_action = UseDefendStand(
            person=self,
            shield=MediumShield(),
        )
        perks = PerkCollection(perks=[main_action, second_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitRanger(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = AttackWithBow(person=self)
        second_action = AttackWithSwordBastard(person=self)
        perks = PerkCollection(perks=[main_action, second_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitRogue(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = AttackWithTwoDaggers(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitSorcerer(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = UseFireBall(person=self)
        second_action = UseFireStorm(person=self)
        third_action = AttackWithDagger(person=self)
        perks = PerkCollection(perks=[main_action, second_action, third_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitWarlock(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = UseShadowBlade(person=self)
        perks = PerkCollection(perks=[main_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )


class UnitWizard(Unit):

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
    ):
        main_action = UseIceStorm(person=self)
        second_action = UseMagicMissile(person=self)
        third_action = AttackWithDagger(person=self)
        perks = PerkCollection(perks=[main_action, second_action, third_action])
        super().__init__(
            name=name,
            title=title,
            description=description,
            characteristic=characteristic,
            perks=perks,
        )
