import enum
from .exception import InvalidStateException as InvalidStateException
from abc import ABC
from typing import Callable, Type, TypeVar

DatabaseModel = TypeVar('DatabaseModel')
TRANSITION_CALLBACK_TYPE = Callable[[], None]

class Meta(enum.EnumMeta): ...
class StateMachineOptions(str, enum.Enum, metaclass=Meta): ...
StateMachineOptionsType = TypeVar('StateMachineOptionsType', bound='StateMachineOptions')

class TurnStateMachine(ABC):
    def __init__(self, *, options_enum: Type[StateMachineOptionsType], model: DatabaseModel, initial_state: StateMachineOptionsType, transition_callback: TRANSITION_CALLBACK_TYPE, model_state_attribute: str = ...) -> None: ...
    @property
    def state(self) -> StateMachineOptionsType: ...
