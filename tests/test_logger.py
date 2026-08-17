import pytest

import src.logger as logger


def test_write_event(tmp_path, monkeypatch):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "events.log"

    monkeypatch.setattr(logger, "LOG_DIR", log_dir)
    monkeypatch.setattr(logger, "LOG_FILE", log_file)

    logger.write_event("TEST_EVENT")

    assert log_file.exists()
    assert log_file.read_text(encoding="utf-8") == "TEST_EVENT\n"


def test_write_event_raises_logging_error(monkeypatch):
    def fail_mkdir(*args, **kwargs):
        raise OSError("simulated directory failure")

    monkeypatch.setattr(logger, "LOG_DIR", type("FakeLogDir", (), {
        "mkdir": fail_mkdir
    })())

    with pytest.raises(
        logger.LoggingError,
        match="Unable to write event"
    ):
        logger.write_event("TEST_EVENT")


def test_write_event_rotates_log(tmp_path, monkeypatch):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "events.log"
    rotated_file = log_dir / "events.log.1"

    monkeypatch.setattr(logger, "LOG_DIR", log_dir)
    monkeypatch.setattr(logger, "LOG_FILE", log_file)
    monkeypatch.setattr(logger, "MAX_LOG_SIZE", 20)

    logger.write_event("FIRST_EVENT")

    assert log_file.exists()
    assert log_file.read_text(encoding="utf-8") == "FIRST_EVENT\n"

    logger.write_event("SECOND_EVENT")

    assert rotated_file.exists()
    assert rotated_file.read_text(encoding="utf-8") == "FIRST_EVENT\n"

    assert log_file.exists()
    assert log_file.read_text(encoding="utf-8") == "SECOND_EVENT\n"


def test_write_event_raises_logging_error_during_rotation(
    tmp_path,
    monkeypatch
):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "events.log"

    monkeypatch.setattr(logger, "LOG_DIR", log_dir)
    monkeypatch.setattr(logger, "LOG_FILE", log_file)
    monkeypatch.setattr(logger, "MAX_LOG_SIZE", 1)

    log_dir.mkdir()
    log_file.write_text("OLD_EVENT\n", encoding="utf-8")

    def fail_rotation():
        raise OSError("simulated rotation failure")

    monkeypatch.setattr(logger, "_rotate_log", fail_rotation)

    with pytest.raises(
        logger.LoggingError,
        match="Unable to write event"
    ):
        logger.write_event("NEW_EVENT")
