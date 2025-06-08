from contextvars import ContextVar
from enum import Enum
from dataclasses import dataclass
from typing import TypeVar, ParamSpec, TYPE_CHECKING, Optional, NamedTuple, Dict

from src.utils.messages import DEFAULT_MSG
from src.utils.constants import (
    CELL_SIZE,
    BASE_CHARACTERISTIC,
    BASE_HIT_POINTS,
    BASE_HP_COEFFICIENT,
    BASE_HIT_CHANCE,
    BASE_DEFENCE,
    BASE_CRIT_CHANCE,
    BASE_CRIT_RESISTANCE,
    BASE_MAGIC_RESISTANCE,
)

F_spec = ParamSpec("F_spec")
F_result = TypeVar("F_result")

if TYPE_CHECKING:
    from arcade import Texture
    from arcade.gui import UIWidget
    from src.abstractions.domain import BaseDomain


class BaseAttribute(Enum):
    """Абстрактная модель свойства объектов"""
    pass


class Entry(NamedTuple):
    """Вспомогательная модель виджетов"""
    child: "UIWidget"
    data: Dict


@dataclass
class Index:
    """Вспомогательный класс для обозначения индекса (позиции) на игровой доске"""
    row: int = None
    column: int = None
    x: float = None
    y: float = None

    def __post_init__(self):
        if self.column is not None and self.row is not None:
            self.x = self.column * CELL_SIZE
            self.y = self.row * CELL_SIZE
        elif self.x is not None and self.y is not None:
            self.column = int(self.x / CELL_SIZE)
            self.row = int(self.y / CELL_SIZE)
        else:
            raise KeyError

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return f"({self.column}, {self.row})"


@dataclass
class Characteristic:
    """Вспомогательная модель характеристик персонажа"""
    strength: int = BASE_CHARACTERISTIC
    constitution: int = BASE_CHARACTERISTIC
    dexterity: int = BASE_CHARACTERISTIC
    intelligence: int = BASE_CHARACTERISTIC
    wisdom: int = BASE_CHARACTERISTIC
    charisma: int = BASE_CHARACTERISTIC
    base_hit_points: int = BASE_HIT_POINTS
    base_hp_coefficient: int = BASE_HP_COEFFICIENT
    base_hit_chance: int = BASE_HIT_CHANCE
    base_defence: int = BASE_DEFENCE
    base_crit_chance: int = BASE_CRIT_CHANCE
    base_crit_resistance: int = BASE_CRIT_RESISTANCE
    base_magic_resistance: int = BASE_MAGIC_RESISTANCE


class Textures(NamedTuple):
    """Вспомогательная модель для определения текстур персонажей"""
    day: "Texture"
    night: "Texture"


@dataclass
class Character:
    """Вспомогательная модель персонажей"""
    name: str
    title: str
    description: str
    characteristic: Characteristic
    textures: Textures


class SpriteCore:
    """Модель исходных данных для графических объектов"""

    def __init__(
            self,
            name: str,
            index: Index,
            texture: "Texture" = None,
            width: float = CELL_SIZE,
            height: float = CELL_SIZE,
            domain: "BaseDomain" = None,
    ):
        """Инициализация спрайта

        Args:
            name: имя
            index: позиция на доске
            texture: текстуры
            width: ширина
            height: высота
            domain: домен
        """

        self._name = name
        self._index = index
        self._texture = texture
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
    def index(self) -> Index:
        return self._index

    @index.setter
    def index(self, value: Index) -> None:
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


class InfoContext:
    """Контекстный менеджер сообщений"""
    def __init__(self):
        self._text = ContextVar("text")
        self._default_value = DEFAULT_MSG

    def set(self, value: str) -> None:
        self._text.set(value)

    def get(self) -> str:
        return self._text.get()

    def update(self, value: str) -> None:
        current_text = self.get()
        self.set(
            value=current_text + "\n" + value
        )

    def reset(self, value: str = None) -> None:
        new_text = value + "\n" + self._default_value if value else self._default_value
        self.set(value=new_text)


info_context = InfoContext()
