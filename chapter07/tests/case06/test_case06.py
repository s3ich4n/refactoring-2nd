# tests/test_tracking.py
import pytest
from src.case06.case06 import (
    Shipment,
)


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
    shipment = Shipment()
    shipment.shipping_company = company
    shipment.tracking_number = number

    assert shipment.display() == expected_display


def test_shipment_basic():
    """
    Shipment의 요소가 제대로 포함되어있나 확인
    """
    shipment = Shipment()

    # 기본적으로 None인 경우 확인
    assert shipment.tracking_info is None

    shipment.shipping_company = "FedEx"
    shipment.tracking_number = "654321"

    # Shipment에 세팅
    assert shipment.display() == "FedEx: 654321"


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

    shipment.shipping_company = company
    shipment.tracking_number = number

    assert shipment.display() == expected_info
