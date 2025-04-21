# 12.3 생성자 본문 올리기

_Pull Up Constructor Body_

## 개요

Before

```python
class Party:
    ...


class Employee(Party):
    def __init__(self, name, user_id, monthly_cost):
        self._name = name
        self._user_id = user_id
        self._monthly_cost = monthly_cost
```

After

```python
class Party:
    def __init__(self, name):
        self._name = name


class Employee(Party):
    def __init__(self, name, user_id, monthly_cost):
        super().__init__(name)
        self._user_id = user_id
        self._monthly_cost = monthly_cost
        
```

## 배경

생성자는 다루기 까다롭다. 그럴거면 최소한의 하는 일만을 하게 하자.

마틴 파울러는 서브클래스들에서 기능이 같은 메소드를 발견하면 함수 추출하기(6.1절)와 메소드 올리기(12.1절)을 차례로 적용하여 말끔하게 슈퍼클래스로 옮긴다.
근데 그 메소드가 생성자라면 신중하다. 생성자가 할 수 있는 일, 호출순서는 제약이 있기 때문이다.

> [!TIP]
> 이 리팩터링이 가볍게 끝나지 않을 것 같으면 생성자를 팩토리 함수로 바꾸기(11.8절)을 고려하는 것이 좋다.

## 절차

1. 슈퍼클래스에 생성자가 없다면 하나 정의한다. 서브클래스의 생성자들에서 슈퍼클래스의 생성자를 호출하는가 확인한다
2. 문장 슬라이드하기(8.6절)로 공통문장 모두를 `super()` 호출 직후로 옮긴다
3. 공통코드를 슈퍼클래스에 추가하고 서브클래스들에선 제거한다. 생성자 매개변수 중 공통코드에서 참조하는 값들을 모두 `super()` 로 건네준다
4. 테스트한다
5. 생성자 시작 부분으로 옮길 수 없는 공통 코드에는 함수 추출하기(6.1절)와 메소드 올리기(12.1절)를 차례로 적용한다

## 예시

두 번째 예시는 모든 서브클래스가 하는 일을 서브클래스에서 먼저 공통코드를 함수로 추출하고

그걸 슈퍼클래스로 옮기면 죄다 똑같이 일하니까

그런 식으로 코드를 다듬는다.