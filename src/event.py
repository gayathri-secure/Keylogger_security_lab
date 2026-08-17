from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    timestamp: datetime
    event_type: str
    value: str
    source: str

    def __post_init__(self):
        if not self.event_type.strip():
            raise ValueError("event_type cannot be empty")

        if not self.value.strip():
            raise ValueError("value cannot be empty")

        if not self.source.strip():
            raise ValueError("source cannot be empty")

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "event_type": self.event_type,
            "value": self.value,
            "source": self.source,
        }
