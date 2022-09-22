from odmantic import AIOEngine

from typing import Any


__all__ = ("AssacModel",)


class AssacModel:
    def __init__(self, engine: AIOEngine):
        self.engine: AIOEngine = engine
        self.data: Any = None

    async def save(self):
        await self.engine.save(self.data)
