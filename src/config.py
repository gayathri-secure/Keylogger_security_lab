import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_LOG_DIR = PROJECT_ROOT / "logs"

LOG_DIR = Path(
    os.getenv("KEYLOGGER_LAB_LOG_DIR", DEFAULT_LOG_DIR)
)

LOG_FILE = LOG_DIR / "events.log"

MAX_LOG_SIZE = 1024 * 1024

