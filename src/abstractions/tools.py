from arcade import load_texture
from enum import Enum
from typing import TypeVar, ParamSpec, TYPE_CHECKING, Optional

from src.utils.constants import CELL_SIZE

F_spec = ParamSpec("F_spec")
F_result = TypeVar("F_result")

if TYPE_CHECKING:
    from arcade import Texture
    from src.abstractions.domain import BaseDomain


class BaseAttribute(Enum):
    """Абстрактная модель свойства объектов"""
    pass


class SpriteCore:
    """Модель исходных данных для графических объектов"""

    def __init__(
            self,
            name: str,
            index: tuple[int, int],
            texture_path: str = None,
            width: float = CELL_SIZE,
            height: float = CELL_SIZE,
            domain: "BaseDomain" = None,
    ):
        """Инициализация спрайта

        Args:
            name: имя
            index: позиция на доске
            texture_path: путь к текстурам
            width: ширина
            height: высота
            domain: домен
        """

        self._name = name
        self._index = index
        self._texture = load_texture(file_path=texture_path) if texture_path else None
        self._width = width
        self._height = height
        self._domain = domain

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def index(self) -> tuple[int, int]:
        return self._index

    @index.setter
    def index(self, value: tuple[int, int]) -> None:
        self._index = value

    @property
    def texture(self) -> Optional["Texture"]:
        return self._texture

    @texture.setter
    def texture(self, value: "Texture") -> None:
        self._texture = value

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def domain(self) -> "BaseDomain":
        return self._domain

    @domain.setter
    def domain(self, value: "BaseDomain") -> None:
        self._domain = value
