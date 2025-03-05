import pytest
from src.case09.case09 import (
    found_person_old,
    found_person_new,
)


@pytest.mark.parametrize(
    "people, expected",
    [
        ([], ""),  # 빈 리스트일 때
        (["Sam", "Nick"], ""),  # 후보가 없을 때
        (["Don", "John", "Kent"], "Don"),  # 여러 후보가 있어도 첫 번째 발견된 이름 반환
        (["Alice", "Kent", "Bob"], "Kent"),  # 중간에 Kent가 있을 때
        (["John"], "John"),  # 단일 후보
        (["Don", "Kent", "John"], "Don"),  # Don이 가장 먼저 오는 경우
    ],
)
def test_found_person_old(people, expected):
    """found_person_old가 주어진 people 리스트에서 올바른 결과를 반환하는지 테스트"""
    assert found_person_old(people) == expected


@pytest.mark.parametrize(
    "people, expected",
    [
        ([], ""),
        (["Sam", "Nick"], ""),
        (["Don", "John", "Kent"], "Don"),
        (["Alice", "Kent", "Bob"], "Kent"),
        (["John"], "John"),
        (["Don", "Kent", "John"], "Don"),
    ],
)
def test_found_person_new(people, expected):
    """found_person_new가 주어진 people 리스트에서 올바른 결과를 반환하는지 테스트"""
    assert found_person_new(people) == expected


@pytest.mark.parametrize(
    "people, expected",
    [
        ([], ""),
        (["Sam", "Nick"], ""),
        (["Don", "John", "Kent"], "Don"),
        (["Alice", "Kent", "Bob"], "Kent"),
        (["John"], "John"),
        (["Don", "Kent", "John"], "Don"),
    ],
)
def test_two_algorithm_same_result(people, expected):
    assert found_person_old(people) == found_person_new(people) == expected
