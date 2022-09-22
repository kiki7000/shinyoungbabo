from AssacCore.models.dataclass.job import Job

from typing import Optional
from random import choice


__all__ = ("JobList",)


class JobList:
    jobs = [
        Job(
            name="바보",
            work=True,
            earnMoney={"min": 1000, "max": 10000},
            hpDecrement={"min": 5, "max": 10},
            earnItem=[],
        ),
        Job(
            name="천재",
            work=True,
            earnMoney={"min": 2000, "max": 20000},
            hpDecrement={"min": 10, "max": 20},
            earnItem=[],
        ),
    ]

    @classmethod
    def find(cls, name: str) -> Optional[Job]:
        for job in cls.jobs:
            if job.name == name:
                return job
        return None

    @classmethod
    def choice(cls) -> Job:
        return choice(cls.jobs)
