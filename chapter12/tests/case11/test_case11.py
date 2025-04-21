from datetime import (
    datetime,
    timedelta,
)

import pytest

from chapter12.src.case11.case11 import (
    CatalogItem,
    Scroll,
    CatalogRepository,
    create_scroll,
    load_scrolls_from_records,
)


@pytest.fixture
def catalog_repo():
    return CatalogRepository()


@pytest.fixture
def history_catalog_item(catalog_repo):
    item = CatalogItem(item_id="C123", title="고대 역사서", tags=["history", "ancient"])
    return catalog_repo.register_item(item)


@pytest.fixture
def greek_catalog_item(catalog_repo):
    item = CatalogItem(
        item_id="C456", title="고대 그리스 문화", tags=["history", "culture", "greek"]
    )
    return catalog_repo.register_item(item)


@pytest.fixture
def religious_catalog_item(catalog_repo):
    item = CatalogItem(
        item_id="C789", title="신성한 문서", tags=["religious", "revered", "ancient"]
    )
    return catalog_repo.register_item(item)


@pytest.fixture
def regular_scroll(greek_catalog_item):
    return Scroll(
        scroll_id="S123",
        catalog_item=greek_catalog_item,
        date_last_cleaned=datetime(2023, 1, 1),
    )


@pytest.fixture
def revered_scroll(religious_catalog_item):
    return Scroll(
        scroll_id="S456",
        catalog_item=religious_catalog_item,
        date_last_cleaned=datetime(2023, 1, 1),
    )


# 카탈로그 아이템 테스트
def test_catalog_item_properties(history_catalog_item):
    assert history_catalog_item.item_id == "C123"
    assert history_catalog_item.title == "고대 역사서"
    assert history_catalog_item.has_tag("history") is True
    assert history_catalog_item.has_tag("fiction") is False


# 카탈로그 저장소 테스트
def test_catalog_repository(catalog_repo):
    # 아이템 등록 및 조회
    item = CatalogItem(item_id="C999", title="테스트 문서", tags=["test"])
    catalog_repo.register_item(item)

    found_item = catalog_repo.find_item("C999")
    assert found_item is item
    assert found_item.title == "테스트 문서"

    # 없는 아이템 조회
    not_found = catalog_repo.find_item("NONEXISTENT")
    assert not_found is None

    # ensure_item - 기존 아이템 조회
    ensured_item = catalog_repo.ensure_item("C999", "다른 제목", ["other"])
    assert ensured_item is item  # 동일 인스턴스 반환
    assert ensured_item.title == "테스트 문서"  # 원래 제목 유지

    # ensure_item - 새 아이템 생성
    new_item = catalog_repo.ensure_item("NEW_ID", "새 문서", ["new"])
    assert new_item.item_id == "NEW_ID"
    assert catalog_repo.find_item("NEW_ID") is new_item


# 스크롤 기본 기능 테스트
def test_scroll_properties(regular_scroll, greek_catalog_item):
    assert regular_scroll.scroll_id == "S123"
    assert regular_scroll.catalog_item_id == "C456"
    assert regular_scroll.title == "고대 그리스 문화"
    assert regular_scroll._catalog_item is greek_catalog_item  # 동일 객체 참조 확인


def test_scroll_has_tag(regular_scroll):
    assert regular_scroll.has_tag("greek") is True
    assert regular_scroll.has_tag("fiction") is False


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


# 참조 공유 테스트
def test_scrolls_share_catalog_item(catalog_repo, greek_catalog_item):
    # 동일한 카탈로그 아이템을 참조하는 여러 스크롤 생성
    scroll1 = Scroll("S1", greek_catalog_item, datetime(2023, 1, 1))
    scroll2 = Scroll("S2", greek_catalog_item, datetime(2023, 2, 1))
    scroll3 = Scroll("S3", greek_catalog_item, datetime(2023, 3, 1))

    # 모두 동일한 카탈로그 아이템을 참조하는지 확인
    assert scroll1._catalog_item is scroll2._catalog_item
    assert scroll2._catalog_item is scroll3._catalog_item
    assert scroll1.title == scroll2.title == scroll3.title == "고대 그리스 문화"

    # 스크롤별 고유 정보는 다른지 확인
    assert scroll1.scroll_id != scroll2.scroll_id
    assert scroll1._last_cleaned != scroll2._last_cleaned


# 팩토리 함수 테스트
def test_create_scroll(catalog_repo):
    # 새 카탈로그 아이템으로 스크롤 생성
    scroll1 = create_scroll(
        scroll_id="S-NEW-1",
        catalog_item_id="C-NEW",
        title="신규 문서",
        tags=["new", "document"],
        date_last_cleaned=datetime(2023, 4, 1),
        catalog_repo=catalog_repo,
    )

    # 같은 카탈로그 아이템 ID로 다른 스크롤 생성
    scroll2 = create_scroll(
        scroll_id="S-NEW-2",
        catalog_item_id="C-NEW",
        title="변경된 제목 (무시됨)",  # 이미 등록된 카탈로그 아이템이 있으므로 무시됨
        tags=["changed", "tags"],  # 마찬가지로 무시됨
        date_last_cleaned=datetime(2023, 5, 1),
        catalog_repo=catalog_repo,
    )

    # 검증
    assert scroll1.scroll_id == "S-NEW-1"
    assert scroll2.scroll_id == "S-NEW-2"
    assert scroll1.catalog_item_id == scroll2.catalog_item_id == "C-NEW"
    assert (
        scroll1.title == scroll2.title == "신규 문서"
    )  # 첫 번째 스크롤의 제목이 유지됨
    assert scroll1._catalog_item is scroll2._catalog_item  # 동일 객체 참조

    # 저장소에서도 동일 객체 조회되는지 확인
    catalog_item = catalog_repo.find_item("C-NEW")
    assert catalog_item is scroll1._catalog_item
    assert catalog_item.title == "신규 문서"


# 데이터 로딩 테스트
def test_load_scrolls_from_records(catalog_repo):
    # 테스트 레코드 데이터
    records = [
        {
            "id": "S001",
            "catalog_data": {
                "id": "CAT001",
                "title": "철학의 기초",
                "tags": ["philosophy", "education"],
            },
            "last_cleaned": "2023-01-01",
        },
        {
            "id": "S002",
            "catalog_data": {
                "id": "CAT001",  # 첫 번째 레코드와 동일한 카탈로그 ID
                "title": "철학의 기초",
                "tags": ["philosophy", "education"],
            },
            "last_cleaned": "2023-02-01",
        },
        {
            "id": "S003",
            "catalog_data": {
                "id": "CAT002",  # 다른 카탈로그 ID
                "title": "고대 로마 역사",
                "tags": ["history", "roman"],
            },
            "last_cleaned": "2023-03-01",
        },
    ]

    # 레코드로부터 스크롤 로딩
    scrolls = load_scrolls_from_records(records, catalog_repo)

    # 검증
    assert len(scrolls) == 3
    assert scrolls[0].scroll_id == "S001"
    assert scrolls[1].scroll_id == "S002"
    assert scrolls[2].scroll_id == "S003"

    # 같은 카탈로그 아이템을 공유하는지 확인
    assert scrolls[0].catalog_item_id == scrolls[1].catalog_item_id == "CAT001"
    assert scrolls[0]._catalog_item is scrolls[1]._catalog_item

    # 다른 카탈로그 아이템은 별도 객체인지 확인
    assert scrolls[2].catalog_item_id == "CAT002"
    assert scrolls[2]._catalog_item is not scrolls[0]._catalog_item

    # 카탈로그 저장소 확인
    assert len(catalog_repo._items) == 2  # 두 개의 카탈로그 아이템만 저장됨
    assert catalog_repo.find_item("CAT001") is scrolls[0]._catalog_item
    assert catalog_repo.find_item("CAT002") is scrolls[2]._catalog_item
