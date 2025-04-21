from datetime import datetime


class CatalogRepository:
    def __init__(self):
        self._items = {}

    def register_item(self, catalog_item):
        self._items[catalog_item.item_id] = catalog_item
        return catalog_item

    def find_item(self, item_id):
        return self._items.get(item_id)

    def ensure_item(self, item_id, title, tags):
        """해당 ID의 카탈로그 아이템을 찾거나, 없으면 새로 생성하여 등록"""
        item = self.find_item(item_id)
        if item is None:
            item = self.register_item(CatalogItem(item_id, title, tags))
        return item


class CatalogItem:
    def __init__(self, item_id, title, tags):
        self._item_id = item_id
        self._title = title
        self._tags = tags

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    def has_tag(self, arg):
        return arg in self._tags


class Scroll:
    def __init__(self, scroll_id, catalog_item, date_last_cleaned):
        self._scroll_id = scroll_id
        self._catalog_item = catalog_item
        self._last_cleaned = date_last_cleaned

    @property
    def scroll_id(self):
        return self._scroll_id

    @property
    def catalog_item_id(self):
        return self._catalog_item.item_id

    @property
    def title(self):
        return self._catalog_item.title

    def has_tag(self, arg):
        return self._catalog_item.has_tag(arg)

    def needs_cleaning(self, target_date):
        threshold = 700 if self.has_tag("revered") else 1500
        return self.days_since_last_cleaning(target_date) > threshold

    def days_since_last_cleaning(self, target_date):
        # 파이썬의 datetime은 Java의 ChronoUnit.DAYS와 다르게 작동하므로 조정
        delta = target_date - self._last_cleaned
        return delta.days


# 팩토리 함수
def create_scroll(
    scroll_id, catalog_item_id, title, tags, date_last_cleaned, catalog_repo
):
    """스크롤을 생성하고 카탈로그 아이템을 공유할 수 있게 함"""
    # 카탈로그 아이템 검색 또는 생성
    catalog_item = catalog_repo.ensure_item(catalog_item_id, title, tags)

    # 스크롤 생성 (카탈로그 아이템 참조)
    return Scroll(scroll_id, catalog_item, date_last_cleaned)


# 데이터 로딩 함수
def load_scrolls_from_records(records, catalog_repo):
    """레코드 데이터로부터 스크롤 객체 목록 생성"""
    scrolls = []
    for record in records:
        scroll = create_scroll(
            scroll_id=record["id"],
            catalog_item_id=record["catalog_data"]["id"],
            title=record["catalog_data"]["title"],
            tags=record["catalog_data"]["tags"],
            date_last_cleaned=datetime.fromisoformat(record["last_cleaned"]),
            catalog_repo=catalog_repo,
        )
        scrolls.append(scroll)
    return scrolls
