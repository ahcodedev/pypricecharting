import pytest

from pypricecharting.types.condition import Cards, Coins, Comics, Condition, VideoGames

# Source: https://www.pricecharting.com/api-documentation#includes


def test_video_games_members():
    assert len(VideoGames) == 10
    assert VideoGames.LOOSE.value == 1
    assert VideoGames.NEW_AND_SEALED.value == 2
    assert VideoGames.CIB.value == 3
    assert VideoGames.GRADED.value == 5
    assert VideoGames.BOX_ONLY.value == 6
    assert VideoGames.MANUAL_ONLY.value == 7
    assert VideoGames.ITEM_AND_BOX.value == 8
    assert VideoGames.ITEM_AND_MANUAL.value == 9
    assert VideoGames.BOX_AND_MANUAL.value == 10
    assert VideoGames.GRADED_CIB.value == 13


def test_video_games_lookup_by_id():
    for member in VideoGames:
        assert VideoGames(member.value) is member


def test_video_games_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        VideoGames(4)


def test_cards_members():
    assert len(Cards) == 10
    assert Cards.UNGRADED.value == 1
    assert Cards.GRADE_8.value == 2
    assert Cards.GRADE_7.value == 3
    assert Cards.GRADE_9.value == 5
    assert Cards.GRADE_9_5.value == 6
    assert Cards.GRADE_10.value == 7
    assert Cards.BGS_10.value == 8
    assert Cards.GRADE_1.value == 9
    assert Cards.GRADE_2.value == 10
    assert Cards.GRADE_3.value == 13


def test_cards_lookup_by_id():
    for member in Cards:
        assert Cards(member.value) is member


def test_cards_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Cards(4)


def test_comics_members():
    assert len(Comics) == 10
    assert Comics.UNGRADED.value == 1
    assert Comics.GRADE_6_0.value == 2
    assert Comics.GRADE_4_0.value == 3
    assert Comics.GRADE_8_0.value == 5
    assert Comics.GRADE_9_2.value == 6
    assert Comics.GRADE_9_8.value == 7
    assert Comics.GRADE_10_0.value == 8
    assert Comics.GRADE_2_0.value == 9
    assert Comics.GRADE_9_6.value == 10
    assert Comics.GRADE_3_0.value == 13


def test_comics_lookup_by_id():
    for member in Comics:
        assert Comics(member.value) is member


def test_comics_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Comics(4)


def test_coins_members():
    assert len(Coins) == 10
    assert Coins.UNGRADED.value == 1
    assert Coins.AU_50_58.value == 2
    assert Coins.VF_20_35.value == 3
    assert Coins.MS_62.value == 5
    assert Coins.MS_64.value == 6
    assert Coins.MS_66.value == 7
    assert Coins.F_12_15.value == 8
    assert Coins.XF_40_45.value == 9
    assert Coins.MS_60.value == 10
    assert Coins.MS_61.value == 13


def test_coins_lookup_by_id():
    for member in Coins:
        assert Coins(member.value) is member


def test_coins_unknown_id_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Coins(4)


def test_condition_categories():
    assert len(Condition) == 4
    assert Condition.VIDEOGAMES.value is VideoGames
    assert Condition.CARDS.value is Cards
    assert Condition.COMICS.value is Comics
    assert Condition.COINS.value is Coins
