# 6.11 단계 쪼개기

_Split Phase_

## 개요

Before

```python
import re

order_data = re.split(r'\s+', order_string)
product_price = price_list[order_data[0].split("-")[1]]
order_price = int(order_data[1]) * product_price
```

After

```python
@dataclass
class Order:
    product_id: str
    quantity: int

order_record = parse_order(order)
order_price = price(order_record, price_list)

def parse_order(a_string) -> Order:
    import re
    
    values = re.split(r'\s+', order_string)
    return Order(
        product_id=values[0].split("-")[1],
        quantity=values[1],
    )

def price(order: Order, price_list):
    return order.quantity * price_list[order.product_id]
```

## 배경

서로 다른 두 대상을 한꺼번에 다루는 코드를 발견하면 각각을 별개 모듈로 나누는 방법을 모색한다.
코드를 수정할 때 두 대상을 동시에 생각할 필요 없이 하나에 집중하기 위해서다.
모듈을 분리해서 다른 모듈을 봐야하는 걸 막자. 생각을 집중하게 만들자.

아무튼 이걸 하는 가장 쉬운법은 동작을 두 단계로 나누는 것이다. 위의 예시는 아래와 같이 나눌 수 있다:
1. 문자열을 파싱해서 `order` 형태로 리턴시키기
2. `order`의 가격을 연산하기

컴파일러도 이런 구성이다. 컴파일러는 보통:
- 텍스트(코드)를 받아서
- 실행 가능한 형태로 변환한다

오랜 연구 끝에 아래와 같은 형태로 개발하는 것이 좋다는 것으로 나왔다:
- 텍스트 토큰화
- 토큰 파싱 후 구문 트리 생성
- 구문 트리 변환
- 오브젝트 코드 생성 (이후 빌드하겠죠)

그래서 각자의 코드를 각자가 집중할 수 있다.

단계를 쪼개는 기법은 주로 덩치 큰 소프트웨어에 적용된다. 예를들어 컴파일러의 매 단계는 다수의 함수와 클래스로 구성된다.
근데 규모와 관계없이 이렇게 별도 모듈로 분리해서 그 차이를 분명하게 드러내면 유지보수하기 더 좋아지지 않을까 한다.

## 절차

`<br />`, `→` 복사해서 쓰기

1. 두 번째 단계에 해당하는 코드를 독립함수로 추출한다
2. 테스트한다
3. 중간 데이터 구조를 만들어서, 앞에서 추출한 함수의 인수로 추가한다
4. 테스트한다
5. 추출한 두 번째 단계 함수의 매개변수를 하나씩 검토한다. 그중 첫 번째 단계에서 사용되는 것은 중간데이터 구조로 옮긴다. 하나씩 옮길 때마다 테스트한다. <br />
→ 가끔 두 번째 단계에서 사용하면 안 되는 매개변수가 있다. 이런 건 각 매개변수를 사용한 결과를 중간 데이터 구조의 필드로 추출하고, 이 필드의 값을 설정하는 문장을 호출한 곳으로 옮긴다(8.4절).
6. 첫 번째 단계 코드를 함수로 추출(6.1절)하면서 중간 데이터 구조를 반환하도록 만든다. <br />
→ 첫 번째 단계를 변환기(_transformer_) 객체로 추출해도 좋다.

## 예시 (1) - 상품의 결제금액을 계산

두 번째 단계를 떼고 테스트 후 (60d9980f0c7048e307fbc6db88c2fcf57d618ab7)

중간 데이터 구조도 만들고 (4c75355f6356ca123afc58e5332bc2445b1d2af2)

두 번째 함수의 매개변수를 검토해서 하나씩 바꿨다 (592de3ec305bb7b873bd66e544a9602e9843b41b, 600670b83f0d03bc5c16986005b4de926d961a95, 2665e7f3d700298f39f9209b9dd00ed933ecc497)

첫 번째 코드를 함수로 추출했다 (f3ccfab924b8a1e52005ab12cf3101e5cb2dc19f)

## 예시 (2) - 자바 코드

테스트 하기 쉽게 구성해놓고 그걸 돌린다.

나머지는 똑같다. 다만 명령줄 호출, 표준 출력을 각자 분리해서 테스트를 쉽게 찍게 했다. 이 것이 험블 객체 패턴(_Humble Object Pattern_)이라 부른다.
