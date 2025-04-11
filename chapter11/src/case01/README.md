# 11.1 질의 함수와 변경 함수 분리하기

## 개요

Before

```python
def get_total_outstanding_and_send_bill():
    result = sum(invoice.amount for invoice in customer.invoices)
    send_bill()
    return result
```

After

```python
def total_outstanding():
    return sum(invoice.amount for invoice in customer.invoices)

def send_bill():
    email_gateway.send(format_bill(customer))
```

## 배경

함수는 겉보기 부수 효과(_observable side effect_)가 없도록 추구해야할 필요가 있다. 그러면 호출해도 요상한 부수효과가 안생긴다.
호출하는 문장의 위치를 어디로든 옮겨도 되고 테스트도 쉽다.
즉 신경 쓸 거리가 매우 적어진다는 것이다.

일단 겉보기 부수 효과가 있는함수와 없는 함수는 구분해두는 것이 좋다.
그러려면 질의 함수(읽기 함수)는 부수효과가 없도록 하는 규칙[^1]을 따르면 좋다.
가능하면 따르는 편이 깔끔한 코드를 만드는 지름길이다. 때로 내가 도리어 무의미한 원칙이라면 일단 어기는 게 맞다.

마틴 파울러는 값을 반환하며 부수효과가 있는 함수는 "거의 모두" 상태를 변경하는 부분과 질의하는 부분을 일단 떼보려고 한다.

'겉보기' 부수 효과라는 말을 쓴 데는 아래 이유를 가진다.

- 요청된 값을 캐시하고 다음 호출에 빠르게 응답하는 방법
- 캐싱도 객체의 상태를 변경하지만 객체 밖에서는 관찰할 수 없음

=> 어떤 순서로 호출하든 모든 호출에 항상 똑같은 값을 반환함을 의미

## 절차

1. 대상 함수를 복제하고 질의 목적에 충실한 이름을 짓는다. <br />
→ 함수 내부를 살펴 무엇을 리턴하나 살펴본다. 어떤 변수의 값을 반환한다면 그 변수 이름으로 힌트를 얻자
2. 새 질의 함수에서 부수효과를 모두 제거한다
3. 정적 검사를 실시한다
4. 원래 함수 (변경함수)를 호출하는 곳을 모두 찾는다. 호출하는 곳에서 리턴값을 사용하면 질의 함수를 호출하게 바꾸고 원래 함수를 호출하는 코드를 바로 아래줄에 새로 추가한다. 하나 수정할 때마다 테스트한다.
5. 원래 함수에서 질의 관련 코드를 제거한다
6. 테스트한다

이걸 다 하면 새로 만든 질의 함수와 원래 함수에 (정리해야 할) 중복이 남아있을 수 있다.

## 예시


[^1]: https://martinfowler.com/bliki/CommandQuerySeparation.html