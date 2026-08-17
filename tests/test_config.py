from pathlib import Path

import src.config as config


def test_default_config_paths(monkeypatch):
    monkeypatch.delenv("KEYLOGGER_LAB_LOG_DIR", raising=False)

    # Reload the module so it reads the changed environment.
    import importlib
    importlib.reload(config)

    assert config.PROJECT_ROOT.exists()
    assert config.LOG_DIR == config.PROJECT_ROOT / "logs"
    assert config.LOG_FILE == config.LOG_DIR / "events.log"
    assert isinstance(config.LOG_FILE, Path)


def test_custom_log_directory(monkeypatch, tmp_path):
    custom_dir = tmp_path / "custom_logs"

    monkeypatch.setenv(
        "KEYLOGGER_LAB_LOG_DIR",
        str(custom_dir)
    )

    import importlib
    importlib.reload(config)

    assert config.LOG_DIR == custom_dir
    assert config.LOG_FILE == custom_dir / "events.log"

    # Restore default configuration for the rest of the test session.
    monkeypatch.delenv("KEYLOGGER_LAB_LOG_DIR", raising=False)
    importlib.reload(config)
