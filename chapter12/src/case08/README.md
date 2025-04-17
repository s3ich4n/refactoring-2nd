# 12.8 슈퍼클래스 추출하기

_Extract Superclass_

## 개요

Before

```python
class Department:
    @property
    def total_annual_cost(self):
        ...

    @property
    def name(self):
        ...

    @property
    def head_count(self):
        ...


class Employee:
    @property
    def annual_cost(self):
        ...

    @property
    def name(self):
        ...

    @property
    def employee_id(self):
        ...
```

After

```python
class Party:
    @property
    def name(self):
        ...

    @property
    def annual_cost(self):
        ...


class Department(Party):
    @property
    def annual_cost(self):
        ...

    @property
    def head_count(self):
        ...


class Employee(Party):
    @property
    def annual_cost(self):
        ...

    @property
    def employee_id(self):
        ...
```

## 배경

비슷한 일을 하는 두 클래스가 보이면 상속 메커니즘을 이용해서 비슷한 부분을 공통의 슈퍼클래스로 올릴 수 있다.
공통된 부분이 데이터면 필드 올리기(12.2절)를, 동작이라면 메소드 올리기(12.1절)를 사용한다.

객체지향을 설명할 때, "현실의 것"을 기초하여 객체를 쌓고, 이는 신중해야한다 라는 말이 있다.
하지만 마틴 파울러는 경험 상 초반 설계의 힌트가 될 수는 있지만, 프로그램이 성장하며 그에 맞는 상속이 별도로 도출되며
슈퍼클래스로 끌어올리고 싶은 공통요소를 찾았을 때 바뀌는 것이 잦았다는 조언을 준다.

슈퍼클래스 추출하기의 대안으로는 클래스 추출하기(7.5절)가 있다.
어느것을 선택하느냐는 중복 동작을 상속으로 해결하느냐, 위임으로 해결하느냐에 따라 달려있다.
슈퍼클래스 추출하기 쪽이 더 간단하므로 이쪽부터 시도하는 편이 권장된다.
나중에 필요하면 슈퍼클래스를 위임으로 바꾸기(12.11절)로 하는 것은 어렵지 않다.

## 절차

`<br />`, `` 복사해서 쓰기

1. 빈 슈퍼클래스를 만든다. 원래 클래스가 새 클래스를 상속하도록 한다 <br />
→ 필요하다면 생성자에 함수 선언 바꾸기(6.5절)를 적용한다
2. 테스트한다
3. 생성자 본문 올리기(12.3절), 메소드 올리기(12.1절), 필드 올리기(12.2절)를 차례로 적용하여 공통 원소를 슈퍼클래스로 옮긴다
4. 서브클래스에 남은 메소드들을 검토한다. 공통되는 부분이 있다면 함수로 추출(6.1절)한 후 메소드 올리기(12.1)를 적용한다
5. 원래 클래스들을 사용하는 코드를 검토하여 슈퍼클래스의 인터페이스를 쓰게할 지 고민한다

## 예시
