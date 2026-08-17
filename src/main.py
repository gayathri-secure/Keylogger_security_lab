from src.formatter import format_event
from src.input_source import TestInputSource
from src.logger import write_event


def process_event(event):
    formatted_event = format_event(event)
    write_event(formatted_event)


def main():
    input_source = TestInputSource()
    event = input_source.get_event()
    process_event(event)

    print("Test event written successfully.")


if __name__ == "__main__":
    main()
