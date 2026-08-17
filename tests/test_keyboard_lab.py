import src.keyboard_lab as keyboard_lab


def test_empty_input_is_ignored(monkeypatch):
    processed_events = []

    monkeypatch.setattr(
        keyboard_lab,
        "process_event",
        lambda event: processed_events.append(event)
    )

    result = keyboard_lab.process_test_input("   ")

    assert result is False
    assert processed_events == []


def test_valid_input_creates_event(monkeypatch):
    processed_events = []

    monkeypatch.setattr(
        keyboard_lab,
        "process_event",
        lambda event: processed_events.append(event)
    )

    result = keyboard_lab.process_test_input("HELLO LAB")

    assert result is True
    assert len(processed_events) == 1

    event = processed_events[0]

    assert event.event_type == "KEYBOARD_TEST"
    assert event.value == "HELLO LAB"
