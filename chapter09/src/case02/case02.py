# 이렇게 쓰던 값이 코드베이스 곳곳에 쓰이면 진짜 실수하기 쉽다.
#   그럴 때 바로 클래스로 캡슐화를 실시한다.
# organization = {"name": "Acme Gooseberry", "country": "GB"}


class Organization:
    def __init__(self, name, country):
        self._name = name
        self._country = country


organization_1 = Organization("Acme Gooseberry", "GB")
