from dataclasses import dataclass, field
from typing import Optional
import time


@dataclass
class Detection:

    label: str

    confidence: float

    x1: int
    y1: int
    x2: int
    y2: int

    tracker_id: Optional[int] = None

    timestamp: float = field(default_factory=time.time)

    source: str = "YOLO"

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def center(self):
        return (
            (self.x1 + self.x2) // 2,
            (self.y1 + self.y2) // 2
        )