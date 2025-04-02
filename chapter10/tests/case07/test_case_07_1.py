from unittest.mock import patch

from chapter10.src.case07.case_07_1 import search_villains


def test_no_villains():
    """악당이 없는 경우 경고가 발생하지 않아야 함"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains(["batman", "superman", "wonderwoman"])
        mock_alert.assert_not_called()


def test_one_joker():
    """리스트에 joker가 한 명 있는 경우 경고가 한 번 발생해야 함"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains(["batman", "joker", "superman"])
        assert mock_alert.call_count == 1


def test_one_saruman():
    """리스트에 saruman이 한 명 있는 경우 경고가 한 번 발생해야 함"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains(["batman", "saruman", "superman"])
        assert mock_alert.call_count == 1


def test_both_villains():
    """두 악당이 모두 있는 경우 경고는 한 번만 발생해야 함 (found 플래그 때문)"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains(["batman", "joker", "saruman", "superman"])
        assert mock_alert.call_count == 1


def test_joker_appears_twice():
    """joker가 여러 번 나타나도 경고는 한 번만 발생"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains(["batman", "joker", "superman", "joker"])
        assert mock_alert.call_count == 1


def test_saruman_first():
    """saruman이 joker보다 먼저 나타나는 경우"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains(["batman", "saruman", "joker", "superman"])
        assert mock_alert.call_count == 1


def test_empty_list():
    """빈 리스트의 경우 경고가 발생하지 않아야 함"""
    with patch("chapter10.src.case07.case_07_1.send_alert") as mock_alert:
        search_villains([])
        mock_alert.assert_not_called()
