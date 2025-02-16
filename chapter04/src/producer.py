class Producer:
    def __init__(
        self,
        province,  # aProvince에 해당
        data: dict  # data 객체를 통째로 받음
    ):
        self._province = province
        self._cost = data.get('cost')
        self._name = data.get('name')
        self._production = data.get('production', 0)  # production || 0 과 동일

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, arg):
        self._cost = int(arg)

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, amount_str):
        try:
            amount = int(amount_str)
        except (ValueError, TypeError):
            amount = 0  # Number.isNaN(amount)와 동일한 효과

        new_production = amount
        self._province.total_production += new_production - self._production
        self._production = new_production
