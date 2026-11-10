import datetime
from enum import Enum, IntEnum, StrEnum, unique


@unique
class Status(Enum):
    """PriceCharting API response status"""

    SUCCESS = "success"
    ERROR = "error"


@unique
class OfferStatus(Enum):
    """PriceCharting Marketplace offer status"""

    AVAILABLE = "available"
    SOLD = "sold"
    ENDED = "ended"
    PENDING = "pending"
    """Published but not purchasable, because of a vacation hold or payment issue."""
    COLLECTION = "collection"
    """Tracked in the seller's collection, not listed for sale."""


@unique
class Rating(Enum):
    """PriceCharting Marketplace feedback rating"""

    GREAT = 2
    GOOD = 1
    OK = 0
    BAD = -1
    AWFUL = -2


@unique
class State(Enum):
    """Value of a set form flag, such as an `OfferPublishRequestParams` condition tag"""

    ON = "on"


@unique
class RateLimit(Enum):
    """Minimum wait between PriceCharting API calls."""

    API = datetime.timedelta(seconds=1)
    """Any API call: once per second."""
    CSV = datetime.timedelta(minutes=10)
    """CSV downloads: once every 10 minutes."""
    OFFERS_POLLING = datetime.timedelta(minutes=5)
    """The same `/api/offers` URL: once every 5 minutes."""


class Condition:
    """Condition ID enums grouped by product category.

    https://www.pricecharting.com/api-documentation#includes
    """

    @unique
    class VideoGames(IntEnum):
        """Condition IDs for video game products.

        https://www.pricecharting.com/api-documentation#includes
        """

        LOOSE = 1
        NEW_AND_SEALED = 2
        CIB = 3
        """Complete in box: item, box, and manual."""
        GRADED = 5
        BOX_ONLY = 6
        MANUAL_ONLY = 7
        ITEM_AND_BOX = 8
        ITEM_AND_MANUAL = 9
        BOX_AND_MANUAL = 10
        GRADED_CIB = 13

    @unique
    class Cards(IntEnum):
        """Condition IDs for trading card products.

        https://www.pricecharting.com/api-documentation#includes
        """

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
    class Comics(IntEnum):
        """Condition IDs for comic book products.

        https://www.pricecharting.com/api-documentation#includes
        """

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
    class Coins(IntEnum):
        """Condition IDs for coin products.

        https://www.pricecharting.com/api-documentation#includes
        """

        UNGRADED = 1
        AU_50_58 = 2
        """About Uncirculated, grade 50-58."""
        VF_20_35 = 3
        """Very Fine, grade 20-35."""
        MS_62 = 5
        """Mint State 62."""
        MS_64 = 6
        """Mint State 64."""
        MS_66 = 7
        """Mint State 66."""
        F_12_15 = 8
        """Fine, grade 12-15."""
        XF_40_45 = 9
        """Extremely Fine, grade 40-45."""
        MS_60 = 10
        """Mint State 60."""
        MS_61 = 13
        """Mint State 61."""


@unique
class Genre(StrEnum):
    """Product genres as labeled by PriceCharting.

    https://www.pricecharting.com/api-documentation#genres
    """

    ACCESSORIES = "Accessories"
    ACTION_AND_ADVENTURE = "Action & Adventure"
    ARCADE = "Arcade"
    BASEBALL = "Baseball"
    BEAT_EM_UP = "Beat'em Up"
    BASKETBALL = "Basketball"
    BOARD_AND_CARD = "Board & Card"
    CASINO = "Casino"
    COMPILATION = "Compilation"
    CONTROLLERS = "Controllers"
    DANCE = "Dance"
    DEMO_AND_NFR = "Demo & NFR"
    EXTREME_SPORTS = "Extreme Sports"
    EDUCATIONAL = "Educational"
    FIGHTING = "Fighting"
    FOOTBALL = "Football"
    FPS = "FPS"
    GOLF = "Golf"
    HACK_AND_SLASH = "Hack and Slash"
    HORROR = "Horror"
    LIGHT_GUN = "Light Gun"
    MAGAZINE = "Magazine"
    MINI_GAMES = "Mini Games"
    MOVIE = "Movie"
    MUSIC = "Music"
    OTHER = "Other"
    PARTY = "Party"
    PINBALL = "Pinball"
    PLATFORMER = "Platformer"
    PUZZLE = "Puzzle"
    RACING = "Racing"
    RPG = "RPG"
    SIMULATION = "Simulation"
    SHOOT_EM_UP = "Shoot'em Up"
    SOCCER = "Soccer"
    SPORTS = "Sports"
    STRATEGY = "Strategy"
    SYSTEMS = "Systems"
    THIRD_PERSON_SHOOTER = "Third Person Shooter"
    TRIVIA = "Trivia"
    VISUAL_NOVEL = "Visual Novel"
    WRESTLING = "Wrestling"


@unique
class Console(StrEnum):
    """PriceCharting Console IDs

    https://www.pricecharting.com/api-documentation#console-ids
    """

    PANASONIC_3DO = "G25"
    ACTION_MAX = "G36545"
    ADVANCED_PICO_BEENA = "G102752"
    AMIGA = "G46"
    AMIGA_CD32 = "G92"
    AMIIBO = "G56"
    AMIIBO_CARDS = "G46757"
    AMSTRAD_CPC = "G70472"
    AMSTRAD_GX4000 = "G66098"
    APPLE_II = "G79417"
    ARCADIA_2001 = "G91"
    ASIAN_ENGLISH_NINTENDO_3DS = "G56638"
    ASIAN_ENGLISH_PSP = "G59682"
    ASIAN_ENGLISH_PLAYSTATION_2 = "G70756"
    ASIAN_ENGLISH_PLAYSTATION_3 = "G56634"
    ASIAN_ENGLISH_PLAYSTATION_4 = "G56635"
    ASIAN_ENGLISH_PLAYSTATION_5 = "G56636"
    ASIAN_ENGLISH_PLAYSTATION_VITA = "G56637"
    ASIAN_ENGLISH_SWITCH = "G56633"
    ASIAN_ENGLISH_SWITCH_2 = "G80190"
    ASIAN_ENGLISH_XBOX = "G72899"
    ASIAN_XBOX_360 = "G79471"
    ATARI_2600 = "G24"
    ATARI_2800 = "G84152"
    ATARI_400 = "G45"
    ATARI_5200 = "G31"
    ATARI_7800 = "G33"
    ATARI_LYNX = "G26"
    ATARI_ST = "G146"
    ATARI_XE = "G72528"
    BALLY_ASTROCADE = "G90"
    BANDAI_PLAYDIA = "G94412"
    CD_I = "G37"
    CASIO_LOOPY = "G63134"
    CLUB_NINTENDO_MAGAZINE = "G77760"
    COLECOVISION = "G30"
    COMMODORE_128 = "G72569"
    COMMODORE_16 = "G56918"
    COMMODORE_64 = "G28"
    DISNEY_INFINITY = "G52"
    DREAMCAST_MAGAZINE = "G53043"
    ELECTRONIC_GAMING_MONTHLY = "G53047"
    ENTEX_ADVENTURE_VISION = "G72005"
    EVERCADE = "G28704"
    FM_TOWNS_MARTY = "G55665"
    FAIRCHILD_CHANNEL_F = "G83"
    FAMICOM = "G55"
    FAMICOM_DISK_SYSTEM = "G117"
    GAME_AND_WATCH = "G68"
    GAME_INFORMER = "G53044"
    GAME_PLAYERS = "G93674"
    GAME_WAVE = "G55666"
    GAME_COM = "G93"
    GAMEBOY = "G49"
    GAMEBOY_ADVANCE = "G1"
    GAMEBOY_COLOR = "G2"
    GAMEPRO = "G53046"
    GAMECUBE = "G3"
    GIZMONDO = "G7728"
    HYPERSCAN = "G55667"
    INTELLIVISION = "G27"
    JP_3DO = "G68532"
    JP_GAMEBOY = "G112"
    JP_GAMEBOY_ADVANCE = "G79"
    JP_GAMEBOY_COLOR = "G113"
    JP_GAMECUBE = "G98"
    JP_LASERACTIVE = "G68060"
    JP_MSX = "G122"
    JP_MSX2 = "G128"
    JP_NEO_GEO_AES = "G115"
    JP_NEO_GEO_CD = "G43342"
    JP_NEO_GEO_MVS = "G114"
    JP_NEO_GEO_POCKET = "G59835"
    JP_NEO_GEO_POCKET_COLOR = "G129"
    JP_NINTENDO_3DS = "G119"
    JP_NINTENDO_64 = "G99"
    JP_NINTENDO_DS = "G111"
    JP_NINTENDO_SWITCH = "G100"
    JP_NINTENDO_SWITCH_2 = "G80189"
    JP_PC_ENGINE = "G82"
    JP_PC_ENGINE_CD = "G154"
    JP_PSP = "G110"
    JP_PLAYSTATION = "G107"
    JP_PLAYSTATION_2 = "G108"
    JP_PLAYSTATION_3 = "G109"
    JP_PLAYSTATION_4 = "G118"
    JP_PLAYSTATION_5 = "G7470"
    JP_PLAYSTATION_VITA = "G106"
    JP_SEGA_DREAMCAST = "G64"
    JP_SEGA_GAME_GEAR = "G74"
    JP_SEGA_MARK_III = "G6900"
    JP_SEGA_MEGA_CD = "G140"
    JP_SEGA_MEGA_DRIVE = "G105"
    JP_SEGA_PICO = "G137"
    JP_SEGA_SATURN = "G67"
    JP_SUPER_32X = "G142"
    JP_VIRTUAL_BOY = "G76"
    JP_WII = "G102"
    JP_WII_U = "G104"
    JP_XBOX = "G125"
    JP_XBOX_360 = "G124"
    JP_XBOX_ONE = "G126"
    JP_XBOX_SERIES_X = "G7587"
    JAGUAR = "G21"
    JAGUAR_CD = "G65467"
    LASERACTIVE = "G66470"
    LEGO_DIMENSIONS = "G144"
    MACINTOSH = "G81500"
    MAGNAVOX_ODYSSEY = "G130"
    MAGNAVOX_ODYSSEY_2 = "G36"
    MAGNAVOX_ODYSSEY_300 = "G131"
    MATTEL_AQUARIUS = "G132"
    MEGAZONE = "G58494"
    MICROVISION = "G6956"
    MINI_ARCADE = "G69"
    N_GAGE = "G42"
    NES = "G17"
    NEO_GEO_AES = "G116"
    NEO_GEO_CD = "G60"
    NEO_GEO_MVS = "G18"
    NEO_GEO_POCKET_COLOR = "G40"
    NINTENDO_3DS = "G39"
    NINTENDO_64 = "G4"
    NINTENDO_DS = "G5"
    NINTENDO_POWER = "G81"
    NINTENDO_SWITCH = "G59"
    NINTENDO_SWITCH_2 = "G80178"
    NUON = "G72978"
    OFFICIAL_NINTENDO_MAGAZINE = "G77563"
    OFFICIAL_US_PLAYSTATION_MAGAZINE = "G73272"
    PAL_3DO = "G68531"
    PAL_AMIGA_CD32 = "G153"
    PAL_AMSTRAD_GX4000 = "G72181"
    PAL_ATARI_2600 = "G72094"
    PAL_ATARI_7800 = "G62701"
    PAL_DREAMCAST_MAGAZINE = "G85742"
    PAL_EVERCADE = "G61287"
    PAL_GAMEBOY = "G73"
    PAL_GAMEBOY_ADVANCE = "G80"
    PAL_GAMEBOY_COLOR = "G77"
    PAL_GAMECUBE = "G70"
    PAL_MSX = "G123"
    PAL_MSX2 = "G127"
    PAL_MEGA_DRIVE_32X = "G141"
    PAL_N_GAGE = "G63150"
    PAL_NES = "G58"
    PAL_NEO_GEO_POCKET = "G61530"
    PAL_NEO_GEO_POCKET_COLOR = "G37074"
    PAL_NINTENDO_3DS = "G94"
    PAL_NINTENDO_64 = "G62"
    PAL_NINTENDO_DS = "G78"
    PAL_NINTENDO_SWITCH = "G87"
    PAL_NINTENDO_SWITCH_2 = "G80188"
    PAL_PSP = "G84"
    PAL_PLAYSTATION = "G72"
    PAL_PLAYSTATION_2 = "G63"
    PAL_PLAYSTATION_3 = "G75"
    PAL_PLAYSTATION_4 = "G86"
    PAL_PLAYSTATION_5 = "G7469"
    PAL_PLAYSTATION_VITA = "G101"
    PAL_SEGA_DREAMCAST = "G65"
    PAL_SEGA_GAME_GEAR = "G121"
    PAL_SEGA_MASTER_SYSTEM = "G51"
    PAL_SEGA_MEGA_CD = "G139"
    PAL_SEGA_MEGA_DRIVE = "G71"
    PAL_SEGA_PICO = "G138"
    PAL_SEGA_SATURN = "G97"
    PAL_SUPER_NINTENDO = "G61"
    PAL_VECTREX = "G133"
    PAL_VIDEOPAC_G7000 = "G134"
    PAL_VIDEOPAC_G7400 = "G135"
    PAL_WII = "G85"
    PAL_WII_U = "G96"
    PAL_XBOX = "G88"
    PAL_XBOX_360 = "G89"
    PAL_XBOX_ONE = "G95"
    PAL_XBOX_SERIES_X = "G7586"
    PC_FX = "G6955"
    PC_GAMER_MAGAZINE = "G53045"
    PC_GAMES = "G145"
    PC_8801 = "G99621"
    PSP = "G9"
    PIPPIN = "G55669"
    PLAYSTATION = "G6"
    PLAYSTATION_2 = "G7"
    PLAYSTATION_3 = "G12"
    PLAYSTATION_4 = "G53"
    PLAYSTATION_5 = "G7468"
    PLAYSTATION_VITA = "G43"
    POKEMON_MINI = "G143"
    POLYMEGA = "G76600"
    RCA_STUDIO_II = "G87937"
    RDI_HALCYON = "G91000"
    RETRO_GAMER_MAGAZINE = "G93657"
    RUMBLE_U = "G43345"
    SEGA_32X = "G50"
    SEGA_CD = "G23"
    SEGA_DREAMCAST = "G16"
    SEGA_GAME_GEAR = "G20"
    SEGA_GENESIS = "G15"
    SEGA_MASTER_SYSTEM = "G29"
    SEGA_PICO = "G136"
    SEGA_SATURN = "G14"
    SEGA_SATURN_MAGAZINE = "G85478"
    SHARP_X1 = "G99620"
    SHARP_X68000 = "G61110"
    SINCLAIR_ZX81 = "G77384"
    SKYLANDERS = "G48"
    STARLINK = "G43344"
    STONEHEART = "G60326"
    STRATEGY_GUIDE = "G26297"
    SUPER_CASSETTE_VISION = "G101795"
    SUPER_FAMICOM = "G66"
    SUPER_NINTENDO = "G13"
    SUPERVISION = "G55668"
    TI_99 = "G120"
    TRS_80 = "G75713"
    TAPWAVE_ZODIAC = "G51260"
    TIGER_R_ZONE = "G43401"
    TURBOGRAFX_CD = "G6927"
    TURBOGRAFX_16 = "G19"
    UB_FUNKEYS = "G75110"
    VTECH_SMILE = "G99622"
    VTECH_SOCRATES = "G56889"
    VECTREX = "G32"
    VIC_20 = "G44"
    VIRTUAL_BOY = "G22"
    WHOLESALE = "G57"
    WII = "G11"
    WII_U = "G47"
    WONDERSWAN = "G151"
    WONDERSWAN_COLOR = "G152"
    XBOX = "G8"
    XBOX_360 = "G10"
    XBOX_ONE = "G54"
    XBOX_SERIES_X = "G7585"
    ZX_SPECTRUM = "G44257"
