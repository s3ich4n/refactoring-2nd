# 6.7 변수 이름 바꾸기

_Rename Variable_

## 개요

Before

```python
a = height * width
```

```python
area = height * width
```

## 배경

이름 잘 짓는건 중요하다. 대충 짓는 것 뿐 아니라, 개발하다보니 이 이름 보다 다른 이름이 낫겠다 싶을 때가 온다.

맥락으로 바로 파악할 수 있게 하는게 중요하다.

특히 함수 호출 한 번으로 끝나는 게 아니라 값이 영속되는 필드면 이름에 더 신경써야한다.

## 절차

1. 폭넓게 쓰이는 변수라면 변수 캡슐화하기(6.6절)을 고려한다
2. 이름을 바꿀 변수를 참조하는 곳을 모두 찾아 하나씩 변경한다 <br />
→ 다른 코드베이스에서 참조하는 변수는 외부에 공개된 변수이므로 이 리팩터링을 적용할 수 없다 <br />
→ 변수 값이 변하지 않는다면 다른 이름으로 복제본을 만들어서 점진적으로 바꾼다. 하나 바꿀 때마다 테스트한다.
3. 테스트한다

## 예시

```python
tpHd = "untitled"

# 읽기만 하는 경우
result += f"<h1>{tpHd}</h1>"

# 쓰기만 하는 경우
tpHd = article_title
```

이럴 땐 변수 캡슐화하기 부터.

```python
class TitleManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._title = "untitled"
        return cls._instance
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, arg):
        self._title = arg

# 싱글턴 인스턴스 생성
title_manager = TitleManager()

# 접근자를 통한 접근
result += f"<h1>{title_manager.title}</h1>"

# 수정자를 통한 수정
title_manager.title = obj['article_title']
```

## 예시 - 상수 이름 바꾸기

```python
cpyNm = "애크미 구스베리"
```

이런건 의외로 쉽다:

```python
companyName = "애크미 구스베리"
cpyNm = companyName
```

이러고나서 점진적으로 `cpyNm` 을 `companyName` 으로 바꾼다.
