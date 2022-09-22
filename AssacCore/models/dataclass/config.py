from dataclasses import dataclass


__all__ = ("Config",)


@dataclass
class Config:
    dbURL: str
