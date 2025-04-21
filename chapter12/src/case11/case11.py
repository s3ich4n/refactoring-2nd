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
    def __init__(self, item_id, title, tags, date_last_cleaned):
        self._catalog_item = CatalogItem(item_id, title, tags)
        self._last_cleaned = date_last_cleaned

    @property
    def item_id(self):
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
