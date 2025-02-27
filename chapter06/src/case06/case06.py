from dataclasses import dataclass


@dataclass(frozen=True)
class Owner:
    first_name: str
    last_name: str


@dataclass
class Spaceship:
    owner: Owner


# 모듈 레벨 변수
_default_owner = Owner(first_name="Martin", last_name="Fowler")


# getter 함수 - 이미 불변 객체이므로 그대로 반환해도 안전
def get_owner():
    """현재 소유자 정보 반환"""
    return _default_owner


# setter 함수
def set_owner(new_owner):
    """소유자 정보 변경"""
    global _default_owner
    _default_owner = new_owner
