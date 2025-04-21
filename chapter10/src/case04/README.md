# 10.4 조건부 로직을 다형성으로 바꾸기

_Replace Conditional with Polymorphism_

## 개요

Before

> [!NOTES]
> `switch` clause가 없어서 이렇게 대체합니다


```python
def get_plumage(bird):
    if bird.type == 'EuropeanSwallow':
        return "average"
    elif bird.type == 'AfricanSwallow':
        return "tired" if bird.number_of_coconuts > 2 else "average"
    elif bird.type == 'NorwegianBlueParrot':
        return "scorched" if bird.voltage > 100 else "beautiful"
    else:
        return "unknown"
```

After

```python
class EuropeanSwallow:
    @property
    def plumage(self):
        return "average"


class AfricanSwallow:
    def __init__(self, number_of_coconuts=0):
        self.number_of_coconuts = number_of_coconuts
    
    @property
    def plumage(self):
        return "tired" if self.number_of_coconuts > 2 else "average"


class NorwegianBlueParrot:
    def __init__(self, voltage=0):
        self.voltage = voltage
    
    @property
    def plumage(self):
        return "scorched" if self.voltage > 100 else "beautiful"
```

## 배경

복잡한 조건부 로직은 풀어내기 가장 난해하다.
이러한 로직은 직관적으로 구조화할 방법도 있으나, 더 높은 수준의 개념으로 조건을 분리할 수도 있다.
이는 바로 클래스와 다형성을 이용하여 풀어내는 것이다.

타입을 여러 개를 만들고 각 타입이 조건부 로직을 자신만의 방식으로 처리하도록 구성하는 방법도 있다.
이러면 타입 별로 어떻게 동작할지는 알아서 런타임에 결정된다.

case문과 변형동작으로 구성된 로직또한 마찬가지. 로직을 슈퍼클래스에 넣고,
변형동작에 해당하는 각각의 케이스를 상속받는 쪽에서 구현한다.

만능은 아니기 때문에, 조건부 로직이 **복잡해진다면** 그 때 고려하는 게 좋다.

## 절차

1. 다형적 동작을 표현하는 클래스가 없으면 만든다. (가능하면 적합한 인스턴스를 알아서 만들어 리턴하는 팩토리 함수도 함께)
2. 호출하는 코드에서 팩토리 함수를 쓰게한다
3. 조건부 로직 함수를 슈퍼클래스로 옮긴다 <br />
→ 조건부 로직이 온전한 함수로 분리되어 있지 않다면 먼저 함수로 추출(6.1절) 한다
4. 서브클래스 중 하나를 선택한다. 서브클래스에서 슈퍼클래스의 조건부 로직 메소드를 오버라이드한다. 조건부 문장 중 선택된 서브클래스에 해당하는 조건절을 서브클래스 메소드로 복사한 다음 적절히 수정한다.
5. 같은 방식으로 각 조건절을 해당 서브클래스에서 메소드로 구현한다
6. 슈퍼클래스 메소드에는 기본 동작부분만 남긴다. 혹은 슈퍼클래스가 추상클래스여야 한다면 `NotImplementedError` 같은걸 `raise` 시킨다.

## 예시
