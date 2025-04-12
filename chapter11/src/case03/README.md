# 플래그 인수 제거하기

_Remove Flag Argument_

## 개요

Before

```python
def set_dimension(self, name, value):
    if name == "height":
        self._height = value
        return

    if name == "width":
        self._width = value
        return
```

After

```python
def set_height(self, value):
    self._height = value

def set_weight(self, value):
    self._height = value
```

## 배경

플래그 인수(_flag argument_) 는 호출되는 함수가 실행할 로직을 호출하는 쪽에서 선택하기 위해 전달하는 인수.

예를 들어 이런 코드가 있다 하자:

```python
def book_concert(a_customer, is_premium):
    if is_premium:
        ... # premium 로직
    else:
        ... # 일반로직
```

근데 이건 쓸 때 이렇게 쓰게 된다.

```python
book_concert(a_customer, true)
book_concert(a_customer, CustomerType.PREMIUM)
book_concert(a_customer, "Premium")
```

마틴 파울러는 이런 코드의 단점은 이렇게 표현한다:

1. 호출할 수 있는 함수는 무엇인가? 그리고 어떻게 호출해야 하나?
2. 이 API가 정확히 뭔 뜻인지 파악하기가 어렵다 
3. 플래그 자체가 boolean 이라면 뜻이 정확히 뭔지 알 방도가 없다

차라리 명확한 단 하나의 기능을 제공하는 편이 더 깔끔하다.

```python
premium_book_concert(a_customer)
```

해당 절에서 일컫는 플래그 인수는 데이터로서 함수에 전달되는게 아니라 로직분기에 쓰이는 값이다.
이걸 떼어내면 코드도 깔끔해지고 코드 분석도구가 더 일을 잘 하게 로직을 풀어내는 데도 일조한다.

함수 하나에서 플래그 인수를 둘 이상 쓰면 플래그 인수를 쓸 수도 있다.
그렇지만, 그 함수가 너무 많은 일을 처리하는 건 아닌지 살펴보고 같은 로직을 조합해내는 더 간단한 함수를 만들 방법을 고민하는 것이 더 좋다.

## 절차

1. 매개변수로 주어질 수 있는 값 각각에 대응하는 명시적 함수들을 생성한다 <br />
→ 주가되는 함수에 깔끔한 분배조건문이 있으면, 조건문 분해하기(10.1절)로 명시적 함수를 작성하자. 그렇지 않다면 래핑 함수(_wrapping function_) 형태로 만든다.
2. 원래 함수를 호출하는 코드를 모두 찾아서 각 리터럴 값에 대응되는 명시적 함수를 호출하도록 수정한다.

## 예시

예시 1은 조건문 분해부터. 많은 일을 하던 `delivery_date`의 일을 쪼갠다.

그담엔 개별 메소드로 테스트를 분리하고,