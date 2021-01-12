from enum import unique

from core.enums import BaseEnum


@unique
class UserState(BaseEnum):
    ENABLED = 0
    DISABLED = 1
    BLOCKED = 2
    DELETED = 3
