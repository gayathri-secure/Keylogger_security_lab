from src.config import LOG_DIR, LOG_FILE


def write_event(event):
    LOG_DIR.mkdir(exist_ok=True)

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(event + "\n")
