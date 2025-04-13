from chapter11.src.case12.case12 import (
    local_shipping_rules,
    ShippingRules,
    CountryData,
)


class TestLocalShippingRules:
    def setup_method(self):
        """각 테스트 메서드 실행 전에 호출되는 설정 메서드"""
        self.country_data = CountryData()
        # 테스트용 데이터 설정
        self.country_data.shipping_rules = {
            "US": {"tax": 0.07, "shipping_cost": 15},
            "CA": {"tax": 0.13, "shipping_cost": 20},
            "UK": {"tax": 0.20, "shipping_cost": 25},
        }

    def test_local_shipping_rules_with_existing_country(self):
        """존재하는 국가 코드에 대한 테스트"""
        # 존재하는 국가 코드로 테스트
        result = local_shipping_rules("US", self.country_data)

        # 반환된 객체 타입 확인
        assert isinstance(result, ShippingRules)
        # 반환된 데이터 확인
        assert result.data == {"tax": 0.07, "shipping_cost": 15}

        # 다른 국가 코드로 테스트
        result = local_shipping_rules("UK", self.country_data)
        assert isinstance(result, ShippingRules)
        assert result.data == {"tax": 0.20, "shipping_cost": 25}

    def test_local_shipping_rules_with_nonexistent_country(self):
        """존재하지 않는 국가 코드에 대한 테스트"""
        # 존재하지 않는 국가 코드로 테스트 - 예외가 발생해야 함
        assert -23 == local_shipping_rules("FR", self.country_data)

    def test_local_shipping_rules_with_empty_country(self):
        """빈 국가 코드에 대한 테스트"""
        assert -23 == local_shipping_rules("", self.country_data)

    def test_local_shipping_rules_with_none_country(self):
        """None 국가 코드에 대한 테스트"""
        assert -23 == local_shipping_rules(None, self.country_data)
