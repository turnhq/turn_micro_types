from enum import Enum

class BaseScopes(str, Enum): ...

class ScreenMicroScopes(BaseScopes):
    READ_WORKERS: str
