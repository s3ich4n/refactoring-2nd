# 7.6 클래스 인라인하기

_Inline Class_

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

제 역할을 못 해서 그대로 두면 안 되는 클래스를 도로 인라인한다. 특정 클래스에 남은 역할이 거의 없으면 돌려놓자.

혹은 두 클래스의 기능을 지금과 다르게 배분할 때도 인라인한다. 한번 합친 다음엔 새 클래슬 추출(7.5절)하는게 쉬울 수도 있다(??)
파울러는 코드 재구성할 때 이런 접근방식을 취하는 것을 권한다. 한 컨텍스트를 다른데 합쳐버리거나, 하나로 합친 후 적절히 다시 분리하는 등.

## 절차

1. 소스 클래스의 각 public 메소드에 대응하는 메소드들을 타깃 클래스에 생성한다. 이 메소드들은 단순히 작업을 소스 클래스로 위임해야 한다.
2. 소스 클래스의 메소드를 사용하는 코드를 모두 타깃 클래스의 위임 메소드를 쓰도록 바꾼다. 하나씩 바꿀 때마다 테스트한다.
3. 소스 클래스의 메소드와 필드를 모두 타깃 클래스로 옮긴다. 하나씩 옮길 때 마다 테스트한다.
4. 소스 클래스를 지운다. RIP

## 예시
