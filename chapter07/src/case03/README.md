# 7.3 기본형을 객체로 바꾸기

_Replace Primitive with Object_

## 개요

Before

```python
# 기본형으로 쓰던 걸...
orders = list(filter(lambda o: o.priority == "high" or o.priority == "rush", orders))
```

After

```python
# ...객체화
class Priority:
    _values = ("low", "normal", "high", "rush")

    def __init__(self, value):
        if value not in self._values:
            raise ValueError(f"Invalid priority value: {value}")
        self._value = value

    def higher_than(self, other):
        return self._values.index(self._value) > self._values.index(other._value)

    @property
    def value(self):
        return self._value


orders = list(filter(lambda o: o.priority.higher_than(Priority("normal")), orders))
```

## 배경

단순 정보가 복잡해지고 고도화된 정보 자신만이 수행하는 "동작"이 필요할 때가 올 수 있다. 이를 위해 그 데이터를 표현하는 전용 클래스를 정의한다.

파울러는 그 시점을 '출력 이상의 기능을 제공'할 때로 보고 그 때부터 클래스화를 제안한다.

## 절차

1. 아직 변수를 캡슐화 하지 않았다면 캡슐화(6.6절) 한다.
2. 단순한 값 클래스(_value class_)를 만든다. 생성자는 기존 값을 인수로 받아 저장하고, 이 값을 반환하게 한다
3. 정적 검사를 수행한다
4. 값 클래스의 인스턴스를 새로 만들고 필드에 저장하도록 세터[^1]를 수정한다. 이미 있다면 필드의 타입을 바꾼다
5. 새로 만든 클래스의 게터를 호출한 결과를 반환하도록 게터[^2]를 수정한다
6. 테스트한다
7. 함수 이름을 바꾸면(6.5절) 원본 접근자의 동작을 더 잘 드러낼 수 있는지 검토한다 <br />
   → 참조를 값으로 바꾸거나(9.4절), 값을 참조로 바꾸면(9.5절) 새로 만든 객체의 역할(값, 참조 객체)이 더 잘 드러나는지 검토한다.

## 예시

[^1]: 단계 1에서 변수를 캡슐화하며 만든 세터
[^2]: 단계 1에서 변수를 캡슐화하며 만든 게터
