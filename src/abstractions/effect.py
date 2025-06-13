from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.abstractions.item import BaseItem
    from src.abstractions.unit import BaseUnit
    from utils.tools import F_spec


class BaseEffect(ABC):
    """Абстрактная модель эффекта
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
        self._name = name
        self._title = title
        self._item = item

    @abstractmethod
    def item_value(self, **kwargs: "F_spec.kwargs") -> int:
        """Сделать бросок кубика предмета"""
        pass

    @abstractmethod
    def hit_value(self, **kwargs: "F_spec.kwargs") -> int:
        """Значение предмета при попадании"""
        pass

    @abstractmethod
    def crit_value(self, **kwargs: "F_spec.kwargs") -> int:
        """Значение предмета при критическом ударе"""
        pass

    @abstractmethod
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
