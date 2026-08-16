from formatter import format_event
from logger import write_event


def main():
    event = "TEST_EVENT"

    formatted_event = format_event(event)
    write_event(formatted_event)

    print("Test event written successfully.")


if __name__ == "__main__":
    main()
