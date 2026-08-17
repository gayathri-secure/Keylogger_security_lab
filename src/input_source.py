from datetime import datetime
from typing import Protocol

from src.event import Event


class InputSource(Protocol):
    def get_event(self) -> Event:
        ...


class TestInputSource:
    def get_event(self) -> Event:
        return Event(
            timestamp=datetime.now(),
            event_type="TEST",
            value="TEST_EVENT"
        )
