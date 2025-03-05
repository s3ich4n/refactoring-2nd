# tests/test_tracking.py
import pytest
from src.case06.case06 import (
    TrackingInformation,
    Shipment,
)


def test_tracking_information_basic():
    """
    TrackingInformation을 생성하고,
    shippingCompany와 trackingNumber를 세터로 설정한 뒤
    제대로 게터로 반환되는지, display 문자열이 정상인지 검증
    """
    tracking = TrackingInformation()

    # 초기 상태 확인 (None)
    assert tracking.shipping_company is None
    assert tracking.tracking_number is None

    # 세터로 값 설정
    tracking.shipping_company = "FedEx"
    tracking.tracking_number = "123456"

    # 게터 및 display 확인
    assert tracking.shipping_company == "FedEx"
    assert tracking.tracking_number == "123456"
    assert tracking.display == "FedEx: 123456"


@pytest.mark.parametrize(
    "company, number, expected_display",
    [
        ("UPS", "999999", "UPS: 999999"),
        ("DHL", "ABC123", "DHL: ABC123"),
        ("KoreaPost", "987654", "KoreaPost: 987654"),
    ],
)
def test_tracking_information_param(company, number, expected_display):
    """
    여러 케이스를 파라미터라이즈하여 TrackingInformation 테스트
    """
    tracking = TrackingInformation()
    tracking.shipping_company = company
    tracking.tracking_number = number

    assert tracking.display == expected_display


def test_shipment_basic():
    """
    Shipment에 TrackingInformation을 연결해보고,
    trackingInfo 프로퍼티가 올바른 문자열을 반환하는지 확인
    """
    shipment = Shipment()

    # 기본적으로 None인 경우 확인
    assert shipment.tracking_info is None

    # TrackingInformation 생성 및 설정
    tracking = TrackingInformation()
    tracking.shipping_company = "FedEx"
    tracking.tracking_number = "654321"

    # Shipment에 세팅
    shipment.tracking_information = tracking
    assert shipment.tracking_info == "FedEx: 654321"


@pytest.mark.parametrize(
    "company, number, expected_info",
    [
        ("CJ", "123123", "CJ: 123123"),
        ("FedEx", "000111", "FedEx: 000111"),
    ],
)
def test_shipment_param(company, number, expected_info):
    """
    Shipment과 TrackingInformation을 함께 사용했을 때
    다양한 입력값에 대해 trackingInfo가 올바른지 테스트
    """
    shipment = Shipment()
    tracking = TrackingInformation()

    tracking.shipping_company = company
    tracking.tracking_number = number

    shipment.tracking_information = tracking

    assert shipment.tracking_info == expected_info
