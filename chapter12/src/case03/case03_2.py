class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def is_privileged(self):
        return False

    def assign_car(self):
        # 차량 할당 로직
        pass


class Manager(Employee):
    def __init__(self, name, grade):
        super().__init__(name)
        self._grade = grade
        if self.is_privileged:
            self.assign_car()  # 모든 하위 클래스가 이 작업을 수행

    @property
    def is_privileged(self):
        return self._grade > 4
