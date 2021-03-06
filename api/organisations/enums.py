from enum import unique

from core.enums import BaseEnum


@unique
class OrganisationStatus(BaseEnum):
    ENABLED = 0
    DISABLED = 1
