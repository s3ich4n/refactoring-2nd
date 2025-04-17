from chapter12.src.case07.case07 import (
    Person,
    Male,
    Female,
    load_from_input,
    User,
)


def test_person_class():
    # 기본 Person 클래스 테스트
    person = Person.create_person("홍길동")
    assert person.name == "홍길동"
    assert person.gender_code == "X"


def test_male_class():
    # Male 서브클래스 테스트
    male = Male.create_person("김철수", "M")
    assert male.name == "김철수"
    assert male.gender_code == "M"

    # Male이 Person의 서브클래스인지 확인
    assert isinstance(male, Person)


def test_female_class():
    # Female 서브클래스 테스트
    female = Female.create_person("이영희", "F")
    assert female.name == "이영희"
    assert female.gender_code == "F"

    # Female이 Person의 서브클래스인지 확인
    assert isinstance(female, Person)


def test_polymorphism():
    # 다형성 테스트
    people = [
        Person.create_person("익명"),
        Person.create_person("홍길동", "M"),
        Person.create_person("성춘향", "F"),
    ]

    expected_codes = ["X", "M", "F"]

    for person, expected_code in zip(people, expected_codes):
        assert person.gender_code == expected_code


def test_load_from_input():
    # 원본 로드 함수 테스트
    test_data = [
        User(name="김철수", gender="M"),
        User(name="이영희", gender="F"),
        User(name="무명", gender=None),
    ]

    people = load_from_input(test_data)

    assert len(people) == 3
    assert isinstance(people[0], Person)
    assert isinstance(people[1], Person)
    assert isinstance(people[2], Person)
    assert people[0].name == "김철수"
    assert people[1].name == "이영희"
    assert people[2].name == "무명"
