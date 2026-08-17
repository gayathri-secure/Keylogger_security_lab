from datetime import datetime

import pytest

from src.event import Event


def test_valid_event():
    event = Event(
        timestamp=datetime.now(),
        event_type="TEST",
        value="TEST_EVENT",
        source="test_source"
    )

    assert event.event_type == "TEST"
    assert event.value == "TEST_EVENT"
    assert event.source == "test_source"


def test_empty_event_type():
    with pytest.raises(ValueError, match="event_type cannot be empty"):
        Event(
            timestamp=datetime.now(),
            event_type="",
            value="TEST_EVENT",
            source="test_source"
        )


def test_empty_value():
    with pytest.raises(ValueError, match="value cannot be empty"):
        Event(
            timestamp=datetime.now(),
            event_type="TEST",
            value="",
            source="test_source"
        )


def test_empty_source():
    with pytest.raises(ValueError, match="source cannot be empty"):
        Event(
            timestamp=datetime.now(),
            event_type="TEST",
            value="TEST_EVENT",
            source=""
        )


def test_event_to_dict():
    timestamp = datetime(2026, 8, 18, 0, 10, 0)

    event = Event(
        timestamp=timestamp,
        event_type="TEST",
        value="STRUCTURED_EVENT",
        source="test_source"
    )

    result = event.to_dict()

    assert result == {
        "timestamp": "2026-08-18T00:10:00",
        "event_type": "TEST",
        "value": "STRUCTURED_EVENT",
        "source": "test_source",
    }
