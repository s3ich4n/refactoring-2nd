# 8.8 반복문을 파이프라인으로 바꾸기

_Replace Loop with Pipeline_

## 개요

Before

```python
names = []
for i in input:
    if i.job == "programmer":
        names.append(i.name)

```

After

```python
# Pythonic way
names = [i.name for i in input if i.job == "programmer"]

# Funtional style
names = list(map(lambda i: i.name, 
                filter(lambda i: i.job == "programmer", input)))
```

## 배경

객체의 컬렉션을 순회할 때 반복문 말고도 다양한 접근을 할 수 있다. 이번 예시는 프로그래밍 언어가 다양한 패러다임을 받아들이면서 제공하는 기능을 소개한다.
컬렉션 파이프라인을 이용하면 로직의 처리 과정을 일련의 연산으로 표현할 수 있다[^1]. 이 때 각 연산을 컬렉션을 받고 다른 컬렉션을 리턴한다.
`map`, `filter`가 그 예시다. `map` 은 함수를 사용해 입력 컬렉션의 원소를 변환하고, `filter`는 또 다른 함수를 사용해 입력 컬렉션을 필터링하여 부분집합을 만든다.
이 부분집합은 다음 파이프라인에도 쓰인다.
이런 식으로 논리를 파이프라인으로 풀면 이해하기 쉬워진다. 파이프라인 대로 로직을 읽으면 되니까.

## 절차

1. 반복문에서 사용하는 컬렉션을 가리키는 변수를 하나 만든다 <br />
→ 기존 변수를 단순히 복사한 것일 수도 있다
2. 반복문의 첫 줄부터 시작하여 각 단위행위를 적절한 컬렉션 파이프라인 연산으로 대체한다. 이 때 컬렉션 파이프라인 연산은 1에서 만든 반복문 컬렉션 변수에서 시작하여, 이전 연산의 결과를 기초로 연쇄수행된다. 하나 대체할 때마다 테스트한다
3. 반복문의 모든 동작을 대체했다면 반복문 자체를 지운다. <br />
→ 반복문이 결과를 누적변수(_accumulator_)에 대입했다면 파이프라인의 결과를 그 누적변수에 대입한다

## 예시

파이썬이면 리스트 컴프리헨션을 쓰는쪽이 더 익숙하다.

다만 이건 자바코드를 보는 게 좋겠다:

```java
public record CityPhone(String city, String phone) {}

public List<CityPhone> acquireData(String input) {
    return Arrays.stream(input.split("\n"))
        .skip(1)
        .filter(line -> !line.trim().isEmpty())  
        .map(line -> line.split(","))
        .filter(fields -> fields[1].trim().equals("India"))
        .map(fields -> new CityPhone(fields[0].trim(), fields[2].trim()))
        .collect(Collectors.toList());
}
```

반복문을 파이프라인으로 대체하는 예시는 마틴 파울러의 블로그 글[^2]도 읽어보자

[^1]: https://martinfowler.com/articles/collection-pipeline/
[^2]: https://martinfowler.com/articles/refactoring-pipelines.html
