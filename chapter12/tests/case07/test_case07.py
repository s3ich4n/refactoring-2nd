from chapter12.src.case07.case07 import (
    Person,
    Male,
    Female,
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
