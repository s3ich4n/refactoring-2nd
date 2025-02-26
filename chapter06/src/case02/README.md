# 6.2 함수 인라인하기

_Inline Function_

## 개요

Before

```python
def get_rating(driver):
    return 2 if more_than_five_late_deliveries(driver) else 1

def more_than_five_late_deliveries(driver):
    return driver.number_of_late_deliveries > 5
```

After

```python
def get_rating(driver):
    return 2 if (driver.number_of_late_deliveries > 5) else 1
```

## 배경

책 전반에서 목적이 뚜렷한 함수를 이용하길 권하지만, 도가 지나치면 거슬린다. 여기선 잘못 추출되면 도로 합치는 방안을 소개한다.

간접 호출을 과하게 쓰는 것이 인라인 대상이다.

## 절차

1. 다형 메소드(_polymorphic method_)인지 확인한다
2. 인라인할 함수를 호출하는 곳을 모두 찾는다
3. 각 호출문을 함수 본문으로 교체한다
4. 하나씩 교체할 때마다 테스트한다 <br />
→ 인라인은 한 번에 할 필요는 없고, 까다로운 부분 대신 여유될 때마다 틈틈이 처리한다
5. 함수 정의(원래 함수)를 삭제한다

쉬운 케이스에서만 처리하기. 복잡한 건 다른 방안으로...

## 예시 - 가장 쉬운 경우
