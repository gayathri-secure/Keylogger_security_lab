from src.config import LOG_DIR, LOG_FILE


class LoggingError(Exception):
    """Raised when an event cannot be written to the log."""


def write_event(event):
    try:
        LOG_DIR.mkdir(exist_ok=True)

        with LOG_FILE.open("a", encoding="utf-8") as file:
            file.write(event + "\n")

    except OSError as exc:
        raise LoggingError(
            f"Unable to write event to {LOG_FILE}"
        ) from exc
