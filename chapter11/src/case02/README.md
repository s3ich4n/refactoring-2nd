# 11.2 함수 매개변수화하기

_Parametrize Function_

## 개요

Before

```python
def ten_percent_raise(a_person):
    a_person.salary = a_person.salary.multiply(1.1)

def five_percent_raise(a_person):
    a_person.salary = a_person.salary.multiply(1.05)
```

After

```python
def raise_salary(a_person, factor):
    a_person.salary = a_person.salary.multiply(factor)
```

## 배경

두 함수의 로직이 비슷한데 리터럴만 조금 다르면 그 값을 매개변수로 받아서 처리하는 것으로 중복제거가 가능하다.

이러면 매개변수만 바꾸는 것으로 여러곳에서 쓸 수 있으니 함수의 유용성이 커진다.

## 절차

1. 비슷한 함수 중 하나를 선택한다
2. 함수 선언 바꾸기(6.5절)로 리터럴들을 매개변수로 추가한다
3. 이 함수를 호출하는 곳 모두에 적절한 리터럴 값을 추가한다
4. 테스트한다
5. 매개변수로 받은 값을 사용하도록 함수 본문을 수정한다. 하나 수정할 때마다 테스트한다
6. 비슷한 다른 함수를 호출하는 코드를 찾아 매개변수화된 함수를 호출하도록 하나씩 수정한다. 하나 수정할 때마다 테스트한다. <br />
→ 매개변수화된 함수가 대체할 함수와 다르게 동작한다면, 그 비슷한 함수의 동작도 처리할 수 있도록 본문 코드를 적절히 수정한다.

## 예시

쉬운 예시는 위의 개요만 봐도 아니까, 조금 복잡한걸로 테스트합시다.
