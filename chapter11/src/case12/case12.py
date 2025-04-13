class CountryNotFoundException(Exception):
    pass


class ShippingRules:
    """배송 규칙을 나타내는 클래스"""

    def __init__(self, data):
        """
        배송 규칙 초기화

        Args:
            data: 배송 규칙 데이터
        """
        self.data = data


class CountryData:
    """국가 데이터를 관리하는 클래스"""

    def __init__(self):
        """국가 데이터 초기화"""
        self.shipping_rules = {}


def local_shipping_rules(country, country_data):
    """
    특정 국가의 배송 규칙을 조회하는 함수

    Args:
        country (str): 국가 코드
        country_data (CountryData): 국가 데이터 객체

    Returns:
        ShippingRules: 해당 국가의 배송 규칙

    """
    data = country_data.shipping_rules.get(country)
    if data:
        return ShippingRules(data)
    else:
        raise CountryNotFoundException(
            f"국가 '{country}'에 대한 배송 규칙을 찾을 수 없습니다."
        )
