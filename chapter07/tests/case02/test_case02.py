from src.case02.case02 import Person, Course


def test_person_creation():
    person = Person("John")
    assert person.name == "John"
    assert person.courses == []


def test_course_creation():
    course = Course("Python Programming", True)
    assert course.name == "Python Programming"
    assert course.is_advanced == True


def test_adding_courses():
    person = Person("John")
    basic_course = Course("Basic Programming", False)
    advanced_course = Course("Advanced Python", True)

    person.courses = [basic_course, advanced_course]
    assert len(person.courses) == 2
    assert person.courses[0].name == "Basic Programming"
    assert person.courses[1].name == "Advanced Python"


def test_counting_advanced_courses():
    person = Person("John")
    courses = [
        Course("Basic Programming", False),
        Course("Advanced Python", True),
        Course("Advanced AI", True),
        Course("Web Basics", False),
    ]
    person.courses = courses

    assert person.get_num_advanced_courses() == 2
