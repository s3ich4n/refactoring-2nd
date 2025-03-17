from chapter09.src.case04.case04 import Person


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

    # 내부 객체 직접 변경
    person._telephone_number.area_code = "031"
    assert person.office_area_code == "031"
