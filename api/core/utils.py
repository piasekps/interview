from math import isnan


def api_version_to_float(version):
    """
    Parse `version` and return its float representation.

    Args:
        version (str): A string representation of an API version that starts with character
            "v" and is followed by a float or integer
    Returns:
        Float representation of `version` or `None` if conversion was impossible
    """
    if not (version and isinstance(version, str)):
        return None

    try:
        result = float(version[1:])
    except ValueError:
        return None

    if result < 0 or isnan(result):
        return None

    return result
