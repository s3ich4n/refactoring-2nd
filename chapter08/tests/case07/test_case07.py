from chapter08.src.case07.case07 import Person, calculate_stats


def test_calculate_stats_with_people():
    # given
    people = [
        Person(age=30, salary=50000),
        Person(age=25, salary=45000),
        Person(age=35, salary=60000),
    ]

    # when
    result = calculate_stats(people)

    # then
    assert result == "youngestAge: 25, totalSalary: 155000"


def test_calculate_stats_with_empty_list():
    # given
    people = []

    # when
    result = calculate_stats(people)

    # then
    assert result == "youngestAge: inf, totalSalary: 0"


def test_calculate_stats_with_one_person():
    # given
    people = [Person(age=40, salary=70000)]

    # when
    result = calculate_stats(people)

    # then
    assert result == "youngestAge: 40, totalSalary: 70000"
