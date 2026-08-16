from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "events.log"


def write_event(event):
    LOG_DIR.mkdir(exist_ok=True)

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(event + "\n")
