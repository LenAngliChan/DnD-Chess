from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.abstractions.dice import BasicRoll
    from src.abstractions.tools import BasicAttribute


class BasicItem(ABC):
    """Абстрактная модель предмета"""

    def __init__(
        self,
        name: str,
        value: "BasicRoll",
        attribute: "BasicAttribute",
    ):
        """Инициализация предмета

        Args:
            name: имя
            value: значение
            attribute: тип предмета
        """
        self.name = name
        self.value = value
        self.attribute = attribute

    @abstractmethod
    def deal(self) -> int:
        """Выполнить действие предмета

        Returns:
            int: значение
        """
        pass
