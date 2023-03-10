from enum import Enum


class BaseScopes(str, Enum):
    pass


class ScreenMicroScopes(BaseScopes):
    READ_WORKERS = "read:workers"
