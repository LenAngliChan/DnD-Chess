from functools import wraps
from typing import TYPE_CHECKING, Callable, TypeVar, ParamSpec

from src.utils.enums import PerkModifier

if TYPE_CHECKING:
    from src.abstractions.perk import BasicPerk

F_spec = ParamSpec("F_spec")
F_result = TypeVar("F_result")


def modify_perk_action(
    func: Callable[F_spec, F_result],
) -> Callable[F_spec, F_result]:
    @wraps(func)
    def wrapper(*args: F_spec.args, **kwargs: F_spec.kwargs) -> F_result:
        perk: "BasicPerk" = args[0]
        modifier = perk.modifier
        value = 0
        try:
            if modifier == PerkModifier.advantage.value:
                throw = 0
                for i in range(2):
                    result = func(*args, **kwargs)
                    if throw < result:
                        throw = result
                value = throw
            elif modifier == PerkModifier.vulnerability.value:
                throw = 99
                for i in range(2):
                    result = func(*args, **kwargs)
                    if throw > result:
                        throw = result
                value = throw
            else:
                value = func(*args, **kwargs)
        finally:
            return value
    return wrapper
