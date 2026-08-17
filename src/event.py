from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    timestamp: datetime
    event_type: str
    value: str

    def __post_init__(self):
        if not self.event_type.strip():
            raise ValueError("event_type cannot be empty")

        if not self.value.strip():
            raise ValueError("value cannot be empty")

    @classmethod
    def create_test_event(cls):
        return cls(
            timestamp=datetime.now(),
            event_type="TEST",
            value="TEST_EVENT"
        )
