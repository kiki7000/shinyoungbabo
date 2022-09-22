__all__ = ("AssacException", "InvalidParameters", "NotFound")


class AssacException(Exception):
    """Base exception class for every exceptions"""

    pass


class InvalidParameters(AssacException):
    pass


class NotFound(AssacException):
    pass
