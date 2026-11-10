import pytest

from pypricecharting.types import Condition

# Source: https://www.pricecharting.com/api-documentation#includes


def test_video_games_members():
    assert len(Condition.VideoGames) == 10
    assert Condition.VideoGames.LOOSE == 1
    assert Condition.VideoGames.NEW_AND_SEALED == 2
    assert Condition.VideoGames.CIB == 3
    assert Condition.VideoGames.GRADED == 5
    assert Condition.VideoGames.BOX_ONLY == 6
    assert Condition.VideoGames.MANUAL_ONLY == 7
    assert Condition.VideoGames.ITEM_AND_BOX == 8
    assert Condition.VideoGames.ITEM_AND_MANUAL == 9
    assert Condition.VideoGames.BOX_AND_MANUAL == 10
    assert Condition.VideoGames.GRADED_CIB == 13


def test_video_games_lookup_by_id():
    for member in Condition.VideoGames:
        assert Condition.VideoGames(member) is member


def test_video_games_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Condition.VideoGames(4)


def test_cards_members():
    assert len(Condition.Cards) == 10
    assert Condition.Cards.UNGRADED == 1
    assert Condition.Cards.GRADE_8 == 2
    assert Condition.Cards.GRADE_7 == 3
    assert Condition.Cards.GRADE_9 == 5
    assert Condition.Cards.GRADE_9_5 == 6
    assert Condition.Cards.GRADE_10 == 7
    assert Condition.Cards.BGS_10 == 8
    assert Condition.Cards.GRADE_1 == 9
    assert Condition.Cards.GRADE_2 == 10
    assert Condition.Cards.GRADE_3 == 13


def test_cards_lookup_by_id():
    for member in Condition.Cards:
        assert Condition.Cards(member) is member


def test_cards_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Condition.Cards(4)


def test_comics_members():
    assert len(Condition.Comics) == 10
    assert Condition.Comics.UNGRADED == 1
    assert Condition.Comics.GRADE_6_0 == 2
    assert Condition.Comics.GRADE_4_0 == 3
    assert Condition.Comics.GRADE_8_0 == 5
    assert Condition.Comics.GRADE_9_2 == 6
    assert Condition.Comics.GRADE_9_8 == 7
    assert Condition.Comics.GRADE_10_0 == 8
    assert Condition.Comics.GRADE_2_0 == 9
    assert Condition.Comics.GRADE_9_6 == 10
    assert Condition.Comics.GRADE_3_0 == 13


def test_comics_lookup_by_id():
    for member in Condition.Comics:
        assert Condition.Comics(member) is member


def test_comics_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Condition.Comics(4)


def test_coins_members():
    assert len(Condition.Coins) == 10
    assert Condition.Coins.UNGRADED == 1
    assert Condition.Coins.AU_50_58 == 2
    assert Condition.Coins.VF_20_35 == 3
    assert Condition.Coins.MS_62 == 5
    assert Condition.Coins.MS_64 == 6
    assert Condition.Coins.MS_66 == 7
    assert Condition.Coins.F_12_15 == 8
    assert Condition.Coins.XF_40_45 == 9
    assert Condition.Coins.MS_60 == 10
    assert Condition.Coins.MS_61 == 13


def test_coins_lookup_by_id():
    for member in Condition.Coins:
        assert Condition.Coins(member) is member


def test_coins_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Condition.Coins(4)
