from datetime import (
    datetime,
    timedelta,
)
from io import StringIO

import pytest

from chapter08.src.case04.case04_1 import (
    Photo,
    Person,
    render_person,
    list_recent_photos,
    emit_photo_data,
)


@pytest.fixture
def sample_photo():
    """테스트용 사진 객체를 생성합니다."""
    return Photo("My Vacation", "Paris", datetime.now())


@pytest.fixture
def sample_person(sample_photo):
    """테스트용 사람 객체를 생성합니다."""
    return Person("John Doe", sample_photo)


@pytest.fixture
def sample_photos():
    """테스트용 사진 목록을 생성합니다."""
    return [
        Photo(
            "Vacation",
            "Paris",
            datetime.now(),
        ),
        Photo(
            "Work Trip",
            "New York",
            datetime.now().replace(day=datetime.now().day) - timedelta(days=10),
        ),
        Photo(
            "Old Trip",
            "Tokyo",
            datetime.now().replace(year=datetime.now().year) - timedelta(days=10),
        ),
    ]


def test_render_person(sample_person):
    """render_person 함수를 테스트합니다."""
    output = StringIO()
    render_person(output, sample_person)
    result = output.getvalue()

    # 결과에 필요한 정보가 포함되어 있는지 확인
    assert sample_person.name in result
    assert sample_person.photo.title in result
    assert sample_person.photo.location in result
    assert "date" in result


def test_list_recent_photos(sample_photos):
    """list_recent_photos 함수를 테스트합니다."""
    output = StringIO()
    list_recent_photos(output, sample_photos)
    result = output.getvalue()

    # 예상 결과의 수를 확인
    recent_photos = [
        p for p in sample_photos if p.date > datetime.now() - timedelta(days=30)
    ]
    assert result.count("<div>") == len(recent_photos)

    # 내용 확인
    for photo in recent_photos:
        assert photo.title in result
        assert photo.location in result


def test_emit_photo_data(sample_photo):
    """emit_photo_data 함수를 테스트합니다."""
    output = StringIO()
    emit_photo_data(output, sample_photo)
    result = output.getvalue()

    # 모든 필요한 정보가 포함되어 있는지 확인
    #   이때, location은 요구사항에서 제외되었다고 가정
    assert f"title: {sample_photo.title}" in result
    assert "date:" in result
