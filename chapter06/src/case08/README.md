# 6.8 매개변수 객체 만들기

_Introduce Parameter Object_

## 개요

Before

```python
def amount_invoiced(start_date, end_date): ...
def amount_received(start_date, end_date): ...
def amount_overdue(start_date, end_date): ...
```

After

```python
@dataclass
class DateRange:
    start_date: datetime
    end_date: datetime


def amount_invoiced(date_range: DateRange): ...
def amount_received(date_range: DateRange): ...
def amount_overdue(date_range: DateRange): ...
```

## 배경

데이터 항목이 몰려다니는 경우 데이터 구조로 묶어준다.

이렇게 묶어주면 데이터 사이의 관계가 매우 명확해지고, 매개변수 수도 줄고, 일관성도 높여준다.

마틴 파울러가 소개하는 장점은 코드가 더 근본적으로 바뀌는 장점에 있다고 소개한다.
이런 데이터 구조를 활용하며 시스템을 쌓아올릴 때, 필요하면 함수로 나아가 클래스로 합쳐서 만들 수도 있다.
이러면 코드의 큰 그림을 다시 그릴 수 있다. 놀랍게도 그 시작점은 데이터를 묶어주는 것 부터다.

## 절차

1. 적당한 데이터구조가 안만들어져 있으면 일단 만든다 <br />
→ 마틴 파울러는 클래스를 선호한다. 동작과 함께 묶기 쉽기 때문이다. 데이터 구조를 VO로 만든다.
2. 테스트한다
3. 함수 선언 바꾸기(6.5)로 새 데이터 구조를 매개변수로 추가한다
4. 테스트한다
5. 함수 호출 시 새 데이터 구조 인스턴스를 넘기도록 수정한다. 하나 바꿀 때마다 테스트한다
6. 기존 매개변수를 쓰던 코드를 새 데이터 구조의 원소를 쓰도록 바꾼다
7. 다 바꿨다면 기존 매개변수를 지우고 테스트한다.

## 예시
