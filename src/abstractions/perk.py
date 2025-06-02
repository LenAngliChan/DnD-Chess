from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional
from arcade import load_texture, Texture

if TYPE_CHECKING:
    from arcade.types import PathOrTexture
    from src.abstractions.item import BaseItem
    from src.abstractions.tools import BaseAttribute
    from src.abstractions.unit import BaseUnit
    from src.abstractions.tools import F_spec


class BasePerk(ABC):
    """Абстрактная модель способности"""

    def __init__(
        self,
        name: str,
        item: "BaseItem",
        attribute: "BaseAttribute",
        status: "BaseAttribute",
        modifier: "BaseAttribute",
        texture_path: "PathOrTexture" = None,
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
        if texture_path:
            if isinstance(texture_path, Texture):
                self._texture = texture_path
            else:
                self._texture = load_texture(file_path=texture_path)

    @property
    def texture(self) -> Optional["Texture"]:
        return self._texture

    @abstractmethod
    def activate(self, target: "BaseUnit", **kwargs: "F_spec.kwargs") -> None:
        """Активировать способность

        Args:
            target: цель способности
            kwargs: дополнительные параметры
        """
        pass

    @abstractmethod
    def change_attribute(self, value: "BaseAttribute") -> None:
        """Изменить тип способности

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def change_status(self, value: "BaseAttribute") -> None:
        """Изменить статус способности

        Args:
            value: значение
        """
        pass

    @abstractmethod
    def change_modifier(self, value: "BaseAttribute") -> None:
        """Изменить модификатор способности

        Args:
            value: значение
        """
        pass
