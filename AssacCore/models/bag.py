from typing import List, Union

from ..data.items import ItemList
from .dataclass.item import Item


class Bag:
    def __init__(self, item_list: List[Union[str, Item]]):
        self.items: List[Item] = [ItemList.to_item(name) for name in item_list]

    def add_item(self, item: Union[str, Item]):
        self.items.append(ItemList.to_item(item))

    def __setitem__(self, key, value: Union[str, Item]):
        self.items[key] = ItemList.to_item(value)

    def __delitem__(self, key):
        del self.items[key]

    def __iter__(self):
        return self.items

    def __list__(self):
        return self.items

    def to_str(self):
        return [item.name for item in self.items]
