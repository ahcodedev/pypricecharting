import pytest

from pypricecharting.types import Genre

# Source: https://www.pricecharting.com/api-documentation#genres


def test_genre_members():
    assert len(Genre) == 42
    assert Genre.ACCESSORIES.value == "Accessories"
    assert Genre.ACTION_AND_ADVENTURE.value == "Action & Adventure"
    assert Genre.ARCADE.value == "Arcade"
    assert Genre.BASEBALL.value == "Baseball"
    assert Genre.BEAT_EM_UP.value == "Beat'em Up"
    assert Genre.BASKETBALL.value == "Basketball"
    assert Genre.BOARD_AND_CARD.value == "Board & Card"
    assert Genre.CASINO.value == "Casino"
    assert Genre.COMPILATION.value == "Compilation"
    assert Genre.CONTROLLERS.value == "Controllers"
    assert Genre.DANCE.value == "Dance"
    assert Genre.DEMO_AND_NFR.value == "Demo & NFR"
    assert Genre.EXTREME_SPORTS.value == "Extreme Sports"
    assert Genre.EDUCATIONAL.value == "Educational"
    assert Genre.FIGHTING.value == "Fighting"
    assert Genre.FOOTBALL.value == "Football"
    assert Genre.FPS.value == "FPS"
    assert Genre.GOLF.value == "Golf"
    assert Genre.HACK_AND_SLASH.value == "Hack and Slash"
    assert Genre.HORROR.value == "Horror"
    assert Genre.LIGHT_GUN.value == "Light Gun"
    assert Genre.MAGAZINE.value == "Magazine"
    assert Genre.MINI_GAMES.value == "Mini Games"
    assert Genre.MOVIE.value == "Movie"
    assert Genre.MUSIC.value == "Music"
    assert Genre.OTHER.value == "Other"
    assert Genre.PARTY.value == "Party"
    assert Genre.PINBALL.value == "Pinball"
    assert Genre.PLATFORMER.value == "Platformer"
    assert Genre.PUZZLE.value == "Puzzle"
    assert Genre.RACING.value == "Racing"
    assert Genre.RPG.value == "RPG"
    assert Genre.SIMULATION.value == "Simulation"
    assert Genre.SHOOT_EM_UP.value == "Shoot'em Up"
    assert Genre.SOCCER.value == "Soccer"
    assert Genre.SPORTS.value == "Sports"
    assert Genre.STRATEGY.value == "Strategy"
    assert Genre.SYSTEMS.value == "Systems"
    assert Genre.THIRD_PERSON_SHOOTER.value == "Third Person Shooter"
    assert Genre.TRIVIA.value == "Trivia"
    assert Genre.VISUAL_NOVEL.value == "Visual Novel"
    assert Genre.WRESTLING.value == "Wrestling"


def test_genre_lookup_by_value():
    for member in Genre:
        assert Genre(member.value) is member


def test_genre_unknown_value_raises():
    with pytest.raises(ValueError, match="is not a valid"):
        Genre("Not A Genre")
