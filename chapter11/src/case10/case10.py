class Customer:
    def __init__(self, base_rate):
        self.base_rate = base_rate


class ChargeCalculator:
    """
    요금 계산을 위한 클래스
    """

    def __init__(self, usage, provider):
        """
        ChargeCalculator 클래스 초기화

        Args:
            usage: 사용량
            provider: 서비스 제공자
        """
        self._usage = usage
        self._provider = provider

    def charge(self, customer, usage, provider):
        """
        총 요금 계산

        Args:
            customer: 고객 정보

        Returns:
            float: 계산된 총 요금
        """
        base_charge = customer.base_rate * self._usage
        return base_charge + self._provider.connection_charge
