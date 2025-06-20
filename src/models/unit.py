from typing import TYPE_CHECKING

from src.abstractions.unit import BaseAbility, BaseUnit
from src.utils.enums import WeaponType, MagicType, PerkStatus
from src.models.dice import Dice, DiceRoll
from src.utils.constants import SAVE_THROW_DICE_SIDE

if TYPE_CHECKING:
    from utils.tools import BaseAttribute
    from src.models.collection import PerkCollection
    from src.utils.characters import Characteristic


class Ability(BaseAbility):
    """Модель характеристик персонажа"""

    def __init__(
        self,
        characteristic: "Characteristic",
    ):
        """Инициализация характеристик персонажа

        Args:
            characteristic: базовые характиристики персонажа
        """
        super().__init__(
            characteristic=characteristic,
        )
        dice = Dice(side=SAVE_THROW_DICE_SIDE)
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
        if attribute in WeaponType.values():
            # против оружия нет бонусов
            value = 0
        elif attribute == MagicType.dark.value:
            # против магии тьмы не существует защиты
            value = 0
        else:
            # Против любых других заклинаний по умолчанию спасбросок d20, даже если это лечение
            value = self.save_roll.action()

        # спасбросок по умению
        if attribute in WeaponType.values():
            # против оружия спасбросок по ловкости
            ability = self._dexterity
        elif attribute == MagicType.force.value:
            # против силовых заклинаний спасбросок по силе
            ability = self._strength
        elif attribute == MagicType.fire.value:
            # против огненных заклинаний спасбросок по ловкости
            ability = self._dexterity
        elif attribute == MagicType.ice.value:
            # против ледяных заклинаний спасбросок по выносливости
            ability = self._constitution
        elif attribute == MagicType.psychic.value:
            # против психических атак спасбросок по итнеллекту
            ability = self._intelligence
        elif attribute == MagicType.radiant.value:
            # против заклинаний света спасбросок по мудрости
            ability = self._wisdom
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
            ability = self._strength
        elif attribute == WeaponType.medium.value:
            # мастерство фехтовальным оружием зависит от силы или ловкости (смотря что больше)
            ability = max(self._dexterity, self._strength)
        elif attribute in (WeaponType.ranged.value, WeaponType.light.value):
            # мастерство легким оружием зависит от ловкости
            ability = self._dexterity
        elif attribute == MagicType.force.value:
            # мастерство магии силы зависит от мудрости
            ability = self._wisdom
        elif attribute in (MagicType.fire.value, MagicType.ice.value):
            # мастерство магии огня и льда зависит от интеллекта
            ability = self._intelligence
        elif attribute in (MagicType.psychic.value, MagicType.radiant.value, MagicType.dark.value):
            # мастерство магии иллюзий, света и тьмы зависит от харизмы
            ability = self._charisma
        else:
            # все остальное по умолнчанию - выносливости
            ability = self._constitution

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
        return (value - self._base_characteristic) // 2


class Unit(BaseUnit):
    """Модель персонажа"""

    def __init__(
        self,
        name: str,
        title: str,
        description: str,
        characteristic: "Characteristic",
        perks: "PerkCollection",
        level: int = 1,
    ):
        """Инициализация персонажа

        Args:
            name: имя персонажа
            characteristic: базовые характиристики персонажа
            perks: список способностей персонажа
            level: уровень персонажа
        """
        super().__init__(
            name=name,
            title=title,
            description=description,
            ability=Ability(characteristic=characteristic),
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
        return self._ability.base_hit_chance + self._level

    @property
    def defense(self) -> int:
        """Защита персонажа (шанс уклонения)
        Рассчитывается как:
            базовая защита
            + броня персонажа

        Returns:
            int: значение
        """
        return self._ability.base_defence + self._armor

    @property
    def crit_chance(self) -> int:
        """Шанс критического удара персонажа
        Рассчитывается как:
            базовый шанс критического удара
            + уровень персонажа

        Returns:
            int: значение
        """
        return self._ability.base_crit_chance + self._level

    @property
    def crit_resistance(self) -> int:
        """Защита от критического удара персонажа (шанс избежать крит. удара)
        Рассчитывается как:
            базовая защита от критического удара
            + уровень персонажа

        Returns:
            int: значение
        """
        return self._ability.base_crit_resistance + self._level

    @property
    def magic_resistance(self) -> int:
        """Защита от магии персонажа (сопротивление маг. урону)
        Рассчитывается как:
            базовая защита от магии
            + уровень персонажа

        Returns:
            int: значение
        """
        return self._ability.base_magic_resistance + self._level

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
            self._ability.base_hit_points +
            self._ability.base_hp_coefficient * (self._level + self._ability.mastery())
        )

    def level_up(self) -> None:
        """Повысить уровень персонажа (на 1 пункт)"""
        self._level += 1
        self._current_hp = 0 + self.hit_points

    def defend_self(self, damage: int = 0) -> None:
        """Действие - защищаться (получить урон от другого персонажа)

        Args:
            damage: урон
        """
        hit_points = self._current_hp - damage
        if hit_points <= 0:
            self._current_hp = 0
        else:
            self._current_hp = hit_points

    def shield_self(self, value: int = 0) -> None:
        """Действие - укрыться щитом

        Args:
            value: значение брони
        """
        self._armor += value

    def heal_self(self, value: int = 0) -> None:
        """Действие - исцелиться

        Args:
            value: значение
        """
        hit_points = self._current_hp + value
        if hit_points > self.hit_points:
            self._current_hp = 0 + self.hit_points
        else:
            self._current_hp = hit_points

    def end_circle(self) -> None:
        """Завершить ход
        Снимаются все временные бафы и броня, перезаряжаются способности
        """
        self._armor = 0
        for perk in self._perks.values():
            perk.change_status(value=PerkStatus.active.value)
