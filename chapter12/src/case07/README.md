# 12.7 서브클래스 제거하기

_Remove Subclass_

## 개요

Before

```python
class Person:
    @property
    def gender_code(self):
        return "X"

class Male(Person):
    @property
    def gender_code(self):
        return "M"


class Female(Person):
    @property
    def gender_code(self):
        return "F"
```

After

```python
class Person:
    @property
    def gender_code(self):
        return self._gender_code
```

## 배경

서브클래싱은 데이터 구조와 다른 변종을 만들거나 종류에 따라 동작을 다르게 할 수 있는 유용한 메커니즘이다.
다형성을 구현하는 매우 멋진 수단이지만, 시간이 지나면서 가치가 바래진다. 심지어 아무도 안쓰는 코드가 될 수도 있다.
심지어는 서브클래스가 필요없는 방식으로 만들어진 기능에서만 쓰이기도 한다.

이런 서브클래스는 차라리 슈퍼클래스의 필드로 대체하여 제거하는 것이 낫다.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 서브클래스의 생성자를 팩토리 함수로 바꾼다(11.8) <br />
→ 생성자를 사용하는 측에서 데이터 필드를 이용해 어떤 서브클래스를 생성할지 결정한다면 그 결정 로직을 슈퍼클래스의 팩토리 메소드에 추가한다.
2. 서브클래스의 타입을 검사하는 코드가 있다면 그 검사 코드에 함수 추출하기(6.1절)와 함수 옮기기(8.1절)를 차례로 적용하여 슈퍼클래스로 옮긴다. 하나 변경할 때마다 테스트한다
3. 서브클래스의 타입을 나타내는 필드를 슈퍼클래스에 만든다
4. 서브클래스를 참조하는 메소드가 3에서 만든 타입 필드를 이용하도록 수정한다
5. 서브클래스를 지운다
6. 테스트한다

## 예시
