from abc import ABC, abstractmethod
from arcade import Sprite
from arcade.gui.widgets.image import UIImage
from arcade.gui import UISpriteWidget
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from utils.tools import SpriteCore
    from src.abstractions.domain import BaseDomain


class BaseImage(UIImage, ABC):
    """Абстрактная модель рисунка"""

    def __init__(
        self,
        core: "SpriteCore",
    ):
        """Инициализация рисунка

        Args:
            core: свойства графического объекта
        """

        super().__init__(
            texture=core.texture,
            width=core.width,
            height=core.height,
        )
        self._core = core

    @property
    def core(self) -> "SpriteCore":
        return self._core

    @abstractmethod
    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        pass


class BasicUISprite(UISpriteWidget, ABC):
    """Абстрактная модель UI спрайта (графического объекта)"""

    def __init__(
        self,
        core: "SpriteCore",
    ):
        """Инициализация спрайта

        Args:
            core: свойства графического объекта
        """
        sprite = Sprite(
            path_or_texture=core.texture,
        )
        super().__init__(
            width=core.width,
            height=core.height,
            sprite=sprite,
        )
        self._core = core

    @property
    def core(self) -> "SpriteCore":
        return self._core

    @abstractmethod
    def change_domain(self, target: "BaseDomain") -> None:
        """Установить новый домен

        Args:
            target: домен
        """
        pass
