from datetime import datetime

from src.event import Event
from src.formatter import format_event


def test_format_event():
    timestamp = datetime(2026, 8, 17, 16, 20, 30)

    event = Event(
        timestamp=timestamp,
        event_type="TEST",
        value="HELLO"
    )

    result = format_event(event)

    assert result == "[2026-08-17 16:20:30] [TEST] HELLO"
