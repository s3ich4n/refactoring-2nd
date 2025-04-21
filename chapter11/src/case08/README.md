# 11.8 생성자를 팩토리 함수로 바꾸기

_Replace Constructor with Factory Function_

## 개요

Before

```python
lead_engineer = Employee(lead_engineer, 'E')
```

After

```python
lead_engineer = Employee.create(lead_engineer)
```

## 배경

생성자를 바로 노출하는 대신 팩토리 함수를 쓰자.
생성자에는 일반 함수에는 없는 제약이 있을 수도 있다.
예를들어 자바면 그 생성자를 정의한 클래스의 인스턴스를 리턴해야한다. 서브클래스의 인스턴스나 프록시를 리턴할 수 없다.
생성자의 이름도 고정이라, 적절한 이름을 쓸 수도 없다.

팩토리 함수는 그런 제약이 없으므로 대체가 쉽다.

파이썬이라면 그런 용도로 딱 맞게 쓸 수 있는 데코레이터인 `@classmethod` 가 있다.

이를테면:

```python
class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def create(cls, name, age):
        return cls(
            name=name,
            age=age,
        )
```

## 절차

1. 팩토리 함수를 만든다. 그 본문에는 원래의 생성자를 호출한다
2. 생성자를 호출하던 코드를 팩토리 함수 호출로 바꾼다
3. 하나씩 수정할 때마다 테스트한다
4. 생성자의 가시 범위가 최소가 되도록 제한한다

## 예시
