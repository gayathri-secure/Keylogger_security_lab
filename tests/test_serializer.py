from datetime import datetime
import json

from src.event import Event
from src.serializer import serialize_event


def test_serialize_event():
    event = Event(
        timestamp=datetime(2026, 8, 18, 0, 10, 0),
        event_type="TEST",
        value="STRUCTURED_EVENT",
        source="test_source"
    )

    result = serialize_event(event)
    data = json.loads(result)

    assert data == {
        "timestamp": "2026-08-18T00:10:00",
        "event_type": "TEST",
        "value": "STRUCTURED_EVENT",
        "source": "test_source",
    }


def test_serialize_event_preserves_unicode():
    event = Event(
        timestamp=datetime(2026, 8, 18, 0, 15, 0),
        event_type="TEST",
        value="Hello தமிழ்",
        source="test_source"
    )

    result = serialize_event(event)
    data = json.loads(result)

    assert data["value"] == "Hello தமிழ்"
