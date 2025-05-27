from enum import Enum
from typing import TypeVar, ParamSpec

F_spec = ParamSpec("F_spec")
F_result = TypeVar("F_result")


class BasicAttribute(Enum):
    """Абстрактная модель свойства объектов"""
    pass
