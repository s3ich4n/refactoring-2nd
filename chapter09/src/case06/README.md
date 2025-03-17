# 9.6 매직 리터럴 바꾸기

_Replace Magic Literal_

## 개요

Before

```python
def potential_energy(mass, height):
    return mass * 9.81 * height
```

After

```python
STANDARD_GRAVITY = 9.81

def potential_energy(mass, height):
    return mass * STANDARD_GRAVITY * height
```

## 배경

위와같이 이런 일반적 리터럴을 매직 리터럴(_magic literal_)이라 한다. 코드를 읽는 사람을 위해 보다 명확히 리팩터링 해야한다.

마틴 파울러는 차라리 그걸 함수호출하는 방안으로 바꾸거나, 이름을 아예 잘 두거나 하는 쪽으로 가이드한다.

`ONE = 1` 같은 접근은 너무 뻔하다.

## 절차

1. 상수를 선언하고 매직 리터럴을 대입한다
2. 해당 리터럴이 쓰인 모든 곳을 찾는다
3. 찾은 곳 각각에서 리터럴이 새 상수와 동일한 의미로 쓰였는지 확인하며, 같은 의미라면 상수로 대체 후 테스트한다.

> ![NOTE]
> 
> 이 리팩터링이 되었나 확인하는 방법:
> 
> 상수값을 바꿔보고 관련 테스트 전체가 바뀐값에 해당하는 결과를 내는지 확인하기
