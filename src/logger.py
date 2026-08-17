from src.config import LOG_DIR, LOG_FILE, MAX_LOG_SIZE


class LoggingError(Exception):
    """Raised when an event cannot be written to the log."""


def _rotate_log():
    rotated_file = LOG_DIR / "events.log.1"

    if LOG_FILE.exists():
        LOG_FILE.replace(rotated_file)


def write_event(event):
    try:
        LOG_DIR.mkdir(exist_ok=True)

        event_data = event + "\n"
        event_size = len(event_data.encode("utf-8"))

        current_size = (
            LOG_FILE.stat().st_size
            if LOG_FILE.exists()
            else 0
        )

        if current_size + event_size > MAX_LOG_SIZE:
            _rotate_log()

        with LOG_FILE.open("a", encoding="utf-8") as file:
            file.write(event_data)

    except OSError as exc:
        raise LoggingError(
            f"Unable to write event to {LOG_FILE}"
        ) from exc
