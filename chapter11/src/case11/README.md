from chapter11.src.case11.case11 import calculate_ascent

# 11.11 수정된 값 반환하기

## 개요

Before

```python
total_ascent = 0
points = []

def calculate_ascent():
    global total_ascent
    for i in range(1, len(points)):
        vertical_change = points[i].elevation - points[i-1].elevation
        total_ascent += vertical_change if vertical_change > 0 else 0
```

After

```python
points = []

def calculate_ascent(points):
    result = 0
    for i in range(1, len(points)):
        vertical_change = points[i].elevation - points[i-1].elevation
        result += vertical_change if vertical_change > 0 else 0
    
    return result

total_ascent = calculate_ascent(points)
```

## 배경

데이터 수정 추적은 꽤나 힘겨운 과정이다.
같은 데이터 블록을 읽고 수정하는 코드가 여러 곳이면 데이터가 수정되는 흐름과 코드의 흐름을 일치시키기 어렵다.
그래서 데이터가 수정되면 그 사실을 명확히 알려주어서 어느 함수가 무슨일을 하는지 쉽게 알 수 있도록 하는 일이 중요하다.

이를 위한 좋은 방법이 있다. 이는 바로 변수를 갱신하는 함수라면 수정된 값을 반환하여 호출자가 그 값을 변수에 담도록 하는 것이다.
이러면 호출자 코드를 읽을 때 변수가 갱신될 것이라는 걸 분명히 인지하게 된다.
해당 변수의 값을 단 한 번만 정하면 될 때 특히나 유용하다.

이 리팩터링은 값 하나를 계산한다는 분명한 목적이 있는 함수에 유용하고, 값 여러개를 갱신하는 함수에는 비효율적이다.
함수 옮기기의 준비 작업으로도 적합한 방법이다.

## 절차

1. 함수가 수정된 값을 반환하게 하여 호출자가 그 값을 자신의 변수에 저장하게 한다
2. 테스트한다
3. 피호출 함수 안에 반환할 값을 가리키는 새로운 변수를 선언한다 <br />
→ 이것이 의도대로 되었는지 확인하려면 호출자에서 초기값을 수정해본다. 제대로 처리되었다면 수정된 값이 무시된다.
4. 테스트한다
5. 계산이 선언과 동시에 이루어지도록 통합한다(선언 시점에 계산로직을 바로 실행하여 대입)
6. 테스트한다
7. 피호출 함수의 변수 이름을 새 역할에 어울리도록 바꾼다
8. 테스트한다

## 예시
