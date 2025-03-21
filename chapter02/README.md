# 2장 - 리팩터링 원칙

## 2.1 리팩터링 정의

리팩터링은:

> 리팩터링: [명사] 소프트웨어의 겉보기 동작(_observable behaviour_)은 그대로 유지한 채, 코드를 이해하고 수정하기 쉽도록 내부 구조를 변경하는 기법

예를 들면 함수 추출하기[^1], 조건부 로직을 다형성으로 바꾸기 [^2] 등이 되겠다.

> 리팩터하다: [동사] 소프트웨어의 겉보기 동작은 그대로 유지한 채, 여러가지 리팩터링 기법을 적용해서 소프트웨어를 재구성

리팩터링을 하는 건 단위와 상관없다. 작게 바꾸든 크게 바뀌든, 정상작동이 보장되는 것이다. 그래서 저자는 '리팩터링 하다 코드가 깨졌어요' 라고 하면 그건 십중팔구 리팩터링이 아니라고 말하는 것이다.

마틴 파울러는 코드 베이스를 정리하거나 구조를 바꾸는 모든 걸 재구성(_restructuring_)이란 용어로 표현하고, 이 중 하나를 리팩터링이라고 일컫는다. 그리고 1장에서의 작업처럼 작업을 수차례 나누면, 작업하다 '어 안되네? 다시 돌리자...' 를 안해도 된다. 디버깅에 시간을 덜 쓴단 소리다.

그리고 겉보기 동작이란 애매한 표현은 코드가 똑같이 "돈다"일 뿐, 완전히 똑같단건 아니다.

예를 들어:
- 함수 추출하기를 하면 콜스택이 달라진다 -> 성능 변화(요즘도요?)
- 함수 선언 바꾸기[^3], 함수 옮기기[^4] 같은 건 모듈의 인터페이스가 바뀔 수도 있다. -> 아무튼 사용자 관점에선 달라지는 게 없어야 된다.

리팩터링은 성능개선보다는 코드를 이해하고 쉽게 만드는 것이 포인트다. 이땐 성능이 좋아질 수도, 그렇지 않을 수도 있다. 반면 성능 최적화는 속도 개선에 신경쓰는 것이다. 이때는 목표 성능 도달을 위해 코드가 지저분해 지는건 감안해야 한다.

## 2.2 두 개의 모자

켄트 백은 소프트웨어 개발을 '기능 추가', '리팩터링'이라는 관점으로 두고 두 개의 모자(_two hats_)로 비유했다.

- 기능 추가할 때는 기능 추가만. 그 기능의 진척도는 테스트코드 패스만으로 측정한다.
- 리팩터링할 때는 기능 추가는 일절 하지 않고 코드 재구성만. (놓친 테스트 케이스가 있지 않은 한)테스트 케이스도 추가하지 않는다.

핵심은, 잘 도는지 끝까지 확인한 후 리팩터링을 한다는 거다. 그리고 여기서도 테스트는 분명히 있다. 테스트가 그만큼 중요하구나.

## 리팩터링하는 이유

리팩터링은 만병통치약은 아니다. 하지만 코드가 건강해지는 약은 맞다.

### 리팩터링하면 소프트웨어 설계가 좋아진다

리팩터링을 안 하면 소프트웨어 아키텍처가 썩기 쉽다. 아키텍처에 대한 이해 없이 코드를 짜면 구조가 무너지기 쉬워지고 이러면 코드 만으로 구조파악이 어려워진다. 코드가 썩는 건 한 순간인데, 가속화되면 점점 힘들어진다. 규칙적인 리팩터링으로 이를 돌려놓을 수 있다.

코드가 길어지는 것도 있고 같은일을 하는 코드가 생길 수도 있다. 이런 중복코드를 잡으면 코드 수정이 쉬워진다. 같은 일을 하는 코드가 널려있다면 시스템이 예상대로 안돌 수 있다. 반대로 중복코드를 없애면 모든 코드의 작동이 고유함을 보장할 수 있다.

### 리팩터링 하면 소프트웨어를 이해하기 쉬워진다

코드는 컴퓨터에게 이런 일을 하라고 시키는 것에 불과하지만 내 코드는 나만 볼 게 아니다. 다른 사람일 수도 있고 심지어 미래의 나일 수도 있다. 코드의 구조 또한 명확히 표현해보자.

### 리팩터링하면 버그를 쉽게 찾을 수 있다

코드 구조가 잡히고 하는 일을 쉽게 발견할 수 있으면 버그를 쉽게 잡을 수 있다. 견고한 코드는 결국 이런 습관에서 나온다.

### 리팩터링하면 프로그래밍 속도를 높일 수 있다

단위 테스트 책[^5]에 아마 소프트웨어 엔트로피를 역전할 수 있는 방법으로 테스팅을 강조한 것 처럼, 테스트코드에 기반하여 코드의 구조를 다듬는 리팩터링이라면 코드 품질에 기여하는 것 또한 너무나 자명하다고 본다.

그런데 처음엔 익숙하지 않고 안하던 것이다 보니 힘들 수 있고 느릴 수 있다. 지속적인 반복학습과 실전 풀이로 이를 가다듬는 수 밖에는 없다.

초기엔 개발이 빨라지더라도 새 기능을 코드베이스에 녹이기 어려워지기도 하고, 패치를 하며 운영도 하면 코드가 어떻게 도는지 감이 안온다. 그러다보면 자연스레 처음부터 하는게 낫겠다 싶어진다.

![이런 그래프를 의미한다](https://martinfowler.com/bliki/images/design-stamina-hypothesis/graph.png)

이렇게 되지 않으려면 내부 설계를 잘 대비해서 코드의 수정이 필요한 부분을 잘 짚어내야한다. 모듈화를 해두어서 코드베이스의 일부만 확실히 바꿀 수 있도록 해야한다. 내부 품질이 뛰어난 코드베이스는 새 기능 구축을 돕는 토대가 된다.

마틴 파울러는 이를 설계 지구력 가설[^6] 이라고 부른다. 내부 설계에 심혈을 기울이면 소프트웨어의 지구력이 높아져서 빠르게 개발할 수 있는 상태가 길어진다는 것을 의미한다. 왜 가설(_hypothesis_)인가 하면 증명이 안되서다. 근데 수많은 뛰어난 프로그래머들도 다 하는 좋은 습관인데 안할 이유가 없지않을까?

20년 전 (2판 출시가 2018년이다)만 해도 완벽한 설계 끝에 코드를 짠다고 여겼다. ~~요즘도 그런데가 허다하다만~~ 코드를 짜는 시점부터 코드는 썩으니까. 하지만 리팩터링을 하면 기존 설계를 바로잡을 수 있고, 요구사항이 바뀌어도 설계를 지속해서 수정할 수 있다.

## 2.4 언제 리팩터링 해야할까?

3의 법칙 (by Don Roberts)

1. 그냥한다
2. 똑같은 일을 두 번 하게되면 일단 계속 한다.
3. 똑같은 일을 세 번 하면 리팩터링한다.

### 준비를 위한 리팩터링 - 기능을 쉽게 추가하게 만들기

코드베이스에 기능을 새로 추가하기 전 리팩터하기 좋다. 현재 코드구조를 보고, 조금만 구조를 바꾸면 다른 작업하기 쉬운 지점을 찾는다. 함수 매개변수화하기[^7]를 적용해서 함수에 필요한 매개변수를 지정하고 호출한다.

버그를 잡을 때도, 오류를 일으키는 코드가 세 곳 이상 복제되어 퍼져있으면 한 곳으로 몰아잡아야 한다. 준비를 위한 리팩터링(_Preparatory Refactoring_)[^8]으로 상황을 개선해두면 버그 수정한 효과가 오래가는 동시에 버그 발생 가능성도 줄일 수 있다.

### 이해를 위한 리팩터링 - 코드를 이해하기 쉽게 만들기

코드를 바꾸려면 코드가 하는 일을 파악해야한다. 코드를 파악할 때 코드의 의도가 명확하게 보여지는지, 조건부 로직의 구조가 요상한지, 함수 이름은 별로인지를 봐야한다.

그렇다 한들 코드를 리팩터하고 테스트 해두면 내 생각을 계속 코드로 검증할 수 있다. 다른 사람이 직접 돌려보며 파악도 할 수 있다. 이 것을 이해를 위한 리팩터링(_Comprehension Refactoring_)이라 부른다.

이렇게 헝클어진 코드를 한결 보기쉽게 다듬으면 설계도 눈에 들어오게 된다. 코드 분석을 위한 리팩터링은 복잡한 코드 내 숨어있는 부분을 발견할 수 있는 기화를 준다.

### 쓰레기 줍기 리팩터링

코드를 보면 쓸데없이 복잡하거나, 매개변수화한 함수 대신 똑같은 함수 여러개로 처리하는 둥 요상한게 있다. 눈 돌아가서 치우고 싶을 수도 있지만 간단한 건 빨리 치우고 넘어가는 편이 좋다. 이런 건 쓰레기 줍기 리팩터링(_Litter-Pickup Refactoring_)이라 부른다.

보이스카우트 규칙은 다른 게 아니라 이런 걸 말하는 것이었구나. 하면서 슥 치우고 가는 습관. 테스트로 방어되기까지 하며 코드 구조를 다듬는 행위.

### 계획된 리팩터링과 수시로 하는 리팩터링

위에 살펴본 리팩터링은 기회가 될 때 진행한다. 마틴은 개발 시 프로그래밍 과정에 자연스럽게 만들다가 리팩터하다가 한다. 뭔가 리팩터링은 거창하다기보다 하다 할 수 있다.

좋은 코드는 더 좋게 리팩터 하는 편이 좋다. 그렇지만 지금 좋은 게 내일 좋다고 보장할 수는 없다. 상황에 맞게 코드를 "수정"할 수 있는 여지를 남겨야한단 뜻이다. 그런 의미에서 켄트 백은 이렇게 말했다:

> 무언가 바꾸려할 땐 바꾸기 쉽게 다듬고 쉽게 바꾸자. 만만치 않을 순 있다.

소프트웨어는 새 기능 추가가 쉽게 코드를 "바꾸는" 것이 진짜 고수들의 시야다. 소프트웨어 개발은 끝이 없으므로 새 기능을 반영하기 위해 계속해서 변해야한다.

계획해서 리팩터 하는 것도 필요는 하다. 리팩터 하지 않다가 다시 리팩터하기 시작한다면 새 기능 추가가 쉽게 코드베이스를 개선할 필요가 있단 뜻이다.

### 오래 걸리는 리팩터링

마틴 기준 오래걸리는 리팩터링은 몇 시간 정도다. 팀 전체가 들러붙어 수 주씩 걸리는 리팩터링은 얼마든 존재할 수 있다. 라이브러리 교체나 대규모 업데이트나, 공통 코드 컴포넌트로 빼기, 의존성 제거하기 등.

마틴은 이런 입장은 회의적으로 본다. 차라리 몇 주에 걸쳐 조금씩 "리팩터링" 하는 것을 제안한다. 마틴이 제안한 리팩터링은 "어차피 코드 안깨지니까". 그런데 라이브러리를 고치거나 하는 작업은 어떻게 한 번에 할거냐? 그럴 땐 기존 것, 새 것 모두를 포용하는 추상 인터페이스부터 마련하고, 기존 코드가 이걸 바라보게 바꾸면 교체가 쉬워진다[^9].

### 코드 리뷰에 리팩터링 활용하기

코드 리뷰는 개발팀에 지식을 전파하기 좋다. 큰 소프트웨어라면 시스템의 다영한 부분을 많은 사람이 이해할 수 있기도 하다. 이를 통해 모든 팀원과 코드의 컨센서스를 맞출 수도 있다.

리팩터링은 코드리뷰에도 도움된다. 새 아이디어를 어떻게 밀어넣고, 추가하고 수정하는지를 상상이 아닌 코드로 보기 때문이다. 하면서 돌아갈 수도 나아갈 수도 있기 때문에 아이디어에 더 집중할 수도 있다. 이게 잘 자리잡으면 짝 프로그래밍(_pair programming_)이 되는 것이다.

### 관리자에게는 뭐라고 말해야 할까?

리팩터링을 하겠다고 하며 재구성(_restructuring_)을 하느라고 시간을 몇 주씩 잡으면 설득이 안 된다.

하지말라 하면 진짜 안하게? 그럼 안 되지. 돈 받고 일하는 프로는 어쨌거나 결과를 내야한다. 이 책을 보고 방법을 익힌 후 주어진 일정내로 완료하면서 코드를 구현하는 방법을 익혀야 한다. 그 방법을 리팩터링이라고 하고.

### 리팩터링 하지 말아야 할 때

이 때를 판단하기가 가장 어렵다. 이 때가 언제일지를 사람들과 묻고싶다.

내가 "수정할 필요가 없다면" 구태여 리팩터를 안할 수도 있다. 처음부터 하는 게 더 나을 때도 있다. 그러나 새로 짜는게 나을 지, 리팩터 하는게 나을 지는 어려운 문제다.

## 2.5. 리팩터링 시 고려해야 할 문제

리팩터링은 만능이 아니다. 적용하기 위해 2주의 시간조차도 아깝다고 하는 사람이 있다. 그렇다보니 손익판단을 잘 해야한다. 하다하다 마틴도 리팩터링하면 뒤따라오는 문제가 있다고 말한다.

### 새 기능 개발속도 저하

테스트에 안 익숙하고 리팩터링 기법에 익숙하지 않으면 당연히 적용하는 데 시간이 오래 걸린다. 마틴 쯤 되어서 익숙하니까 어거지로 리팩터를 밀어붙여도 할 수 있는 것으로 보인다.

그리고 과도하게 리팩터링 하는 것보다 아예 안 하는 경우가 더 많다. 이럴 때일 수록 코드베이스가 더 망가지기 쉽다.

가장 무서운 것은 마틴 또한 책에서 경계한 점이다. 리팩터링은 신성한 행위이며  바람직한 절대 선으로 보는 _교조적 태도_ 다. 저딴 이유로 좋은게 아니라 개발 기간을 줄이고 기능 추가시간을 줄이고 버그 수정시간을 줄일 수 있다. 이 것을 잘 하는 것이 프로로써 일하는 게 아닐까 싶다.

### 코드 소유권

리팩터링 하다보면 내가 쓰는 코드의 오너가 아니다보니 함부로 리팩터를 못하는 경우도 생긴다. 함수 선언 바꾸기 를 쓰면 특히 그렇게 될 수 있다. 마틴은 코드의 오너쉽을 느슨하게 하고 리뷰 후 머지해서 변화사항을 함께 체크하는 방향을 제안한다. 큰 시스템을 개발할 때 어울린다고 한다.

### 브랜치

가능하면 리팩터링의 흐름을 빠르게 가져가서, 충돌을 줄이는 걸 권장한다. 지속적으로 결과를 통합하자는(이게 CI네요!?) 의미다. 그렇다보니 마틴은 CI를 (다르게는 trunk-based development 를) 선호한다. 근데 CI(_Continuous Integration_)를 하려면 마스터를 건강하게 유지하고, 기능을 잘게 쪼개고, 기능을 토글할 수 있는 플래그를 통해 빠르게 추가되는 기능이 시스템 전체를 망치지 않도록 한다.

CI와 리팩터링을 합친 개념이 켄트백이 말한 XP(_extreme programming_)다.

### 테스팅

리팩터는 프로그램의 겉보기 동작이 똑같이 유지된다는 것이다. 근데 이걸 하려면 새 동작으로 넘어가기 위한 완충재가 필요하다. 그게 테스트 코드다. CI에는 그래서 테스트가 포함되어야 하고, 이렇게 정상동작을 확인해야 비로소 CD(_Continuous Delivery_)를 하는 것에 의미가 생긴다.

### 레거시 코드

싫은 거 안다. 그렇지만 이걸 개선하는 방법은 테스트를 하면서 꾸준히 리팩터 하는 수 밖에... 레거시 코드 활용 전략[^10] 같은 책에서도 말하는 "프로그램에서 그나마 테스트가 들어갈 부분을 비집고 넣어서 테스트 해야한다" 라는 것이다. 그 틈새를 리팩터링이 만든다.

### 데이터베이스

마틴이 쓴 데이터베이스 리팩터링 이란 책도 있다[^11].

예를 들어 필드 바꾸기 정도는 함수 선언 바꾸기에 따라 호출부와 정의부를 한번에 바꿔야한다.

하지만 테스트는 마이그레이션도 해야하고 프로덕션에 넣기 전 여러 단계로 릴리즈도 해야한다. 동시에 공존시킨 후 완료되면 기존 걸 삭제하는 방식을 말한다.

## 2.6 Refactoring, Architecture and YAGNI

리팩터링을 한다는 것은 오늘과 내일의 간극을 빠르게 잡겠다는 것을 의미한다. 

마틴이 말하는 내용 중, 요구사항을 매우 유연하게 잡으려 하다가 알고봤더니 모두 할 수 없는 목표였다거나 하는 걸 의미한다. 이걸 위해 소프트웨어를 유연하게 만들려고 했다보니 함수가 복잡해진다.

그말인 즉, 지금 가장 적합하고 간단하고 효율적인 설계까지 하고 필요할 때 리팩터를 하겠다는 뜻이다. 처음엔 빠르게 구현하되 변화의 가능성을 열어두고 점진적으로 진화시키겠다는 뜻이다.

you ain't gonna need it, do you?

## 2.7 리팩터링과 소프트웨어 개발 프로세스

XP니 뭐니 하며 테스트코드와 리팩터링를 묶어서 TDD(_Test-driven Development_)라고 한다. 

- 개발 프로세스를 저자가 말한대로 개선하기 위한 첫 토대는 테스트 코드다. 에러를 걸러내는 테스트를 자동으로 수행할 수 있어야 한다.
- 그러고 나서야 기법을 실현할 줄도 알아야 될 뿐더러 리팩터가 프로세스 전반에서 자연스럽게 이루어져야 한다.
- 이를 지속적으로 통합도 할 줄 알아야한다.

이 셋이 되면 지금 필요없을 걸?(YAGNI) 해도 응~ 나중에 바꿀거야~ 할 수 있다는 것이다.

이미 알고 있지만 아는 것과 실천하는 것은 다르다. 부디 이 스터디로 계속 연습할 수 있길 바란다...

## 2.8 리팩터링과 성능

리팩터링 해도 느려질 수는 있지만, 이건 매우 근시안적인 관점이며 일단 튜닝하기 쉬운 구조를 만들고 속도를 내는게 더 낫다고 제안하는 단락이다.

마틴이 겪어 본 빠른 소프트웨어 작성법 세 가지는
- 시간 예산분배 방법 - 하드 리얼타임 시스템에 사용. 무조건 되어야 하는 시스템.
- 끊임없이 관심을 기울이는 법 - 빨라지는 것 같지만 진짜 빨라지는 건 아니고 정작 컴파일러/런타임/하드웨어의 실질적 동작은 아무것도 모르는 케이스
- 코드를 최적화하면 그중 90%는 효과가 거의 없다는 부분을 이해하고, 성능최적화를 들어가기 전엔 그냥 코드부터 쉽게 짜는 것에 집중한다.

리팩터를 잘 해놓으면 프로파일러로 분석할 때 아래 이점을 얻을 수 있다
- 코드 짤 시간이 짧아졌으므로 이 시간을 프로파일링에 쓸 수 있다
- 분석할 코드들이 짧게 나누어져 있으므로 생각의 범위를 다른 부분에 할애할 수 있다(개선안, 튜닝의 구체적 안건)

## 2.9 리팩터링의 유래

80년대 Smalltalk 얘기부터 나오며 기여한 사람들이 많이 나온다. 일종의 Acknowledgements 같은 내용같다.

## 2.10 리팩터링 자동화

JetBrains나 vscode에서도 해준다. IDE를 무조건적으로 잘 활용하자. 책의 기법을 학습하고 내가 다루는 도구에서 이걸 해주는지 보면 된다. 십중팔구 되어있을 걸?

[^1]: 6.1절
[^2]: 10.4절
[^3]: 6.5절
[^4]: 8.1절
[^5]: https://product.kyobobook.co.kr/detail/S000001805070
[^6]: https://martinfowler.com/bliki/DesignStaminaHypothesis.html
[^7]: 11.2절
[^8]: https://martinfowler.com/articles/preparatory-refactoring-example.html
[^9]: https://martinfowler.com/bliki/BranchByAbstraction.html
[^10]: https://product.kyobobook.co.kr/detail/S000001804724 이 책입니다. <br />그리고 이 책을 통한 한국의 좋은 아티클 두 가지를 함께 소개합니다. <br />https://tosspayments-dev.oopy.io/66bd4494-792a-4137-82bc-57eb41f32345<br />https://techblog.woowahan.com/2613/
