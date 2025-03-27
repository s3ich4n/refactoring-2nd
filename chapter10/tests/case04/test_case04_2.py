from chapter10.src.case04.case04_2 import (
    Voyage,
    HistoryItem,
    rating,
    create_rating,
    ExperiencedChinaRating,
    Rating,
)


def test_rating_creates_appropriate_rating_class():
    # 중국 경험이 있는 경우
    voyage = Voyage(zone="china", length=10)
    history = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=15),
    ]
    rating_instance = create_rating(voyage, history)
    assert isinstance(rating_instance, ExperiencedChinaRating)

    # 중국 경험이 없는 경우
    voyage = Voyage(zone="west-indies", length=10)
    history = [
        HistoryItem(zone="west-indies", profit=5),
        HistoryItem(zone="east-indies", profit=15),
    ]
    rating_instance = create_rating(voyage, history)
    assert isinstance(rating_instance, Rating)
    assert not isinstance(rating_instance, ExperiencedChinaRating)


def test_rating_a():
    # "A" 등급이 나와야 하는 경우
    voyage = Voyage(zone="china", length=10)
    history = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=15),
        HistoryItem(zone="china", profit=-2),
        HistoryItem(zone="west-africa", profit=7),
        HistoryItem(zone="china", profit=10),
        HistoryItem(zone="east-indies", profit=12),
    ]
    assert rating(voyage, history) == "A"


def test_rating_b():
    # "B" 등급이 나와야 하는 경우
    voyage = Voyage(zone="west-indies", length=20)
    history = [
        HistoryItem(zone="west-indies", profit=-5),
        HistoryItem(zone="west-indies", profit=-15),
        HistoryItem(zone="west-indies", profit=-2),
    ]
    assert rating(voyage, history) == "B"


def test_voyage_risk():
    # 일반 Rating 클래스 테스트
    rating_inst = Rating(Voyage(zone="china", length=3), [])
    assert rating_inst.voyage_risk() == 5  # 1 + 0 + 0 + 4

    rating_inst = Rating(Voyage(zone="east-indies", length=6), [])
    assert rating_inst.voyage_risk() == 7  # 1 + 2 + 0 + 4

    rating_inst = Rating(Voyage(zone="west-indies", length=10), [])
    assert rating_inst.voyage_risk() == 5  # 1 + 2 + 2 + 0


def test_captain_history_risk():
    # 일반 Rating 클래스 테스트
    history_with_negative = [
        HistoryItem(zone="west-indies", profit=5),
        HistoryItem(zone="west-indies", profit=-5),
        HistoryItem(zone="west-indies", profit=-15),
    ]

    rating_inst = Rating(Voyage(zone="west-indies", length=10), history_with_negative)
    assert rating_inst.captain_history_risk() == 7  # 1 + 4 + 2

    # ExperiencedChinaRating 클래스 테스트
    history_with_china = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=-5),
        HistoryItem(zone="west-indies", profit=-15),
    ]

    rating_inst = ExperiencedChinaRating(
        Voyage(zone="china", length=10), history_with_china
    )
    assert rating_inst.captain_history_risk() == 5  # 1 + 4 + 2 - 2


def test_voyage_profit_factor():
    # 일반 Rating 클래스 테스트
    voyage_indies = Voyage(zone="east-indies", length=15)
    voyage_other = Voyage(zone="west-indies", length=15)

    history_no_china = [
        HistoryItem(zone="west-indies", profit=5),
        HistoryItem(zone="east-indies", profit=15),
    ] * 5  # 10 items total

    rating_inst = Rating(voyage_indies, history_no_china)
    assert rating_inst.voyage_profit_factor() == 3  # 2 + 0 + 1 + 1 - 1

    rating_inst = Rating(voyage_other, history_no_china)
    assert rating_inst.voyage_profit_factor() == 2  # 2 + 0 + 0 + 1 - 1

    # ExperiencedChinaRating 클래스 테스트
    voyage_china = Voyage(zone="china", length=10)

    history_with_china = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=15),
    ] * 6  # 12 items total

    rating_inst = ExperiencedChinaRating(voyage_china, history_with_china)
    assert rating_inst.voyage_profit_factor() == 7  # 2 + 1 + 0 + 1 + 3


def test_history_length_factor():
    # 일반 Rating 클래스 테스트
    history_short = [HistoryItem(zone="west-indies", profit=5)] * 7
    history_long = [HistoryItem(zone="west-indies", profit=5)] * 9

    rating_inst = Rating(Voyage(zone="west-indies", length=10), history_short)
    assert rating_inst.history_length_factor() == 0

    rating_inst = Rating(Voyage(zone="west-indies", length=10), history_long)
    assert rating_inst.history_length_factor() == 1

    # ExperiencedChinaRating 클래스 테스트
    history_medium = [HistoryItem(zone="china", profit=5)] * 9
    history_very_long = [HistoryItem(zone="china", profit=5)] * 11

    rating_inst = ExperiencedChinaRating(
        Voyage(zone="china", length=10), history_medium
    )
    assert rating_inst.history_length_factor() == 0

    rating_inst = ExperiencedChinaRating(
        Voyage(zone="china", length=10), history_very_long
    )
    assert rating_inst.history_length_factor() == 1


def test_voyage_length_factor():
    # 일반 Rating 클래스 테스트
    rating_inst = Rating(Voyage(zone="west-indies", length=14), [])
    assert rating_inst.voyage_length_factor() == 0

    rating_inst = Rating(Voyage(zone="west-indies", length=15), [])
    assert rating_inst.voyage_length_factor() == -1

    # ExperiencedChinaRating 클래스 테스트
    history_with_china = [HistoryItem(zone="china", profit=5)] * 11

    rating_inst = ExperiencedChinaRating(
        Voyage(zone="china", length=10), history_with_china
    )
    assert rating_inst.voyage_length_factor() == 0

    rating_inst = ExperiencedChinaRating(
        Voyage(zone="china", length=13), history_with_china
    )
    assert rating_inst.voyage_length_factor() == 1

    rating_inst = ExperiencedChinaRating(
        Voyage(zone="china", length=19), history_with_china
    )
    assert rating_inst.voyage_length_factor() == 0  # 1 + 1 - 1
