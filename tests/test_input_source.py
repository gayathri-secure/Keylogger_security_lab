from src.input_source import get_test_event


def test_get_test_event():
    event = get_test_event()

    assert event.event_type == "TEST"
    assert event.value == "TEST_EVENT"
