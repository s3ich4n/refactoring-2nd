# 10.7 제어 플래그를 탈출문으로 바꾸기

_Replace Control Flag with Break_

## 개요

Before

```python
found = False
for p in people:
    if not found:
        if p == "joker":
            send_alert()
            found = True
```

After

```python
for p in people:
    if p == "joker":
        send_alert()
        break
```

## 배경

제어 플래그로 동작을 변경하는 건 항상 존재할 수 있다. 그런데 이렇게 제어 플래그로 설정하고 다른데서 그걸 쓰는 건 간소화할 수 있다.

마틴 파울러는 차라리 break문이나 return 문으로 이렇게 흐름을 빨리 썰어내는걸 제안한다.

## 절차

1. 제어 플래그를 사용하는 코드를 함수로 추출(6.1절)할지 고민한다
2. 제어 플래그를 갱신하는 각각의 코드를 제어문으로 바꾼다. 하나 바꾸고나서 테스트한다. <br />
→ 제어문으로는 주로 `return`, `break`, continue` 가 쓰인다
3. 모두 수정했다면 제어 플래그를 제거한다

## 예시
