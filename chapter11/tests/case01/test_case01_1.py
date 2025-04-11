import io
import sys
from unittest.mock import patch

from chapter11.src.case01.case01 import (
    find_villains,
    send_alert,
)


def test_no_villains():
    """악당이 없는 경우 None을 반환하고 경고가 발생하지 않아야 함"""
    found = find_villains(["batman", "superman", "wonderwoman"])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found is None
    # None을 send_alert에 전달하면 'ALERT: Villain found! - None'이 출력됨
    assert captured_output.getvalue() == "ALERT: Villain found! - None\n"


def test_one_joker():
    """리스트에 joker가 한 명 있는 경우 'joker'를 반환하고 경고가 발생해야 함"""
    found = find_villains(["batman", "joker", "superman"])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found == "joker"
    assert captured_output.getvalue() == "ALERT: Villain found! - joker\n"


def test_one_saruman():
    """리스트에 saruman이 한 명 있는 경우 'saruman'을 반환하고 경고가 발생해야 함"""
    found = find_villains(["batman", "saruman", "superman"])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found == "saruman"
    assert captured_output.getvalue() == "ALERT: Villain found! - saruman\n"


def test_both_villains():
    """두 악당이 모두 있는 경우 먼저 발견된 악당을 반환하고 경고가 발생해야 함"""
    found = find_villains(["batman", "joker", "saruman", "superman"])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found == "joker"
    assert captured_output.getvalue() == "ALERT: Villain found! - joker\n"


def test_joker_appears_twice():
    """joker가 여러 번 나타나도 첫 번째 발견된 joker만 반환하고 경고가 발생해야 함"""
    found = find_villains(["batman", "joker", "superman", "joker"])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found == "joker"
    assert captured_output.getvalue() == "ALERT: Villain found! - joker\n"


def test_saruman_first():
    """saruman이 joker보다 먼저 나타나는 경우 saruman을 반환하고 경고가 발생해야 함"""
    found = find_villains(["batman", "saruman", "joker", "superman"])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found == "saruman"
    assert captured_output.getvalue() == "ALERT: Villain found! - saruman\n"


def test_empty_list():
    """빈 리스트의 경우 None을 반환하고 경고가 발생하지 않아야 함"""
    found = find_villains([])
    
    # stdout 캡처
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    send_alert(found)
    
    # stdout 복원
    sys.stdout = sys.__stdout__
    
    assert found is None
    # None을 send_alert에 전달하면 'ALERT: Villain found! - None'이 출력됨
    assert captured_output.getvalue() == "ALERT: Villain found! - None\n"


# unittest.mock을 사용한 대체 방법 (위의 테스트와 동일한 결과)
def test_with_mock():
    """unittest.mock을 사용한 테스트 방법"""
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        found = find_villains(["batman", "joker", "superman"])
        send_alert(found)
        assert found == "joker"
        assert fake_stdout.getvalue() == "ALERT: Villain found! - joker\n"
