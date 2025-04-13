class ChargeCalculator:
    """
    요금 계산을 위한 클래스
    """

    def __init__(self, customer, usage, provider):
        """
        ChargeCalculator 클래스 초기화

        Args:
            customer: 고객 정보
            usage: 사용량
            provider: 서비스 제공자
        """
        self._customer = customer
        self._usage = usage
        self._provider = provider

    @property
    def charge(self):
        """
        총 요금 계산

        Returns:
            float: 계산된 총 요금
        """
        base_charge = self._customer.base_rate * self._usage
        return base_charge + self._provider.connection_charge
