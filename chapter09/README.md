# 9장 - 데이터 조직화

데이터 구조는 프로그램에서 중요한 역할을 수행한다. 따라서 데이터 구조에 집중한 리팩터링도 배워둘 필요가 있다. 여기서는 하나의 값이 여러 목적으로 쓰이는 것을 극도로 경계한다.

이런 코드는 변수 쪼개기(9.1절)로 용도별로 분리해야한다. 변수에 이름을 제대로 짓는 건 그만큼 중요하다. 변수 이름 바꾸기(6.7절)는 그런 의미로 반드시 잘 해줘야한다. 필요하면 파생변수를 질의 함수로 바꾸기(9.3절)을 활용해서 변수 자체를 없애주는 것도 방법일 수 있다.

참조(_reference_)인지, 값(_value_)인지 헷갈릴 때가 있다. 그 둘 사이를 전환할 때는 참조를 값으로 바꾸기 (9.4절), 값을 참조로 바꾸기(9.5절)를 써야한다. 코드에 의미를 알기 어려운 리터럴이 있다면 매직 리터럴 바꾸기 (9.6절)로 명확하게 바꾼다.
