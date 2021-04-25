from enum import IntEnum,unique, Enum

@unique
class Color(IntEnum):
    WHITE = 255
    BLACK = 0

@unique
class MaskColor(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3