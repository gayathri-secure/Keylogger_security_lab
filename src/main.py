from src.formatter import format_event
from src.input_source import InputSource, TestInputSource
from src.logger import LoggingError, write_event


def process_event(event):
    formatted_event = format_event(event)

    try:
        write_event(formatted_event)
    except LoggingError as exc:
        print(f"Logging failed: {exc}")
        return False

    return True


def run_source(input_source: InputSource):
    event = input_source.get_event()
    return process_event(event)


def main():
    input_source = TestInputSource()

    if run_source(input_source):
        print("Test event written successfully.")


if __name__ == "__main__":
    main()
