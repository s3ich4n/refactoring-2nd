from chapter09.src.case04.case04 import (
    Person,
    TelephoneNumber,
)


def test_person_telephone():
    # Person 객체 생성
    person = Person()

    # 속성 설정
    person.office_area_code = "02"
    person.office_number = "1234-5678"

    # 속성 확인
    assert person.office_area_code == "02"
    assert person.office_number == "1234-5678"

    # TelephoneNumber 객체가 올바르게 업데이트 되었는지 확인
    assert person._telephone_number.area_code == "02"
    assert person._telephone_number.number == "1234-5678"

    # 불변 객체는 직접 수정할 수 없음 - 아래 테스트는 실패함
    # person._telephone_number.area_code = "031"  # AttributeError 발생

    # 대신 setter를 통해 새 객체로 교체
    old_number = person._telephone_number.number
    person.office_area_code = "031"
    assert person.office_area_code == "031"
    assert person.office_number == old_number  # 번호는 유지되어야 함


def test_telephone_number_equality():
    t1 = TelephoneNumber("312", "555-0142")
    t2 = TelephoneNumber("312", "555-0142")

    assert t1 == t2
