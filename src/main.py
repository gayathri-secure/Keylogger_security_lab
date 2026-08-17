from src.formatter import format_event
from src.input_source import get_test_event
from src.logger import write_event


def process_event(event):
    formatted_event = format_event(event)
    write_event(formatted_event)


def main():
    event = get_test_event()
    process_event(event)

    print("Test event written successfully.")


if __name__ == "__main__":
    main()
