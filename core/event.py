from dataclasses import dataclass, field
import time


@dataclass
class Event:

    name: str

    confidence: float

    timestamp: float = field(default_factory=time.time)

    description: str = ""