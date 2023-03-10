from abc import ABC
import enum
from typing import Callable, Dict, Generic, Literal, Set, Type, TypeVar, Union

from .exception import InvalidStateException

DatabaseModel = TypeVar("DatabaseModel")

TRANSITION_CALLBACK_TYPE = Callable[[], None]


class Meta(enum.EnumMeta):
    pass


class StateMachineOptions(str, enum.Enum, metaclass=Meta):
    ...


StateMachineOptionsType = TypeVar(
    "StateMachineOptionsType", bound="StateMachineOptions"
)


class TurnStateMachine(ABC, Generic[StateMachineOptionsType, DatabaseModel]):
    __slots__ = (
        "_state",
        "_on_enter_transition_callbacks",
        "_on_exit_transition_callbacks",
        "_transition_callback",
        "_model_state_attribute",
    )
    _state: StateMachineOptionsType
    _options_enum: Type[StateMachineOptionsType]
    _all_valid_states: Set[str]
    _transition_callback: TRANSITION_CALLBACK_TYPE
    _on_enter_callbacks: Dict[StateMachineOptionsType, Callable]
    _on_exit_callbacks: Dict[StateMachineOptionsType, Callable]
    _model: DatabaseModel
    _model_state_attribute: str

    def __init__(
        self,
        *,
        options_enum: Type[StateMachineOptionsType],
        model: DatabaseModel,
        initial_state: StateMachineOptionsType,
        transition_callback: TRANSITION_CALLBACK_TYPE,
        model_state_attribute: str = "status",
    ):
        self._model = model
        self._state = initial_state
        self._transition_callback = transition_callback
        self._options_enum = options_enum
        self._all_valid_states = self.__get_valid_states(options_enum)
        self._on_enter_callbacks = self.__get_callbacks(prefix="_on_enter_")
        self._on_exit_callbacks = self.__get_callbacks(prefix="_on_exit_")

        self._model_state_attribute = model_state_attribute

    @property
    def state(self) -> StateMachineOptionsType:
        """
        Dynamically get current state from model
        """
        current_state = self._options_enum(
            getattr(self._model, self._model_state_attribute)
        )
        if not current_state:
            raise Exception("Couldn't get state from model")
        self._state = current_state
        return current_state

    def __get_callbacks(
        self, *, prefix: Literal["_on_enter_", "_on_exit_"]
    ) -> Dict[StateMachineOptionsType, TRANSITION_CALLBACK_TYPE]:
        # Look for any methods in the child class called
        # _on_enter_[state] or _on_exit_[state]

        callbacks: Dict[StateMachineOptionsType, TRANSITION_CALLBACK_TYPE] = dict()
        for state in self._all_valid_states:
            state_enum = self._options_enum(state)
            method_name = f"{prefix}{state}"
            callback = getattr(self, method_name, None)
            if callback and callable(callback):
                print(method_name, callback)
                callbacks[state_enum] = callback

        return callbacks

    def _run_on_enter_callback(self, new_state: StateMachineOptionsType) -> None:
        callback = self._on_enter_callbacks.get(new_state)
        if not callback:
            return
        callback()

    def _run_on_exit_callback(self, old_state: StateMachineOptionsType) -> None:
        callback = self._on_exit_callbacks.get(old_state)
        if not callback:
            return
        callback()

    @staticmethod
    def __get_valid_states(enum_meta: Type[StateMachineOptionsType]) -> Set[str]:
        return {v.value for k, v in enum_meta._member_map_.items()}

    def __validate_state(self, state: StateMachineOptionsType) -> None:
        if state.value not in self._all_valid_states:
            raise InvalidStateException(
                f"{state} is not valid. Valid states: {self._all_valid_states}"
            )
        else:
            return

    def _validate_transition(
        self,
        *,
        transition: StateMachineOptionsType,
        from_state: Union[Set[StateMachineOptionsType], Literal["*"]],
    ) -> None:
        # Check no invalid states were passed in from_state set
        if isinstance(from_state, set):
            for state in from_state:
                self.__validate_state(state)
        if from_state == "*":
            return
        if self._state not in from_state:
            raise Exception(f"Invalid transition {transition} from {self._state}")

    def _apply_state(self, new_state: StateMachineOptionsType) -> None:
        # Make sure new state is in enum
        self.__validate_state(new_state)
        self._run_on_exit_callback(self._state)
        self._state = new_state
        self._run_on_enter_callback(new_state)

        # This should apply the new state to the model
        self._transition_callback()
