from typing import TYPE_CHECKING

from src.abstractions.unit import BaseAbility, BaseUnit
from src.utils.enums import WeaponType, MagicType
from models.dice import DiceRoll, DifficultyDice
from src.utils.constants import SAVE_THROW_DICE_SIDE

if TYPE_CHECKING:
    from src.abstractions.tools import BaseAttribute
    from src.models.collection import PerkCollection
    from src.utils.characters import Character


class Ability(BaseAbility):
    """Модель характеристик персонажа"""

    def __init__(
        self,
        character: "Character",
    ):
        """Инициализация характеристик персонажа

        Args:
            character: базовые характиристики персонажа
        """
        super().__init__(
            character=character,
        )
        dice = DifficultyDice(side=SAVE_THROW_DICE_SIDE)
        self.save_roll = DiceRoll(dice=dice)

    def save_throw(self, attribute: "BaseAttribute") -> int:
        """Спасбросок
        Рассчитывается как:
            базовый спасбросок (бросок кубика)
            + спасбросок по умению (бонус характеристики)

        Args:
            attribute: тип спасброска

        Returns:
            int: значение спасброска
        """

        # базовый спасбросок
        if isinstance(attribute, WeaponType):
            # против оружия нет бонусов
            value = 0
        elif attribute == MagicType.dark.value:
            # против магии тьмы не существует защиты
            value = 0
        else:
            # Против любых других заклинаний по умолчанию спасбросок d20, даже если это лечение
            value = self.save_roll.action()

        # спасбросок по умению
        if isinstance(attribute, WeaponType):
            # против оружия спасбросок по ловкости
            ability = self.dexterity
        elif attribute == MagicType.force.value:
            # против силовых заклинаний спасбросок по силе
            ability = self.strength
        elif attribute == MagicType.fire.value:
            # против огненных заклинаний спасбросок по ловкости
            ability = self.dexterity
        elif attribute == MagicType.ice.value:
            # против ледяных заклинаний спасбросок по выносливости
            ability = self.constitution
        elif attribute == MagicType.psychic.value:
            # против психических атак спасбросок по итнеллекту
            ability = self.intelligence
        elif attribute == MagicType.radiant.value:
            # против заклинаний света спасбросок по мудрости
            ability = self.wisdom
        else:
            ability = None

        if ability:
            value += self._ability_coefficient(value=ability)

        return value

    def mastery(self, attribute: "BaseAttribute" = None) -> int:
        """Мастерство
        Рассчитывается как:
            бонус характеристики

        Args:
            attribute: тип проверки на мастерство

        Returns:
            int: значение мастерства
        """

        # бонус мастерства
        if attribute == WeaponType.heavy.value:
            # мастерство тяжелым оружием зависит от силы
            ability = self.strength
        elif attribute == WeaponType.medium.value:
            # мастерство фехтовальным оружием зависит от силы или ловкости (смотря что больше)
            ability = max(self.dexterity, self.strength)
        elif attribute in (WeaponType.bow.value, WeaponType.light.value):
            # мастерство легким оружием зависит от ловкости
            ability = self.dexterity
        elif attribute in (MagicType.force.value, MagicType.dark.value):
            # мастерство магии силы и тьмы зависит от мудрости
            ability = self.wisdom
        elif attribute in (MagicType.fire.value, MagicType.ice.value):
            # мастерство магии огня и льда зависит от интеллекта
            ability = self.intelligence
        elif attribute in (MagicType.psychic.value, MagicType.radiant.value):
            # мастерство магии иллюзий и света зависит от харизмы
            ability = self.charisma
        else:
            # все остальное по умолнчанию - выносливости
            ability = self.constitution

        return self._ability_coefficient(value=ability)

    def _ability_coefficient(self, value: int) -> int:
        """Бонус характеристики
        Рассчитывается как:
            (характеристика - базовое значение) // 2

        Args:
            value: характеристика

        Returns:
            int: бонус характеристики
        """
        return (value - self.base_characteristic) // 2


class Unit(BaseUnit):
    """Модель персонажа"""

    def __init__(
        self,
        name: str,
        character: "Character",
        perks: "PerkCollection",
        level: int = 1,
    ):
        """Инициализация персонажа

        Args:
            name: имя персонажа
            character: базовые характиристики персонажа
            perks: список способностей персонажа
            level: уровень персонажа
        """
        super().__init__(
            name=name,
            ability=Ability(character=character),
            perks=perks,
            level=level,
        )

    @property
    def hit_chance(self) -> int:
        """Шанс попадания персонажа
        Рассчитывается как:
            базовый шанс попадания
            + уровень персонажа

        Returns:
            int: значение
        """
        return self.ability.base_hit_chance + self.level

    @property
    def defense(self) -> int:
        """Защита персонажа (шанс уклонения)
        Рассчитывается как:
            базовая защита
            + броня персонажа

        Returns:
            int: значение
        """
        return self.ability.base_defence + self.armor

    @property
    def crit_chance(self) -> int:
        """Шанс критического удара персонажа
        Рассчитывается как:
            базовый шанс критического удара
            + уровень персонажа

        Returns:
            int: значение
        """
        return self.ability.base_crit_chance + self.level

    @property
    def crit_resistance(self) -> int:
        """Защита от критического удара персонажа (шанс избежать крит. удара)
        Рассчитывается как:
            базовая защита от критического удара
            + уровень персонажа

        Returns:
            int: значение
        """
        return self.ability.base_crit_resistance + self.level

    @property
    def magic_resistance(self) -> int:
        """Защита от магии персонажа (сопротивление маг. урону)
        Рассчитывается как:
            базовая защита от магии
            + уровень персонажа

        Returns:
            int: значение
        """
        return self.ability.base_magic_resistance + self.level

    @property
    def hit_points(self) -> int:
        """Очки здоровья персонажа
        Рассчитывается как:
            базовое значение здоровья
            + коэффициент прироста здоровья * (уровень персонажа + бонус выносливости)

        Returns:
            int: значение
        """
        return (
            self.ability.base_hit_points +
            self.ability.base_hp_coefficient * (self.level + self.ability.mastery())
        )

    def level_up(self) -> None:
        """Повысить уровень персонажа (на 1 пункт)"""
        self.level += 1
        self.current_hp = 0 + self.hit_points

    def defend(self, damage: int = 0) -> None:
        """Действие - защищаться (получить урон от другого персонажа)

        Args:
            damage: урон
        """
        hit_points = self.current_hp - damage
        if hit_points <= 0:
            self.current_hp = 0
        else:
            self.current_hp = hit_points

    def end_circle(self) -> None:
        """Завершить ход
        Снимаются все временные бафы и броня
        """
        self.armor = 0
