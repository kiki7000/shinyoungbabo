from odmantic import AIOEngine

from typing import Optional

from ..errors import InvalidParameters, NotFound
from ..data.jobs import JobList

from .base import AssacModel
from .bag import Bag

from .dataclass.job import Job
from .database.user import DUser


class User(AssacModel):
    def __init__(self, engine: AIOEngine, id: int = None, data: DUser = None):
        super().__init__(engine)

        if id is None and data is not None:
            raise InvalidParameters("Cannot pass both id and data parameter")
        elif data is not None:
            self.data: DUser = data
        elif id is not None:
            res = await engine.find_one(DUser, DUser.discordID == id)
            if res is None:
                raise NotFound("User is not registered")
            self.data: DUser = res
        else:
            raise InvalidParameters("You should pass id or data parameter")

    @property
    def id(self) -> int:
        return self.data.discordID

    @property
    def money(self) -> int:
        return self.data.money

    @property
    def hp(self) -> int:
        return self.data.hp

    @property
    def maxHP(self) -> int:
        return self.data.maxHP

    @property
    def level(self) -> int:
        return self.data.level

    @property
    def xp(self) -> int:
        return self.xp

    @property
    def job(self) -> Optional[Job]:
        return JobList.find(self.data.job)

    @property
    def bag(self) -> Bag:
        return Bag(self.data.bag)

    @property
    def stocks(self):
        raise NotImplementedError("Todo")

    @property
    def team(self):
        raise NotImplementedError("Todo")
