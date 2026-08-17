from pathlib import Path

import src.logger as logger


def test_write_event(tmp_path, monkeypatch):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "events.log"

    monkeypatch.setattr(logger, "LOG_DIR", log_dir)
    monkeypatch.setattr(logger, "LOG_FILE", log_file)

    logger.write_event("TEST_EVENT")

    assert log_file.exists()
    assert log_file.read_text(encoding="utf-8") == "TEST_EVENT\n"
