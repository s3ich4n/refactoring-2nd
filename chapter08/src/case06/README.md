# 8.6 문장 슬라이드하기

_Slide Statements_

## 개요

Before

```python
pricing_plan = retrieve_pricing_plan()
order = retreive_order()
charge = None
charge_per_unit = pricing_plan.unit
```

After

```python
pricing_plan = retrieve_pricing_plan()
charge_per_unit = pricing_plan.unit
order = retreive_order()
charge = None
```

## 배경

관련있는 코드는 가까이 모아둬야 이해하기 쉽다.
예를들어 하나의 데이터 구조를 이용하는 문장은 -- 다른 데이터를 쓰는 코드에 섞여있기보다 -- 한데 모여있어야 좋다.
변수를 선언하고 쓰는 코드도 마찬가지다. 변수를 쓰려할 때 선언하는 스타일 같은 것 말이다.

관련 코드끼리 모으는 작업은 다른 리팩터링(주로 함수 호출하기, 6.1절)의 준비단계로 자주 쓰인다.
관련있는 코드를 명확히 구분되는 함수로 빼는게, 그냥 문장을 모으는 것 보다 낫다.
그렇지만 코드가 모여있지 않다면 함수 호출은 애초에 할 수도 없다.

## 절차

1. 코드 조각(문장들)을 이동할 목표 위치를 찾는다. 코드 조각의 원래 위치와 목표 위치 사이의 코드들을 훑어보며, 조각을 모으고 나면 동작이 달라지는 코드가 있나 살펴본다. 아래와 같은 간섭이 있다면 이 리팩터링은 포기한다. <br />
→ 코드 조각에서 참조하는 요소를 선언하는 문장 앞으로는 이동할 수 없다 <br />
→ 코드 조각을 참조하는 요소의 뒤로는 이동할 수 없다 <br />
→ 코드 조각에서 참조하는 요소를 수정하는 문장을 건너뛰어 이동할 수 없다 <br />
→ 코드 조각이 수정하는 요소를 참조하는 요소를 건너뛰어 이동할 수 없다
2. 코드 조각을 원래 위치에서 잘라내어 목표 위치에 붙여넣는다
3. 테스트한다

테스트가 실패한다면 더 적게 나눠서 시도해보자. 이동 거리를 줄이는 방법, 한 번에 옮기는 조각의 크기를 줄이는 방법으로 재시도해보자.

## 예시

### 예시 (1)

코드 조각을 슬라이드 할 때는 두 가지를 확인해야 한다.

- 무엇을 슬라이드할 것인가?
- 슬라이드 할 수 있나?

마틴 파울러는 선언코드를 슬라이드하여 처음 사용하는 곳 까지 붙이려는 일을 자주 한다.
그 외에도 다른 리팩터링을 위해 문장 슬라이드를 자주 한다. 예를들어 함수 추출을 위해 비슷한 코드를 한데 묶고, 그걸 함수로 묶는 식(6.1절) 말이다.

슬라이드 할 거를 캐치했으면 진짜 해도 상관없는지를 봐야한다. 코드의 순서가 바뀌면 겉보기 동작이 달라지는지를 중심으로 판단하자.

아래 코드를 기준으로 살펴보자.

```python
# 선언부
pricing_plan = retrieve_pricing_plan()
order = retreive_order()
base_charge = pricing_plan.base
charge = None
charge_per_unit = pricing_plan.unit
units = order.units # order 근방으로 옮겨도 문제 없음
discount = None     # discount 를 쓰기 직전에 옮겨도 됨

charge = base_charge + units * charge_per_unit
discountable_units = max(units - pricing_plan.discount_threshold, 0)
discount = discountable_units * pricing_plan.discount_factor
if order.is_repeat: discount += 20
charge = charge - discount
charge_order(charge)
```

선언부 코드는 그냥 바꾸면 된다. discount 선언문을 필요한 곳 근처로 옮기는 식으로.
`retrieve_order` 를 저렇게 옮겨도 되는 이유는, CQS[^1] 를 지켜서 작성했다고 가정하기 때문이다.
이걸 적용할 때는 사이드 이펙터가 있나없나 잘 보고 처리해야한다.

슬라이드가 안전한가/그렇지 않은가는 관련된 연산이 무엇이고 어떻게 구성되는지 확실히 알고있어야 한다.

이를 위한 보조도구로는 테스트 커버리지가 있을 수도 있다. 테스트가 믿음직하지 못하면 이 리팩터링은 더 신중해야한다.
아니면 (더 흔한 접근으로는) 영향받는 코드의 테스트를 보강한다.

만약 이 과정이 실패하면, 더 작게 슬라이드하보는 것이다.
더 짧은 줄을 건너뛰거나, 위험해보이는 줄까지 슬라이드해보고 고장나며 두 케이스를 생각할 수 있다.
수행할 가치가 없거나, 다른 무언가를 먼저 해야하거나.

### 예시 (2) - 조건문이 있는 경우

조건문의 안팎으로 슬라이드 해야할 때도 있다. 조건문 밖으로 슬라이드할 때는 중복로직이 빠질거고, 조건문 안으로 슬라이드할 때는 중복로직이 추가될 것이다.

예를들어 이런 코드를 보자:

```python
result = None
if len(available_resources) == 0:
    result = create_resource()
    allocated_resources.append(result)
else:
    result = available_resources.pop()
    allocated_resources.append(result)
    
# 여기 넣거나, 각 분기에 쓰거나
# allocated_resources.append(result)
return result
```


여기선 append 하는 로직이 중복되니까, 블록 밖으로 빼면 중복제거가 된다. 반대로 슬라이드하면 모든 분기에 복제되어 들어간다.

## 더 읽을 거리

문장 교환하기(_Swap Statement_)[^2] 라는 리팩터링 기법도 있다. 이건 문장 하나짜리 조각만 취급한다.
단일 문장일 수도 있는 걸 더 보기 좋게 쪼갠다고 생각하면 된다.
충분히 매력적이고, 그냥 보기만 봤을 땐 뭐 저런거까지 하나? 싶어도 효과가 있다.

이 리팩터링을 통해 큰걸 고치는게 어려우면, 이 방법을 시도해보는 것도 방법이라는 걸 시사한다.

[^1]: Command-Query Separation, https://martinfowler.com/bliki/CommandQuerySeparation.html
[^2]: https://www.industriallogic.com/blog/swap-statement-refactoring/
