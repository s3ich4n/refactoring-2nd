# 7.1 레코드 캡슐화하기

_Encapsulate Record_

## 개요

Before

```python
organization = {
    "name": "Acme Gooseberries",
    "country": "GB",
}
```

After

```python
class Organization:
    def __init__(
        self,
        name: str,
        country: str,
    ):
        self._name = name
        self._country = country

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str) -> None:
        self._country = value 
```

파이썬이면 엄밀히는 접근제한자가 없으니, 데이터의 성격에 따라 이를 책임있게 사용한다.

```python
class Organization:
    def __init__(
        self,
        name: str,
        country: str,
    ):
        self.name = name
        self.country = country

>>> org = Organization(name="test", country="KR")
>>> org.name
test
```

## 배경

데이터를 넣을 때 이런 유의미한 값을 넣을 수 있다. 매우 직관적으로 넣을 수 있지만, 단순하면 세세함을 챙기기 어렵다. 
특히나 계산해서 얻을 수 있는 값과 그렇지 않은 값을 명확히 가르기가 너무 어렵다. 

마틴 파울러는 이 때문에 가변 데이터(_mutable_)를 레코드보다 객체를 더 선호한다.

객체를 쓰면 계산으로 얻을 수 있는 값, 그렇지 않은 값을 각각의 메소드로 줄 수도 있고, 계산되었는지 신경 쓸 필요도 없다.
캡슐화를 하면 이름 변경에도 유리하다.

가변 데이터일 때는 객체면 좋고, 불변(_immutable_) 데이터면 값을 모두 구해서 저장하고, 이름을 바꿀 때는 필드를 복제한다.

이런 레코드 구조는 두 가지로 갈린다:
1. 필드 이름을 노출하는 경우
2. (필드를 외부로부터 숨겨서) 내가 원하는 이름을 쓰는 경우
    - hash, map, hashmap, dictionary(!), associative array 등의 이름

이런 nested list, hashmap은 json, xml로 직렬화 가능하다. 이런 구조도 캡슐화할 수 있다.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 레코드를 담은 변수를 캡슐화(6.6절)한다
2. 레코드를 감싼 단순한 클래스로 해당 변수의 내용을 교체한다. 이 클래스에 원본 레코드를 반환하는 접근자도 정의하고, 변수를 캡슐화하는 함수들이 이 접근자를 사용하도록 수정한다.
3. 테스트한다
4. 원본 레코드 대신 새로 정의한 클래스 타입의 객체를 반환하는 함수들을 새로 만든다
5. 레코드를 반환하는 예전 함수를 사용하는 코드를 4에서 만든 새 함수로 갈아끼운다. 필드에 접근할 때는 객체의 접근자를 사용한다. 적절한 접근자가 없으면 추가한다. 한 부분을 바꿀 때마다 테스트한다. <br />
→ 중첩된 구조처럼 복잡한 레코드면 데이터 갱신하는 클라이언트에 주의해서 살펴본다. 클라이언트가 데이터를 읽기만 한다면 데이터의 복제본이나 읽기 전용 프록시를 반환할 건지 고려 필요
6. 클래스에서 원본 데이터를 반환하는 접근자와 (1에서 검색하기 쉬운 이름을 붙여둔) 원본 레코드를 반환하는 함수를 제거한다
7. 테스트한다
8. 레코드의 필드에도 데이터 구조인 중첩 구조라면 레코드 캡슐화하기와 컬렉션 캡슈로하하기(7.2절)를 재귀적으로 적용한다.

## 예시 (1) - 간단한 레코드 캡슐화하기

상수 캡슐화는 여기서한다 (fb38e282e65613245fb88f6c172887d570fc4003)

이렇게 하면 변수 자체는 물론, 조작방식도 바뀐다 (d9f0aed76d8ef866453f1d06a349d326423300c7)
- 레코드를 클래스로 바꾸기
- 새 클래스의 인스턴스를 반환하는 함수를 새로 만든다

`data`를 풀어서 쓸 수도 있다 (b0e1643fa61f538872b175ae7ed2ceb6421fb91f)

## 예시 (2) - 중첩된 레코드 캡슐화하기
