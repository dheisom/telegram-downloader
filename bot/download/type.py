from dataclasses import dataclass, field

from pyrogram.types import Message


@dataclass
class Download:
    id: int
    filename: str
    from_message: Message
    added: float
    progress_message: Message
    started: float = 0
    last_update: float = 0
    last_call: float = 0
    size: int = 0


@dataclass
class Data:
    downloads: list[Download] = field(default_factory=list)
    running: int = 0
    stop: list[int] = field(default_factory=list)
