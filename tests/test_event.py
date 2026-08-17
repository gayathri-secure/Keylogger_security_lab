from datetime import datetime

import pytest

from src.event import Event


def test_valid_event():
    event = Event(
        timestamp=datetime.now(),
        event_type="TEST",
        value="TEST_EVENT"
    )

    assert event.event_type == "TEST"
    assert event.value == "TEST_EVENT"


def test_empty_event_type():
    with pytest.raises(ValueError, match="event_type cannot be empty"):
        Event(
            timestamp=datetime.now(),
            event_type="",
            value="TEST_EVENT"
        )


def test_empty_value():
    with pytest.raises(ValueError, match="value cannot be empty"):
        Event(
            timestamp=datetime.now(),
            event_type="TEST",
            value=""
        )
