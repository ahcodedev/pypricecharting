from enum import Enum, unique

# https://www.pricecharting.com/api-documentation#includes


@unique
class VideoGames(Enum):
    """Condition IDs for video game products."""

    LOOSE = 1
    NEW_AND_SEALED = 2
    CIB = 3
    GRADED = 5
    BOX_ONLY = 6
    MANUAL_ONLY = 7
    ITEM_AND_BOX = 8
    ITEM_AND_MANUAL = 9
    BOX_AND_MANUAL = 10
    GRADED_CIB = 13


@unique
class Cards(Enum):
    """Condition IDs for trading card products."""

    UNGRADED = 1
    GRADE_8 = 2
    GRADE_7 = 3
    GRADE_9 = 5
    GRADE_9_5 = 6
    GRADE_10 = 7
    BGS_10 = 8
    GRADE_1 = 9
    GRADE_2 = 10
    GRADE_3 = 13


@unique
class Comics(Enum):
    """Condition IDs for comic book products."""

    UNGRADED = 1
    GRADE_6_0 = 2
    GRADE_4_0 = 3
    GRADE_8_0 = 5
    GRADE_9_2 = 6
    GRADE_9_8 = 7
    GRADE_10_0 = 8
    GRADE_2_0 = 9
    GRADE_9_6 = 10
    GRADE_3_0 = 13


@unique
class Coins(Enum):
    """Condition IDs for coin products."""

    UNGRADED = 1
    AU_50_58 = 2
    VF_20_35 = 3
    MS_62 = 5
    MS_64 = 6
    MS_66 = 7
    F_12_15 = 8
    XF_40_45 = 9
    MS_60 = 10
    MS_61 = 13


@unique
class Condition(Enum):
    """Condition ID enums grouped by product category."""

    VIDEOGAMES = VideoGames
    CARDS = Cards
    COMICS = Comics
    COINS = Coins
