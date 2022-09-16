from dataclasses import dataclass
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