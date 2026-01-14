import enum
from typing import Tuple


class ErrorTypes(enum.IntEnum):
    MessageParsingError = 1
    TextMessageInvalid = 2
    InvalidMessageReadId = 3
    InvalidDialogReadId = 4
    InvalidUserPk = 5
    InvalidRandomId = 6
    FileMessageInvalid = 7
    FileDoesNotExist = 8


ErrorDescription = Tuple[ErrorTypes, str]
