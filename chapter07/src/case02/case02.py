import copy


class Person:
    def __init__(self, name):
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return copy.copy(self._courses)

    def add_course(self, course):
        self._courses.append(course)

    def remove_course(self, course):
        try:
            self._courses.remove(course)
        except ValueError:
            raise ValueError("Course not found")

    # 가급적 안 쓰는 방안으로.
    # @courses.setter
    # def courses(self, course_list):
    #     self._courses = copy.copy(course_list)

    def get_num_advanced_courses(self):
        return len([course for course in self.courses if course.is_advanced])


class Course:
    def __init__(self, name, is_advanced):
        self._name = name
        self._is_advanced = is_advanced

    @property
    def name(self):
        return self._name

    @property
    def is_advanced(self):
        return self._is_advanced
