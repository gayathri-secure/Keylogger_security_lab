from datetime import datetime

from event import Event
from formatter import format_event
from logger import write_event


def main():
    event = Event(
        timestamp=datetime.now(),
        event_type="TEST",
        value="TEST_EVENT"
    )

    formatted_event = format_event(event)
    write_event(formatted_event)

    print("Test event written successfully.")


if __name__ == "__main__":
    main()
