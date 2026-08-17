from pathlib import Path

from src.config import LOG_DIR, LOG_FILE, PROJECT_ROOT


def test_config_paths():
    assert PROJECT_ROOT.exists()
    assert LOG_DIR == PROJECT_ROOT / "logs"
    assert LOG_FILE == LOG_DIR / "events.log"
    assert isinstance(LOG_FILE, Path)
