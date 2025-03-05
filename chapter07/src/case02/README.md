# 7.2 컬렉션 캡슐화하기

_Encapsulate Collection_

## 개요

Before

```python
class Person:
    def __init__(self, courses):
        self._courses = courses

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, a_list):
        self._courses = a_list

```

After

```python
import copy  # for shallow copy


class Person:
    def __init__(self, courses):
        self._courses = courses

    @property
    def courses(self):
        return copy.copy(self._courses)

    def add_course(self, a_course): ...

    def remove_course(self, a_course): ...
```

## 배경

가변 데이터를 캡슐화해서 원치않는 변경을 허락하는걸 막는다. getter가 컬렉션 자체를 반환하면 눈치채지 못하는 사이에 컬렉션 원소가 수정될 수 있다.

파울러는 `add_course`, `remove_course` 같은 컬렉션 수정을 하는 메소드를 통해서 값을 수정하도록 한다.

핵심은, 원본 모듈 밖에서 컬렉션을 수정하지 않는 습관이 필요하다. 이런 건 수단으로 강제하는 것이 좋다.

1. 컬렉션 필드 접근을 메소드로 감싸기
2. 복사본을 주기

아무튼 코드베이스에서는 일관성을 지니게 하는 것이 핵심이다. 한 프로젝트는 반드시 하나의 방식을 공유하자.

## 절차

1. 컬렉션을 캡슐화부터 한다(6.6절)
2. 컬렉션에 원소를 추가/제거 하는 함수를 추가한다 <br />
   → 컬렉션 자체를 통째로 바꾸는 세터는 제거한다(11.7절). 세터를 제거할 수 없다면 인수로 받은 컬렉션을 복제해 저장하게 만든다
3. 정적 검사를 수행한다
4. 컬렉션을 참조하는 부분을 모두 찾는다. 컬렉션의 변경자를 호출하는 코드가 모두 앞에서 추가한 추가/제거 함수를 호출하도록 수정한다. 하나씩 바꿀 때마다 테스트한다.
5. 컬렉션 게터를 수정해서 원본 내용을 수정할 수 없는 읽기전용 프록시나 복제본을 반환하게 한다.
6. 테스트한다.

## 예시

컬렉션 접근 제어를 막는게 캡슐화지, private으로 설정했다고 다가 아니다.
