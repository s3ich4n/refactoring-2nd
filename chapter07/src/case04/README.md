# 7.4 임시 변수를 질의 함수로 바꾸기

_Replace Temp with Query_

## 개요

Before

```python
def calculate_price(self):
    base_price = self._quantity * self._item_price
    if base_price > 1000:
        return base_price * 0.95
    else:
        return base_price * 0.98
```

After

```python
@property
def base_price(self):
    return self._quantity * self._item_price


def calculate_price(self):
    if self.base_price > 1000:
        return self.base_price * 0.95
    else:
        return self.base_price * 0.98
```

## 배경

함수 내에서 쓰는 결과값을 뒤에서 다시 참조하기 위해 임시변수를 쓴다. 이 아이디어는 굿. 더 좋은 아이디어는 아예 함수로 만들어서 쓰는 것이다.

긴 함수의 한 부분을 별도 함수로 뺄 때 먼저 변수들을 각각의 함수로 만들면 일이 수월해진다. 추출한 함수에 변수를 따로 전달할 필요가 없어지니까.
이러면 추출한 함수와 원래 함수의 경계도 더 명확해진다. 이상한 의존관계를 떼어내고 사이드 이펙트를 제거할 수 있다.
비슷한 계산을 수행하는 다른 함수에서도 쓸 수 있다. 코드 중복을 줄일 수 있다는 뜻이다.

이 리팩터링은 클래스 안에서 적용하면 효과가 가장 크다.

하지만 장점만 있는 것은 아니다. 변수는 값을 한 번만 계산하고 그 뒤로는 읽기만 하게 하는게 좋다.
예를 들어 변수에 값을 한 번 대입한 후 더 복잡한 코드 덩어리에서 여러 차례 다시 대입하면 모두 질의함수로 뽑아내야 한다.
이렇게 리팩터하면 변수가 다음번에 또 쓰일 때 항상 같은 값을 내야한다.

## 절차

1. 변수가 사용되기 전에 값이 확실히 결정되는지, 변수를 사용할 때마다 계산 로직이 매번 다른 결과를 만들어내는 건 아닌지 확인한다.
2. 읽기전용으로 만들 수 있는 변수는 읽기 전용으로 만든다.
3. 테스트한다
4. 변수 대입문을 함수로 추출한다<br />
   → 변수와 함수가 같은 이름을 가질 수 없다면 함수 이름을 임시로 짓는다. 추출한 함수가 사이드이펙트를 내지 않는지 확인한다. 사이드이펙트가 있다면 질의 함수와 변경 함수 분리하기(
   11.1절)로 대처한다
5. 테스트한다
6. 변수 인라인하기(6.4절)로 임시 변수를 제거한다

## 예시
