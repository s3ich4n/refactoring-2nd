# 9.4 참조를 값으로 바꾸기

_Change Reference to Value_

## 개요

Before

```python
class Product:
    def __init__(self):
        self._price = None  # 예시를 위해 초기화
    
    def apply_discount(self, arg):
        self._price.amount -= arg
```

After

```python
class Product:
    def __init__(self):
        self._price = None  # 예시를 위해 초기화
    
    def apply_discount(self, arg):
        self._price = Money(self._price.amount - arg, self._price.currency)
```

## 배경

객체(데이터 구조)를 다른 객체(데이터 구조)에 중첩하면 내부 객체를 참조 혹은 값으로 취급할 수 있다.
참조나 값이냐의 차이는 내부 객체의 속성을 갱신하는 방식에서 그 차이가 확연히 드러난다.
참조로 다루는거면 그 객체의 속성만 바꾸는거고
값으로 다루는 경우라면 통째로 교체하는 것이다.

필드를 값으로 다룬다면 내부 객체의 클래스를 수정해서 값 객체(_Value Object_)로 만들 수 있다. VO는 immutable이고, 이런 구조는 더 다루기 쉽다.
복제해서 써도 문제없고, 바뀐 값이 사이드이펙트를 낼 수도 없다. 안바뀌니까

그렇지만 값객체의 이런 특징때문에 이런 리팩터링을 쓰면 안 되는 경우도 있다. 특정 객체를 공유하는 케이스다. 그 때는 참조로 다뤄야한다.

## 절차

1. 후보 클래스가 불변인지, 불변이 될 수 있는지 확인한다
2. 각각의 setter를 하나씩 제거(11.7절)한다
3. 이 값 객체의 필드를 사용하는 동치성(_equality_) 비교 메소드를 만든다 <br />
→ 이걸 할 땐 해시코드 생성 메소드도 같이 오버라이드 해야한다. (파이썬이라면 `__eq__`, `__hash__` 를 의미)

## 예시
