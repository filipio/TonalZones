from enum import IntEnum,unique

@unique
class Filter(IntEnum):
    AVARAGING = 0
    GAUSSIAN = 1
    MEDIAN=2
    BILATERAL=3
