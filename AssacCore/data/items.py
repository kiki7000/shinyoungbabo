from AssacCore.models.dataclass.item import Item

from typing import Optional, Union


__all__ = ("ItemList",)


class ItemList:
    items = [
        Item(
            name="시녕죽이기",
            size=100,
            type="normal",
            sellingPlace="shop",
            info="키키천재"
        )
    ]

    @classmethod
    def find(cls, name: str) -> Optional[Item]:
        for item in cls.items:
            if item.name == name:
                return item
        return None

    @classmethod
    def to_item(cls, item: Union[str, Item]) -> Optional[Item]:
        if isinstance(item, str):
            return cls.find(item)
        elif isinstance(item, Item):
            return item
