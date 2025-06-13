from functools import wraps
from math import inf
from typing import TYPE_CHECKING, Callable, TypeVar, ParamSpec

from src.utils.enums import RollModifier

if TYPE_CHECKING:
    from src.abstractions.dice import BaseRoll

F_spec = ParamSpec("F_spec")
F_result = TypeVar("F_result")


def modify_roll(
    func: Callable[F_spec, F_result],
) -> Callable[F_spec, F_result]:
    @wraps(func)
    def wrapper(*args: F_spec.args, **kwargs: F_spec.kwargs) -> F_result:
        roll: "BaseRoll" = args[0]
        modifier = roll.modifier
        if modifier == RollModifier.advantage.value:
            throw = 0
            for i in range(2):
                result = func(*args, **kwargs)
                if throw < result:
                    throw = result
            value = throw
        elif modifier == RollModifier.vulnerability.value:
            throw = inf
            for i in range(2):
                result = func(*args, **kwargs)
                if throw > result:
                    throw = result
            value = throw
        else:
            value = func(*args, **kwargs)

        return value
    return wrapper
