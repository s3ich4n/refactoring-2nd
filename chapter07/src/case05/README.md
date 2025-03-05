# 7.5 클래스 추출하기

_Extract Class_

## 개요

Before

```python
class Person:
    def __init__(self, office_area_code, office_number):
        self._office_area_code = office_area_code
        self._office_number = office_number

    @property
    def office_area_code(self):
        return self._office_area_code

    @property
    def office_number(self):
        return self._office_number
```

After

```python
class Person:
    def __init__(self, telephone_number):
        self._telephone_number = telephone_number

    @property
    def office_area_code(self):
        return self._telephone_number.area_code

    @property
    def office_number(self):
        return self._telephone_number.number


class TelephoneNumber:
    def __init__(self, area_code, number):
        self._area_code = area_code
        self._number = number

    @property
    def area_code(self):
        return self._area_code

    @property
    def number(self):
        return self._number
```

## 배경

"클래스는 명확하게 추상화하고 소수의 주어진 역할만을 처리하도록 하자." 가 원래 가이드라인이지만 인생사 그렇게 흘러가지 않는다.
연산을 넣고 데이터도 보강하다보면 점점 커지는데, 그러면 클래스가 비대해진다.

메소드와 데이터가 너무 많으면 이해하기 쉽지 않으니 분리하는 것이 좋다.
일부 데이터와 메소드를 따로 묶을 수 있겠다 싶으면 분리하기 좋은 신호다.
함께 변경되는 일이 많거나 서로 의존하는 데이터도 분리한다.
이럴 땐 데이터나 메소드 일부를 빼보고 자문해보자. 빼고서도 다른 필드나 메소드들에 문제가 없다면 ㅇㅋ

서브클래스가 만들어지는 방식에서 징후가 나타날 수 있다. 작은 기능 일부를 위한 서브클래스, 확장할 기능이 무엇이냐에 따라 서브클래스가 다르게 만들어진다면 클래스를 나누라는 의미.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 클래스의 역할을 분리할 방법을 정한다
2. 분리될 역할을 담당할 클래스를 새로 만든다 <br />
   → 원래 클래스에 남은 역할과 클래스의 이름이 어울리지 않는다면 적절히 바꾼다
3. 원래 클래스의 생성자에서 새로운 클래스의 인스턴스를 생성하여 필드에 저장한다
4. 분리될 역할에 필요한 필드들을 새 클래스로 옮긴다(필드 옮기기, 8.2절). 하나씩 옮기고 테스트한다
5. 메소드들도 새 클래스로 옮긴다(함수 옮기기, 8.1절). 저수준 메소드(호출당하는 일이 많은 메소드)부터 옮긴다. 하나씩 옮기고 테스트한다
6. 양쪽 클래스의 인터페이스를 살펴보면서 불필요한 메소드를 제거하고, 이름도 새 환경에 맞게 바꾼다.
7. 새 클래스를 외부로 노출할지 정한다. 노출하려는 경우 새 클래스에 참조를 값으로 바꾸기(9.4절)를 적용할지 고민한다.

## 예시

전화번호만 별도로 빼보자. (07ebffb8c26d91622dc93de7ecb16c7b8fe1e5e9)

뺀 이름에서 포괄적인 요소를 바꾸고 테스트코드도 갈아엎는다. (f0797e280a91562fe474e00aa2aa303e36c8bacb)
