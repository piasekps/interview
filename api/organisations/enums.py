from enum import Enum, unique


@unique
class OrganisationStatus(Enum):
    ENABLED = 0
    DISABLED = 1

    @classmethod
    def get_name_by_value(cls, value):
        """
        Get status name.

        We can't directly ask for Enum[value] or Enum.value hence we need to map value to name and return it.

        Args:
            value (int): Enum value
        """
        mapping = {status.value: status.name for status in cls}

        return mapping[value]

    @classmethod
    def values(cls):
        """
        Get all available values for the enum

        Returns:
            (list): Contains all available values for the enum
        """
        return [status.value for status in cls]
