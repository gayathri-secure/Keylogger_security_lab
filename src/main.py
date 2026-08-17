from src.formatter import format_event
from src.input_source import TestInputSource
from src.logger import LoggingError, write_event


def process_event(event):
    formatted_event = format_event(event)

    try:
        write_event(formatted_event)
    except LoggingError as exc:
        print(f"Logging failed: {exc}")
        return False

    return True


def main():
    input_source = TestInputSource()
    event = input_source.get_event()

    if process_event(event):
        print("Test event written successfully.")


if __name__ == "__main__":
    main()
