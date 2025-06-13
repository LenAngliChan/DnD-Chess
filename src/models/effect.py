from typing import TYPE_CHECKING

from src.abstractions.effect import BaseEffect
from src.utils.tools import info_context
from src.utils.messages import (
    EFFECT_HIT_VALUE_MSG,
    EFFECT_CRIT_VALUE_MSG,
    MELEE_ATTACK_MSG,
    SHIELD_APPLY_MSG,
    MAGIC_ATTACK_MSG,
    HEAL_APPLY_MSG,
    RESIST_VALUE_MSG,
)

if TYPE_CHECKING:
    from src.abstractions.item import BaseItem
    from src.abstractions.unit import BaseUnit
    from utils.tools import F_spec


class Effect(BaseEffect):
    """Модель эффекта
    Эффект отвечает за броски значения предмета
    Также отвечает за влияние на цель
    """

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def item_value(
        self,
        domain_bonus: int = 0,
        building_bonus: int = 0,
    ):
        """Сделать бросок кубика предмета
        Учет бонусов:
            Разница в силе доменов идет как бонус (только для погашения штрафа)
            Здания дают бонус к защите противника (штраф к урону)

        Returns:
            int: значение
        """
        return self._item.deal(
            bonus=domain_bonus,
            penalty=building_bonus,
        )

    def hit_value(
        self,
        mastery: int = 0,
        **kwargs: "F_spec.kwargs"
    ) -> int:
        """Значение предмета при попадании
        Рассчитывается как:
            бросок кубика предмета
            + бонусы

        Returns:
            int: значение
        """
        value = self.item_value(**kwargs)
        info_context.update(
            value=EFFECT_HIT_VALUE_MSG.format(value=value, mastery=mastery),
        )
        return value + mastery

    def crit_value(self) -> int:
        """Значение предмета при критическом ударе
        Рассчитывается как:
            значение удара при попадании

        Returns:
            int: значение
        """
        value = self.item_value()
        info_context.update(
            value=EFFECT_CRIT_VALUE_MSG.format(value=value),
        )
        return value

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        pass


class Cut(Effect):
    """Модель эффекта - Режущий Урон"""
    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет режущего урона
        value = 0
        if hit:
            value = self.hit_value(**kwargs)
            if crit:
                value += self.crit_value()

        target.defend_self(damage=value)
        info_context.update(
            value=MELEE_ATTACK_MSG.format(
                result=value,
                type=self._item.attribute,
                name=target.title,
            ),
        )


class Pierce(Effect):
    """Модель эффекта - Колющий Урон"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет колющего урона
        value = 0
        if hit:
            value = self.hit_value(**kwargs)
            if crit:
                value += self.crit_value()

        target.defend_self(damage=value)
        info_context.update(
            value=MELEE_ATTACK_MSG.format(
                result=value,
                type=self._item.attribute,
                name=target.title,
            ),
        )


class Crush(Effect):
    """Модель эффекта - Дробящий Урон"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет дробящего урона
        value = self.hit_value(**kwargs)
        if hit:
            if crit:
                value += self.crit_value()
        else:
            value = value // 2

        target.defend_self(damage=value)
        info_context.update(
            value=MELEE_ATTACK_MSG.format(
                result=value,
                type=self._item.attribute,
                name=target.title,
            ),
        )


class Shield(Effect):
    """Модель эффекта - Добавить Защиту"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def item_value(self, **kwargs: "F_spec.kwargs"):
        """Сделать бросок кубика предмета
        При поднятии щита обычно нет бонусов и штрафов

        Returns:
            int: значение
        """
        return self._item.deal()

    def hit_value(
        self,
        **kwargs: "F_spec.kwargs"
    ) -> int:
        """Значение предмета при попадании
        Рассчитывается как:
            бросок кубика предмета

        Returns:
            int: значение
        """
        value = self.item_value(**kwargs)
        info_context.update(
            value=EFFECT_HIT_VALUE_MSG.format(value=value, mastery=0),
        )
        return value

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет дополнительной защиты
        value = self.hit_value(**kwargs)

        target.shield_self(value=value)
        info_context.update(
            value=SHIELD_APPLY_MSG.format(
                result=value,
                name=target.title,
            ),
        )


class Elemental(Effect):
    """Модель эффекта - Магический Урон"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет магического урона
        value = self.hit_value(**kwargs)
        resist = target.magic_resistance
        info_context.update(
            value=RESIST_VALUE_MSG.format(resist=resist),
        )
        if hit:
            if crit:
                value += self.crit_value()
        else:
            if crit:
                value += self.crit_value()
            else:
                value = value // 2

        value = max(value - resist, 0)
        target.defend_self(damage=value)
        info_context.update(
            value=MAGIC_ATTACK_MSG.format(
                result=value,
                type=self._item.attribute,
                name=target.title,
            ),
        )


class Heal(Effect):
    """Модель эффекта - Исцеление"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def item_value(self, **kwargs: "F_spec.kwargs"):
        """Сделать бросок кубика предмета
        При исцелении обычно нет бонусов и штрафов

        Returns:
            int: значение
        """
        return self._item.deal()

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет исцеления
        value = self.hit_value(**kwargs)
        resist = target.magic_resistance
        info_context.update(
            value=RESIST_VALUE_MSG.format(resist=resist),
        )
        if hit:
            if crit:
                value += self.crit_value()
        else:
            if crit:
                value += self.crit_value()
            else:
                value = value // 2

        value = max(value - resist, 0)
        # при критическом промахе будет нанесен урон самому заклинателю
        if not hit and crit:
            info_context.update(
                value=MAGIC_ATTACK_MSG.format(
                    result=value,
                    type=self._item.attribute,
                    name=target.title,
                ),
            )
            target.defend_self(damage=value)
        else:
            info_context.update(
                value=HEAL_APPLY_MSG.format(
                    result=value,
                    name=target.title,
                ),
            )
            target.heal_self(value=value)


class Buff(Effect):
    """Модель эффекта - бафф/дебафф"""

    def __init__(
        self,
        name: str,
        title: str,
        item: "BaseItem",
    ):
        """Инициализация эффекта

        Args:
            name: имя эффекта
            title: имя эффекта для отображения на gui
            item: предмет
        """
        super().__init__(
            name=name,
            title=title,
            item=item,
        )

    def item_value(self, **kwargs: "F_spec.kwargs"):
        """Сделать бросок кубика предмета
        При бафах/дебафах обычно нет бонусов и штрафов

        Returns:
            int: значение
        """
        return self._item.deal()

    def apply(
        self,
        target: "BaseUnit",
        hit: bool,
        crit: bool,
        **kwargs: "F_spec.kwargs",
    ) -> None:
        """Применить эффект к цели

        Args:
            target: цель способности
            hit: бросок на попадание
            crit: бросок на критический удар
            kwargs: дополнительные параметры
        """
        # расчет значений бафа/дебафа
        pass
