from datetime import (
    datetime,
    timedelta,
)

import pytest

from chapter12.src.case11.case11 import (
    CatalogItem,
    Scroll,
)


@pytest.fixture
def catalog_item():
    return CatalogItem(item_id="C123", title="고대 역사서", tags=["history", "ancient"])


@pytest.fixture
def regular_scroll():
    return Scroll(
        item_id="S789",
        title="고대 그리스 문화",
        tags=["history", "culture", "greek"],
        date_last_cleaned=datetime(2023, 1, 1),
    )


@pytest.fixture
def revered_scroll():
    return Scroll(
        item_id="S456",
        title="신성한 문서",
        tags=["religious", "revered", "ancient"],
        date_last_cleaned=datetime(2023, 1, 1),
    )


def test_catalog_item_properties(catalog_item):
    assert catalog_item.item_id == "C123"
    assert catalog_item.title == "고대 역사서"
    assert catalog_item.has_tag("history") is True
    assert catalog_item.has_tag("fiction") is False


def test_scroll_inheritance(regular_scroll):
    # 부모 클래스에서 상속받은 속성과 메서드 테스트
    assert regular_scroll.item_id == "S789"
    assert regular_scroll.title == "고대 그리스 문화"
    assert regular_scroll.has_tag("greek") is True


def test_days_since_last_cleaning(regular_scroll):
    # 90일 후
    target_date = regular_scroll._last_cleaned + timedelta(days=90)
    assert regular_scroll.days_since_last_cleaning(target_date) == 90

    # 2000일 후
    target_date = regular_scroll._last_cleaned + timedelta(days=2000)
    assert regular_scroll.days_since_last_cleaning(target_date) == 2000


def test_regular_scroll_needs_cleaning(regular_scroll):
    # 1000일 후 (임계값 1500일 미만) - 청소 필요 없음
    target_date = regular_scroll._last_cleaned + timedelta(days=1000)
    assert regular_scroll.needs_cleaning(target_date) is False

    # 2000일 후 (임계값 1500일 초과) - 청소 필요함
    target_date = regular_scroll._last_cleaned + timedelta(days=2000)
    assert regular_scroll.needs_cleaning(target_date) is True


def test_revered_scroll_needs_cleaning(revered_scroll):
    # 500일 후 (임계값 700일 미만) - 청소 필요 없음
    target_date = revered_scroll._last_cleaned + timedelta(days=500)
    assert revered_scroll.needs_cleaning(target_date) is False

    # 800일 후 (임계값 700일 초과) - 청소 필요함
    target_date = revered_scroll._last_cleaned + timedelta(days=800)
    assert revered_scroll.needs_cleaning(target_date) is True
