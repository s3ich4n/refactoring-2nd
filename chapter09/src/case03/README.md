# 9.3 파생 변수를 질의 함수로 바꾸기

_Replace Derived Variable with Query_

## 개요

Before

```python
class SomeClass:
    def __init__(self):
        self._discounted_total = 0  # 초기값은 예시를 위해 추가했습니다
        self.discount = 0  # 초기값은 예시를 위해 추가했습니다

    @property
    def discounted_total(self):
        return self._discounted_total

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, a_number):
        old = self.discount
        self._discount = a_number
        self._discounted_total += old - a_number
```

After

```python
class SomeClass:
    def __init__(self):
        self.base_total = 0  # 초기값은 예시를 위해 추가했습니다
        self._discount = 0  # 초기값은 예시를 위해 추가했습니다

    @property
    def discounted_total(self):
        return self.base_total - self._discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, a_number):
        self._discount = a_number
```

## 배경

가변 데이터로 인해 서로다른 코드가 이상하게 엮이는 경우는 잡기도 어렵다. 완전히 배제할 수 없다면 최대한 가변 데이터의 유효범위를 줄여보자.

값을 쉽게계산해낼 수 있는 변수는 모두 제거할 수 있다. 이로 인해 계산 과정을 보여주는 코드 자체가 데이터의 의미를 더 분명히 드러내기도 하며 변경된 값을 놓치고 결과변수에 반영하지 않는 실수를 막아준다.

피연산자가 불변이면 계산 결과도 일정하므로 불변으로 만들 수 있다. 그래서 새로운 데이터 구조를 생성하는 변형연산(_transformation operation_) 이라면 계산코드로 대체할 수 있더라도 그대로 둘 수 있다.

변형연산의 종류는 아래와 같다:
1. 데이터 구조를 감싸며 그 데이터에 기초하여 계산한 결과를 속성으로 제공하는 객체
2. 데이터 구조를 받아 다른 데이터 구조로 변환해 반환하는 함수

소스 데이터가 가변이고 파생 데이터 구조의 수명을 관리해야되면 객체를 쓰는게 훨씬 낫고, 소스데이터가 불변이거나 파생 데이터를 쓰다 버릴거면 아무렇게나 써도 무방하다.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 변수값이 갱신되는 지점을 모두 찾는다. 필요하면 변수 쪼개기(9.1절)를 활용해 각 갱신지점에서 변수를 분리한다
2. 해당 변수의 값을 계산해주는 함수를 만든다
3. 해당 변수가 사용되는 모든 곳에 어서션을 추가(10.6절)해서 함수의 계산결과가 변수의 값과 같은지 확인한다 <br />
→ 필요하면 변수 캡슐화하기(6.6절)를 적용하여 어서션이 들어갈 장소를 마련한다
4. 테스트한다
5. 변수를 읽는 코드를 모두 함수로 대체한다
6. 테스트한다
7. 변수를 선언하고 갱신하는 코드를 죽은 코드 제거하기(8.9절)로 없앤다

## 예시

