from src.case05.case_05_2 import (
    in_new_england,
    Customer,
    Address,
)


def test_case05_2():
    customers = [
        Customer(Address("MA")),  # 매사추세츠 - 뉴잉글랜드
        Customer(Address("NY")),  # 뉴욕 - 뉴잉글랜드 아님
        Customer(Address("CT")),  # 코네티컷 - 뉴잉글랜드
        Customer(Address("FL")),  # 플로리다 - 뉴잉글랜드 아님
    ]

    new_englanders = [c for c in customers if in_new_england(c.address.state)]

    assert len(new_englanders) == 2
