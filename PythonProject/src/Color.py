from enum import IntEnum,unique, Enum

@unique
class Color(IntEnum):
    WHITE = 255
    BLACK = 0

@unique
class MaskColor(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    FILL = 255