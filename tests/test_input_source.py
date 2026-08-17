from src.input_source import TestInputSource


def test_get_test_event():
    input_source = TestInputSource()

    event = input_source.get_event()

    assert event.event_type == "TEST"
    assert event.value == "TEST_EVENT"
