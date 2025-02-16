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
        data: dict  # 전체 데이터를 dict로 받도록 변경
    ):
        self._name = data['name']
        self._producers = []
        self._total_production = 0
        self._demand = data['demand']
        self._price = data['price']

        # producers 데이터로 Producer 인스턴스들 생성
        for producer in data['producers']:
            self.add_producer(Producer(self, producer))

    def add_producer(self, producer):
        self._producers.append(producer)
        self._total_production += producer.production

    @property
    def name(self):
        return self._name

    @property
    def producers(self):
        return self._producers.copy()  # JavaScript의 slice()와 같은 역할

    @property
    def total_production(self):
        return self._total_production

    @total_production.setter
    def total_production(self, arg):
        self._total_production = arg

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, arg):
        self._demand = int(arg)  # parseInt() 대신 int() 사용

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        self._price = int(arg)
