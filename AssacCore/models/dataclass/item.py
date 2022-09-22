from dataclasses import dataclass
from typing import Literal, Dict, Optional


__all__ = ("Item", "ShopItem")


@dataclass
class Item:
    name: str
    size: int

    type: Literal["normal", "package"]
    sellingPlace: Literal["craft", "none", "shop"]

    info: str
    canUse: bool = True

    craftAble: bool = False
    material: Optional[Dict[str, int]] = None


@dataclass
class ShopItem(Item):
    stock: int = 0
