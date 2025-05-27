from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.abstractions.item import BasicItem
    from src.abstractions.tools import BasicAttribute
    from src.abstractions.unit import BasicUnit
    from src.abstractions.tools import F_spec


class BasicPerk(ABC):
    """Абстрактная модель способности"""

    def __init__(
        self,
        name: str,
        item: "BasicItem",
        attribute: "BasicAttribute",
        status: "BasicAttribute",
        modifier: "BasicAttribute",
    ):
        """Инициализация способности

        Args:
            name: имя
            item: предмет
            attribute: тип способности
            status: статус способности
            modifier: модификатор способности
        """
        self.name = name
        self.item = item
        self.attribute = attribute
        self.status = status
        self.modifier = modifier

    @abstractmethod
    def activate(self, target: "BasicUnit", **kwargs: "F_spec.kwargs") -> None:
        """Активировать способность

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """
        pass

    @abstractmethod
    def change_attribute(self, value: "BasicAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def change_status(self, value: "BasicAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def change_modifier(self, value: "BasicAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        pass
