from odmantic import Model

from typing import List, Optional
from abc import ABC


__all__ = ("DUser",)


class DUser(Model, ABC):
    discordID: int
    money: int = 0

    hp: int = 100
    maxHP: int = 100

    level: int = 1
    xp: int = 0

    job: str
    bag: List[str] = []
    stocks: List[str] = []
    team: Optional[str] = None

    class Config:
        collection = "users"
