from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "events.log"
