from datetime import datetime

from chapter08.src.case03.case03 import (
    render_person,
    render_photo,
    photo_div,
    emit_photo_data,
)


def test_render_person():
    # 테스트 데이터 설정
    person = {
        "name": "홍길동",
        "photo": {
            "title": "여행 사진",
            "location": "서울",
            "date": datetime(2023, 5, 15),
        },
    }

    # 함수 실행
    result = render_person(None, person)

    # 결과 검증
    assert "<p>홍길동</p>" in result
    assert "<div>\n<p>제목: 여행 사진</p>\n</div>" in result
    assert "<p>title: 여행 사진</p>" in result
    assert "<p>location: 서울</p>" in result
    assert "<p>date: 2023-05-15</p>" in result


def test_render_photo():
    # 테스트 데이터 설정
    photo = {"title": "생일 파티", "location": "대전", "date": datetime(2023, 7, 20)}

    # 함수 실행
    result = render_photo(photo)

    # 결과 검증
    assert result == "<div>\n<p>제목: 생일 파티</p>\n</div>"


def test_photo_div():
    # 테스트 데이터 설정
    photo = {"title": "가족 사진", "location": "부산", "date": datetime(2023, 8, 10)}

    # 함수 실행
    result = photo_div(photo)

    # 결과 검증
    assert "<div>" in result
    assert "<p>title: 가족 사진</p>" in result
    assert "<p>location: 부산</p>" in result
    assert "<p>date: 2023-08-10</p>" in result
    assert "</div>" in result


def test_emit_photo_data():
    # 테스트 데이터 설정
    photo = {"location": "제주도", "date": datetime(2023, 12, 25)}

    # 함수 실행
    result = emit_photo_data(photo)

    # 결과 검증
    assert "<p>location: 제주도</p>" in result
    assert "<p>date: 2023-12-25</p>" in result
    assert result == "<p>location: 제주도</p>\n<p>date: 2023-12-25</p>"
