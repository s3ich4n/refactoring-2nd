from chapter12.src.case07.case07 import (
    Person,
    Male,
    Female,
    load_from_input,
)


def test_person_class():
    # 기본 Person 클래스 테스트
    person = Person("홍길동")
    assert person.name == "홍길동"
    assert person.gender_code == "X"


def test_male_class():
    # Male 서브클래스 테스트
    male = Male("김철수")
    assert male.name == "김철수"
    assert male.gender_code == "M"

    # Male이 Person의 서브클래스인지 확인
    assert isinstance(male, Person)


def test_female_class():
    # Female 서브클래스 테스트
    female = Female("이영희")
    assert female.name == "이영희"
    assert female.gender_code == "F"

    # Female이 Person의 서브클래스인지 확인
    assert isinstance(female, Person)


def test_polymorphism():
    # 다형성 테스트
    people = [Person("익명"), Male("홍길동"), Female("성춘향")]

    expected_codes = ["X", "M", "F"]

    for person, expected_code in zip(people, expected_codes):
        assert person.gender_code == expected_code


def test_load_from_input():
    # 원본 로드 함수 테스트
    test_data = [
        {"name": "김철수", "gender": "M"},
        {"name": "이영희", "gender": "F"},
        {"name": "무명", "gender": None},
    ]

    people = load_from_input(test_data)

    assert len(people) == 3
    assert isinstance(people[0], Male)
    assert isinstance(people[1], Female)
    assert isinstance(people[2], Person)
    assert people[0].name == "김철수"
    assert people[1].name == "이영희"
    assert people[2].name == "무명"
