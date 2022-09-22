from dataclasses import dataclass
from typing import TypedDict, List

from AssacCore.models.dataclass.item import Item


__all__ = ("Job",)


@dataclass
class Job:
    name: str
    work: bool

    earnMoney: TypedDict("earnMoney", {"max": int, "min": int})
    hpDecrement: TypedDict("hpDecrement", {"max": int, "min": int})
    earnItem: List[TypedDict("earnItem", {"max": int, "min": int, "item": Item})]
