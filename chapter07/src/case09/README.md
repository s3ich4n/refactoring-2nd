# 7.9 알고리즘 교체하기

_Substitute Algorithm_

## 개요

Before

```python
def found_person(people):
    for person in people:
        if person == "Don":
            return "Don"
        if person == "John":
            return "John"
        if person == "Kent":
            return "Kent"
    return ""
```

After

```python
def found_person_new(people):
    candidates = ["Don", "John", "Kent"]
    return next((p for p in people if p in candidates), "")
```

## 배경

목적을 달성하기 위해 쉬운 방법은 존재하게 마련이다. 알고리즘도 마찬가지다.
파울러는 더 쉬운 방법이 있으면 복잡한 코드를 고친다. 알고리즘을 모두 걷어내고 훨씬 쉬운 코드로 바꿀 때의 방법이다.
문제를 더 확실히 이해하고 더 쉬운 방법을 발견했을 때 이 방법을 쓰는 것이 좋다. 내 코드와 똑같은 라이브러리로 바꿔치기할 때도 적용할 수 있다.

이 작업을 하려면 반드시 메소드가 가능한 한 잘게 나눈 상태인지 확인해야한다. 그래야 간소화가 수비다. 큰걸 한번에 바꾸는건 너무 어렵다.

## 절차

1. 교체할 코드를 함수 하나에 모은다.
2. 이 함수만을 이용해 동작을 검증하는 테스트를 마련한다.
3. 대체할 알고리즘을 준비한다.
4. 정적 검사를 수행한다.
5. 기존 알고리즘과 새 알고리즘의 결과를 비교하는 테스트를 수행한다. 두 결과가 같다면 리팩터링이 끝난다. 그렇지 않다면 기존 알고리즘을 참고하여 새 알고리즘을 테스트하고 디버깅한다.

## 예시

```python
people_list = ["Sam", "Don", "Amy"]

result = found_person(people_list)
result = found_person_new(people_list)
print(result)  # "Don"
```