# 8.2 필드 옮기기

_Move Field_

## 개요

Before

```python
class Customer:
    @property
    def plan(self):
        return self._plan

    @property
    def discount_rate(self):
        return self._discount_rate
```

After

```python
class Customer:
    @property
    def plan(self):
        return self._plan

    @property
    def discount_rate(self):
        return self.plan._discount_rate
```

## 배경

프로그램은 동작을 구현하는 코드로 대부분 이루어져있지만, 프로그램의 진짜 힘은 데이터 구조에서 나온다.
주어진 문제에 적합한 데이터구조를 활용하면 동작코드는 자연스럽게 단순하고 직관적으로 짜여진다.
잘못된 데이터 구조를 선택하면 아구가 맞지 않는 데이터를 다루는 코드로 엉망이 된다.
이해하기 어려운 코드가 만들어지는 데서 끝나지 않고, 데이터 구조 자체도 프로그램의 목적을 숨긴다.

그런 이유로 데이터구조가 중요하다. 하지만 _제대로_ 하기는 어렵다.
프로그램이 필요한 적합한 데이터 구조는 결험과 도메인 주도 설계 같은 기술로 이를 개선할 수 있다.
하지만 그 천하의 마틴 파울러도 모든 기술 및 경험에도 불구하고, 초기 설계에는 실수가 빈번했다.
프로젝트가 진행되면서 문제 도메인과 데이터 구조에 대해 많은 이해가 쌓이면 기존 설계가 오판이었음을 알게 된다.

현재 데이터 구조가 맞지 않음을 인지했다면 바로 수정해야한다.
고치지 않고 두면 머릿속이 혼란해지고, 나중에 짤 코드의 복잡도로 이어진다.

예를들며 얘기해보자. 함수에 레코드[^1]를 넘길 때마다 또 다른 레코드의 필드도 함께 넘기고 있다면 데이터 위치를 옮겨야 할 것이다.
함수에 항상 함께 건네지는 데이터 조각은 상호관계가 명확하게 드러나도록 한 레코드에 담는 게 좋다.
변경도 주요한 요인이다. 한 레코드를 바꾸려 할 때 다른 레코드 필드까지 바꿔야하면 필드의 위치가 잘못됐다는 신호다.
구조체 여러 개체 정의된 똑같은 필드들을 갱신해야 한다면 한 번만 갱신해도 되는 위치로 옮기란 신호다.

필드 옮기기 리팩터링은 대체로 더 큰 리팩터링의 일부로 수행된다.
필드 하나를 잘 옮기면 그 필드를 쓰던 많은 코드가 다른데서 쓰이는게 더 나아질 수 있다. 그러면 리팩터링을 마저 진행해서 호출코드도 다 바꾼다.
비슷한 이치로, 옮기려는 데이터가 쓰이는 패턴때문에 당장은 필드를 옮길 수 없을 때가 있다.
그러면 사용패턴부터 먼저 풀어주고 필드를 옮긴다.

레코드 대신 클래스나 객체도 마찬가지로 똑같은 원리로 관리되어야 한다.
클래스는 메소드와 데이터의 캡슐화가 이루어진 덩어리다보니 리팩터링을 하기는 쉽지만,
캡슐화되지 않은 데이터는 못하진 않더라도 더 까다로울 것이다.

## 절차

1. 소스 필드가 캡슐화되어있지 않다면 캡슐화한다
2. 테스트한다
3. 타깃 객체에 필드(와 접근자 메소드)를 생성한다
4. 정적 검사를 수행한다
5. 소스 객체에서 타긱 객체를 참조할 수 있는지 확인한다 <br />
→ 기존 필드나 메소드 중 타깃 객체를 넘겨주는게 있을 수도 있다. 없다면 이 기능의 메소드를 쉽게 만들 수 있는지 살펴본다. 쉽지않다면 타깃 객체를 저장할 새 필드를 소스 객체에 생성한다. 이러면 영구적인 변경이 되겠지만, 더 넓은 맥락에서 리팩터링을 충분히 하면 다시 없앨 수 있다
6. 접근자들이 타깃 필드를 사용하도록 수정한다 <br />
→ 여러 소스에서 같은 타깃을 공유한다면, 먼저 세터를 수정해서 타깃필드/소스필드 모두를 수정하게 만들고, 일관성을 깨트리는 갱신을 검출하기 위해 어서션을 추가(10.6절)한다. 잘 처리되었다면 접근자들이 타깃 필드를 쓰도록 수정한다
7. 테스트한다
8. 소스 필드를 제거한다
9. 테스트한다

## 예시

현재 예시로는 `discount_rate` 필드를 `CustomerContract` 에게 옮기는 걸 하려한다

### 첫 번째 케이스

첫 과정부터 헤멨는데, initializer에서 데이터 초기화를 캡슐화 한 아이디어가 낯설었다. (c14c3982edea6e72d061d20d71d423c44c584cf4)

할인율이라는 데이터가 계약(Contract)과 더 밀접하게 관련되어 있다고 판단될 때, 데이터와 그 데이터를 사용하는 메서드들을 같은 클래스로 모아서 응집도를 높일 수 있다.

이것이 핵심이다.

### 두 번째 케이스

Account가 AccountType의 이자율을 가져오면 문제가 있을 수 있다.

리팩터링 전에는 각 계좌가 자신만의 이자율을 갖고있고, 지금은 종류가 같은 모든 계좌가 이자율을 "공유"하길 원한다.
수정 전에도 이자율이 계좌별로 다 같았다면 모를까, 이자율이 다른 계좌가 하나라도 있다면 그건 ***리팩터링이 아니다***.
이유는 쉽다. 겉보기 동작이 달라지니까.

이 문제는 "Move Field" 리팩터링의 핵심 원칙을 말해준다.

필드를 이동하기 전에 해당 이동이 동작을 바꾸지 않는지 확인해야 하며,
만약 이동이 동작을 바꾼다면, 그것은 리팩터링이 아니라 기능 변경이 되는 것이다.

[^1]: 자바의 `record` 생각해도 되고, `@dataclass` 생각해도 되고, 하다못해 dictionary 같은 raw한거 생각해도 되고.