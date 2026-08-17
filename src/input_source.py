from datetime import datetime

from src.event import Event


def get_test_event():
    return Event(
        timestamp=datetime.now(),
        event_type="TEST",
        value="TEST_EVENT"
    )
