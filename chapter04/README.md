# 4장 - 테스트 구축하기

가치있는 리팩터링을 위해서는 불가피한 실수 대비용 완충재가 필요하다. 그것이 테스트 스위트(_test suite_)이다. 책에서 소개하는 리팩터링 대다수는 테스트 스위트로 검증하길 제안한다. 왜
좋은지 저자의 설명을 요약해보자.

## 4.1 자가 테스트코드의 가치

프로그래머는 코드 짜는 것보다 디버깅하는데 시간을 많이 쓴다. 버그는 몇줄 그냥 고치고 끝인데, 그 여정이 매우 길다. 그리고 버그 잡다가 또 버그가 생긴다. 마틴 파울러도 일하면서 테스트코드를
담기로 했는데, 이 때 자동화가 뒷받침되게끔 각잡고 하자고 마음먹은 후 이렇게 결심했다:

> [!TIP]
> 모든 테스트는 완전 자동화. 결과도 스스로 검사되게끔.

이걸 하니까 회귀 버그 잡는것에 시간을 거의 덜 쏟았다.

> [!NOTE]
> 테스트 스위트는 버그검출 도구다. 버그를 찾는 시간을 대폭 줄여준다.

켄트 백과 에릭 감마[^1]가 비행기 타고 날아가면서 뚝딱 만든 프로그램이 있다. 그게 저 유명한 JUnit이다. `xUnit` 식구들 의 영향을 받은 `unittest`가 파이썬의 기본 테스트
검출기고, 내가 쓰는 `pytest` 는 파이썬스러운(_pythonic_) 성향을 더 띈다.

테스트 작성법을 알아야 하고, 테스트를 자동화할 수 있어야 하고, 테스트를 처음부터 짜고 쌓아올라가는 편이 좋다[^2]. 내가 만드는 기능의 계약을 테스트로 구성하고(이 때 테스트 run하면
당연히 Fail이다. 코드베이스가 없거나 바뀐 조건에서 패스하는거니까), 코드베이스를 고치고 테스트를 Pass로 바꾼다. 그리고 리팩터링을 여기서 적용.

## 4.2 테스트할 샘플 코드

이런 사진이 있는데 비즈니스로직만 먼저 짜고 테스트해보자.

![예시 사진](./media/001.png)

예시코드는 `src` 디렉터리에, 테스트코드는 `tests` 디렉터리에 추가한다.

## 4.3 첫 번째 테스트

자바스크립트에선 Mocha를, 나는 pytest를 써서 테스트한다. 픽스처를 구성하고...

```python
@pytest.fixture(name="test_data")
def sample_province_data():
    return {
        "name": "Asia",
        "producers": [
            {"name": "Byzantium", "cost": 10, "production": 9},
            {"name": "Attalia", "cost": 12, "production": 10},
            {"name": "Sinope", "cost": 10, "production": 6},
        ],
        "demand": 30,
        "price": 20,
    }
```

```python
def test_sample_province_data(test_data):
    assert Province(test_data)
```

테스트하면 끝.

```python
def test_province_shortfall(test_data):
    asia = Province(test_data)
    assert asia.shortfall == 5
```

값이 뻔하더라도, 일부러 고장내본다. shortfall 연산을 엉망으로 만들면 하나는 깨진다.

![일부러 고장내기. 진짜 잘 테스트하나 확인하는게 쉬우니까](./media/002.png)

여기서 마틴 파울러의 팁 하나.

> [!TIP]
> 자주 테스트하시오.
> 작성중인 코드는 최소 몇 분 간격으로 테스트하시오.
> 적어도 한 번은 전체 테스트를 돌려보시오.

이번에 uvicorn 공부하면서 전체 테스트 케이스가 600개 언저리였고 다 돌리는데 1분 10초 정도 걸렸다(M3 Pro 기준). 아무튼 자주 돌리기.

패스하면 초록막대, 페일나면 빨간막대인 건 너무 유명하다. 마틴 파울러는 여기에 더해서 테스트가 하나라도 빨간막대면 리팩터 하면 안된다고 조언한다. 차라리 이전상태(다 패스하던)로 돌아가서 재작업하길 주문한다.

## 4.4 테스트 추가하기

테스트는 위험요인을 기준으로 테스트 해야한다. 읽고쓰는 저렴한 테스트보다 가장 걱정되는 부분을 집중해서 테스트하는게 더 가치있다.

두 번째 팁.

> [!TIP]
> 완벽하게 만드느라 테스트를 못 돌릴거면, 불완전한 테스트라도 작성해 실행하는 게 낫다.

```python
def test_province_profit(test_data):
    asia = Province(test_data)
    assert asia.profit == 230
```

이 테스트는 실제 계산결과 `230`을 넣고 테스트한거다.

그런데 책에서 말하는 바는 픽스처가 각 테스트별로 별개로 쓰이길 바랐다. "테스트끼리 상호작용하게 하는 공유 픽스처"를 만들지 말라는 것.

그럼 scope를 `function` 으로 돌리면 매번 생기니, `beforeEach` 와 유사하게 행동한다.

## 4.5 픽스처 수정하기

테스트 시 픽스처를 쓰고 세터로 픽스처 내의 내용을 바꾸는 경우, 이건 테스트가 필요하다.

그러니까 아래와 같은 경우를 의미한다:

```python
def test_change_production(test_data):
    asia = Province(test_data)
    asia.producers[0].production = 20

    assert asia.shortfall == -6
    assert asia.profit == 292
```

표준 픽스처를 취해서, 테스트를 돌리고 검증한다. (Arrange-Act-Assert 라 하든 Given-When-Then이라 하든, Setup-Exercise-Verify라 하든...)
핵심은 초기 작업 중 공통 부분을 픽스처화 해서 "초기화"를 잘 하고 테스트를 격리시키라는 말.

## 4.6 경계 조건 검사하기

현재까진 해피케이스만 봤다. 안좋은 케이스도 있어야한다. 마틴 파울러는 현 예시 같은 경우에 주로 '컬렉션이 빈 경우'를 테스트하는 편이라고 한다.

```python
def test_province_with_no_producers():
    data = {
        "name": "Asia",
        "producers": [],
        "demand": 30,
        "price": 20
    }

    no_producers = Province(data)

    assert no_producers.shortfall == 30
    assert no_producers.profit == 0
```

숫자형 값은 `0`일때도 테스트해보면:

```python
def test_province_with_zero_demand(asia):
    asia = Province(asia)
    asia.demand = 0

    assert asia.shortfall == -25
    assert asia.profit == 0
```

음수도 넣어보면? 수요가 마이너스인 경우. 근데 이럴 수 있나?  잠깐, 이런 '이럴 수 있나?' 를 생각하는 게 중요하다. 프로그램의 특이사항, 경계를 생각할 필요가 있다. 그걸 테스트 해야한다.

```python
def test_province_with_negative_demand(asia):
    asia = Province(asia)
    asia.demand = -1

    assert asia.shortfall == -26
    assert asia.profit == -10
```

> [!TIP]
> 문제가 생길 여지가 있는 경계 조건을 생각하자.
> 그 부분을 집중적으로 테스트하자.

만일 수요값이 비어있다면?

```python
def test_province_with_empty_demand(asia):
    asia = Province(asia)

    with pytest.raises(ValueError):
        asia.demand = ""

    # asia.demand에 문자열을 넣는 행위가 Exception이 터지므로
    # 허용하지 않는다. (i.e., NaN 케이스가 없음)
```

이런 식으로, 내 프로그램의 특이케이스와 망가지기 쉬운 부분을 중점해서 테스트하면 보다 견고하게 구성할 수 있다. 이럴 땐 아주 못된 사람 마인드로 테스트 해야한다(!)

만약 `producers` 값이 이상하다면?

```python
def test_province_with_invalid_producers():
    data = {
        "name": "Asia",
        "producers": "",    # 아예 안맞는 값을 넣으면?
        "demand": 30,
        "price": 20
    }

    # 반복문을 정상으로 판단함(str도 Sequence니까 iterable함)
    # 그리고 빈 문자열은 반복문을 패스해서 객체 생성이 완료됨.
    # 기본값이 들어가져서 작동됨.
    prov = Province(data)

    assert prov.shortfall == 30
```

음.... 책에서처럼 터지게 하려면?

```python
def test_province_with_invalid_producers():
    data = {
        "name": "Asia",
        "producers": " ",    # 이러면....
        "demand": 30,
        "price": 20
    }

    # ...반복문을 정상으로 판단함(str도 Sequence니까 iterable함)
    # 그리고 빈 문자열을 `Producer` 객체에 넣으려다보니 터짐
    with pytest.raises(AttributeError):
        assert Province(data)

```

의도한 대로 터졌다. 그러면 프로그램은 어떻게 대응해야할까? 생각의 흐름을 써보자:

- 의미있는 오류메시지를 뱉게할까?
    - 신뢰할 수 없는 곳에서(외부에서 JSON을 로드하고 던진다거나) 데이터가 오면
    - 그땐 테스트 해야할지도?
- 일단 지금 그대로 둬도 되면?
    - 신뢰할 만한 다른 곳에서 입력 객체를 만들어주는 경우(같은 코드베이스 안 처럼)
    - 그럼 굳이 안해도 될 지도..? 중복검증은 크게 의미없으니까

같은 생각을 계속 해야한다.

하지만 마틴 파울러는 리팩터 전이라면 이런 테스트를 리팩터 전에는 안쓴다고 제안한다. 리팩터링은 겉보기 동작에 영향을 주면 안된다. 이런 건 겉보기 동작과는 관계없다.

이렇게 데이터가 잘못 흘러서 디버깅 하기 어려울 것 같으면 어서션 추가하기(10.6절)을 해줘도 좋다.

> [!TIP]
> 어차피 모든 버그를 못 잡을 것이다 라고 생각해서 테스트를 안짜면
> 대다수의 버그를 잡을 기회를 날리는 셈이다

그러면 테스트를 어디까지 해야할까? 사실 적당히가 중요한 법이다. 수확 체감 법칙(_law of diminishing returns_) 이 적용된다는 뜻이다. 
테스트 자체에 힘을 주면 의욕이 떨어질 수도 있다. 즉, 진짜 필요한 테스트, 가치있는 테스트를 잘 챙겨서 쓰자. 그게 결국 나를 도와줄 것이다.

후에 배울 기법들을 더 배우고 리팩터 하면서 잠재적인 버그를 체크할 때가 오길 바란다.

## 4.7 끝나지 않은 여정

자동화해서 테스팅도 잘 해야되고, 테스트 용이성도 설계의 중요한 부분이 되어야한다고 본다. 테스트는 반복가능하고 자주 실행가능하고 명확해야한다.

그리고 테스트는 버그를 잘 잡아야한다. 또 하나의 조언이 있다:

> [!TIP]
> 버그 리포트를 받으면 그 케이스를 커버하는 단위 테스트를 짜자

충분한 테스트코드는 주관적이다. 여러 객관화된 수치로 판단할 수는 있으나 정확하지는 않다. 테스트 코드는 요구사항을 커버하는 거고, 세상 일은 요구사항 대로 돌아가지 않다보니 항상 럭비공마냥 멋대로 튀게 마련이다.

객관화된 수치 중 하나는 테스트 커버리지다. 이는 환자의 온도같은 것이라, 환자의 건강을 체크하는 지표로 활용될 수 있으나 온도 정상화가 목적이 되어서는 안된다.

테스트 코드 작성 때문에 개발속도가 안 나온다 생각되면 테스트를 너무 많이 짜고있진 않은지 살펴보자.

### 추가로...

참고로 여기서 말하는 테스트는 단위 테스트(_unit test_)이다. 통합 테스트나 다양한 내용은 일단 다루지 않는다.

> [!NOTE]
> 단위 테스트 또한 별도로 공부중입니다. ([관련 링크](https://github.com/s3ich4n/unit-testing-101))
> 이 내용이 여러분들께 도움이 되시길 바랍니다.

[^1]: GoF 의 그 사나이.
[^2]: 그게 안 된다면 레거시 코드 활용 전략에서 제시하는 테스트 추가용 기법을 배우면 좋겠다. <br /> https://m.yes24.com/Goods/Detail/64586851