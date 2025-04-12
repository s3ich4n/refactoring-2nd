# 11.7 세터 제거하기

_Remove Setting Method_

## 개요

Before

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
```

After

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

## 배경

세터 메소드가 있다는건 필드가 수정될 수 있다는 것을 의미한다.
객체 생성 후 수정되지 않길 원하는 필드면 세터를 안 만들었을 것이다.

세터 제거하기가 필요할 때는 두 가지다.
1. 접근자 필드를 통해서만 필드를 다루려할 때 - 명확히 하기 위함
2. 클라이언트에서 생성 스크립트(_creation script_)로 객체를 생성할 때

## 절차

1. 설정해야 하는 값을 생성자에서 받지 않는다면 그 값을 받을 매개변수를 생성자에 추가한다(함수 선언 바꾸기 - 6.5절). 그런 다음 생성자 안에서 적절한 세터를 호출한다. <br />
→ 세터 여러 개를 제거하려면 해당 값 모두를 한꺼번에 생성자에 추가한다. 그러면 이후과정이 간소해진다.
2. 생성자 밖에서 세터를 호출하는 곳은 제거하고, 새 생성자를 사용하도록 한다. 하나 수정할 때마다 테스트한다. <br />
→ (갱신하려는 대상이 공유 참조 객체라서) 새로운 객체를 생성하는 방식으로는 세터 호출을 대체할 수 없다면 이 리팩터링을 취소한다.
3. 세터 메소드를 인라인(6.2절)한다. 가능하다면 해당 필드를 불변으로 만든다.
4. 테스트한다.

## 예시

