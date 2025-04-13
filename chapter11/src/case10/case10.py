class ChargeCalculator:
    """
    요금 계산을 위한 클래스
    """

    def __init__(self):
        """
        ChargeCalculator 클래스 초기화

        Args:
        """
        ...

    def charge(self, customer, usage, provider):
        """
        총 요금 계산

        Args:
            customer: 고객 정보
            usage: 사용량
            provider: 서비스 제공자

        Returns:
            float: 계산된 총 요금
        """
        base_charge = customer.base_rate * usage
        return base_charge + provider.connection_charge
