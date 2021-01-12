from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def get_name_by_value(cls, value):
        """
        Get status name.

        Args:
            value (int): Enum value
        """
        return cls(value).name

    @classmethod
    def values(cls):
        """
        Get all available values for the enum

        Returns:
            (list): Contains all available values for the enum
        """
        return [status.value for status in cls]
