# 10.6 어서션 추가하기

_Introduce Assertion_

## 개요

Before

```python
if self.discount_rate:
    base = base - (self.discount_rate * base)
```

After

```python
assert self.discount_rate >= 0

if self.discount_rate:
    base = base - (self.discount_rate * base)
```

## 배경

특정 조건이 참인걸 반드시 보장해야하는 때가 있다.

그 때는 언어 별 assertion을 통해 이를 보장하는 것이 좋다. 그렇지만...

> ![WARNING]
> 
> 어서션은 시스템 운영에 영향을 주면 안 된다. 어서션 추가가 있다한들 시스템 동작이 달라지지는 않아야 한다


## 절차

1. 참이라 가정하는 조건이 보이면 그 조건을 명시하는 어서션을 추가한다.

## 예시
