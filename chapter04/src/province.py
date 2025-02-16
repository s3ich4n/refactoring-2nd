"""
생산 계획은 각 지역의 수요와 가격으로 구성됨
지역에 위치한 생산자들은 각기 제품을 특정 가격으로 특정 수량만큼 생산가능
UI는 생산자별로 제품을 모두 판매했을 때 얻을 수 있는 수익도 보여줌
화면 맨 아래에는 (수요에서 총 생산량을 뺀) 생산 부족분과 현재 계획에서 거둘 수 있는 총 수익을 보여줌
사용자는 UI에서 수요, 가격, 생산자별 생산량, 비용을 조정해가며 그에 따른 생산 부족분과 총수익을 확인할 수 있음
사용자가 화면에서 숫자를 변경할 때마다 관련 값들이 갱신됨
"""

from chapter04.src.producer import Producer


class Province:
    def __init__(
        self,
        name: str,
        producers: list[dict],
        demand: int,
        price: int,
    ):
        self._name = name
        self._producers = []
        self._total_production = 0
        self._demand = demand
        self._price = price

        for producer in producers:
            self.add_producer(Producer(**producer))

    def add_producer(self, producer):
        self._producers.append(producer)
        self._total_production += producer.production

    @property
    def producers(self):  # getter 먼저 정의
        return self._producers

    @producers.setter
    def producers(self, producers): ...
