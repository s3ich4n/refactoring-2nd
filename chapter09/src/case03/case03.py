class SomeClass:
    def __init__(self):
        self._production = 0  # 초기값은 예시를 위해 추가했습니다
        self._adjustments = []  # 초기값은 예시를 위해 추가했습니다

    @property
    def production(self):
        return sum(adjustment.amount for adjustment in self._adjustments)

    def apply_adjustment(self, an_adjustment):
        self._adjustments.append(an_adjustment)
        self._production += an_adjustment.amount
