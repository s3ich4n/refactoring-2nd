# 12.2 필드 올리기

_Pull Up Field_

## 개요

> [!NOTE]
> 
> 파이썬에선 12.3절과 함께 묶여서 처리될 수 있다. 아래 예시도 사실 12.3절 내용이 포함되어있다.

Before

```python
class Employee:
    ...


class Salesperson(Employee):
    def __init__(self, name):
        self._name = name


class Engineer(Employee):
    def __init__(self, name):
        self._name = name
```

After

```python
class Employee:
    def __init__(self, name):
        self._name = name


class Salesperson(Employee):
    def __init__(self, name):
        super().__init__(name)


class Engineer(Employee):
    def __init__(self, name):
        super().__init__(name)
```

> [!TIP]
> 반대 리팩터링: 필드 내리기 (12.5절)

## 배경

서브클래스가 독립적으로 개발되었거나 하나의 계층구조로 뒤늦게 리팩터링된 경우라면 일부 기능이 중복되어있을 경우가 있다.
필드 중복이 대표적이다. 이런 필드는 이름이 비슷한데, 꼭 그렇지도 않다. 이런 경우는 뭔 일이 일어지나 분석해야한다.
분석 결과 필드들이 비슷한 방식으로 쓰인다고 판단되면 슈퍼클래스로 올려야한다.

이러면 두 중복을 줄일 수 있다:
1. 데이터 중복 선언
2. 해당 필드가 사용하는 동작

동적 언어 중에는 필드를 클래스 정의에 포함시키지 않는 경우가 많다.
그 대신 필드에 가장 처음 값이 대입될 때 등장한다.
이런 경우라면 필드를 올리기 전에 반드시 생성자 본문부터 올려야(12.3절) 한다.

## 절차

1. 후보 필드들을 사용하는 곳 모두가 그 필드들을 똑같은 방식으로 쓰는지 살펴본다
2. 필드들의 이름이 다르면 똑같은 이름으로 바꾼다(필드 이름 바꾸기 - 9.2절)
3. 슈퍼클래스에 새로운 필드를 생성한다 <br />
→ 서브클래스에서 이 필드에 접근할 수 있어야 한다 (cf. 이 때 쓰는 접근제한자가 `protected` 다)
4. 서브클래스의 필드를 제거한다
5. 테스트한다


## 예시

12.3절 생성자 본문 올리기와 예시를 함께 처리할 예정