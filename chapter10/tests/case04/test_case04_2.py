from chapter10.src.case04.case04_2 import (
    Voyage,
    HistoryItem,
    rating,
    voyage_risk,
    captain_history_risk,
    has_china,
    voyage_profit_factor,
)


def test_rating_a():
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
    voyage = Voyage(zone="west-indies", length=20)
    history = [
        HistoryItem(zone="west-indies", profit=-5),
        HistoryItem(zone="west-indies", profit=-15),
        HistoryItem(zone="west-indies", profit=-2),
    ]
    assert rating(voyage, history) == "B"


def test_voyage_risk():
    assert voyage_risk(Voyage(zone="china", length=3)) == 5  # 1 + 0 + 0 + 4
    assert voyage_risk(Voyage(zone="east-indies", length=6)) == 7  # 1 + 2 + 0 + 4
    assert voyage_risk(Voyage(zone="west-indies", length=10)) == 5  # 1 + 2 + 2 + 0


def test_captain_history_risk():
    voyage = Voyage(zone="china", length=10)
    history_with_china = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=-5),
        HistoryItem(zone="west-indies", profit=-15),
    ]
    history_no_china = [
        HistoryItem(zone="west-indies", profit=5),
        HistoryItem(zone="west-indies", profit=-5),
        HistoryItem(zone="west-indies", profit=-15),
    ]

    assert captain_history_risk(voyage, history_with_china) == 5  # 1 + 4 + 2 - 2
    assert captain_history_risk(voyage, history_no_china) == 7  # 1 + 4 + 2 + 0


def test_has_china():
    history_with_china = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=15),
    ]
    history_no_china = [
        HistoryItem(zone="west-indies", profit=5),
        HistoryItem(zone="east-indies", profit=15),
    ]

    assert has_china(history_with_china) is True
    assert has_china(history_no_china) is False


def test_voyage_profit_factor():
    voyage_china = Voyage(zone="china", length=10)
    voyage_indies = Voyage(zone="east-indies", length=15)
    voyage_other = Voyage(zone="west-indies", length=15)

    # 12 items total
    history_with_china = [
        HistoryItem(zone="china", profit=5),
        HistoryItem(zone="west-indies", profit=15),
    ] * 6

    # 10 items total
    history_no_china = [
        HistoryItem(zone="west-indies", profit=5),
        HistoryItem(zone="east-indies", profit=15),
    ] * 5

    # China voyage with China history
    #   2 + 1 + 0 + 3 + 1 + 0 + 0
    assert voyage_profit_factor(voyage_china, history_with_china) == 7

    # East Indies voyage with no China history
    #   2 + 0 + 1 + 0 + 1 + 0
    assert voyage_profit_factor(voyage_indies, history_no_china) == 3

    # Other voyage with no China history
    #   2 + 0 + 1 + 0 + 1 - 1
    assert voyage_profit_factor(voyage_other, history_no_china) == 2
