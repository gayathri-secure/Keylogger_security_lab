from datetime import datetime

import src.main as main
from src.event import Event

from src.logger import LoggingError

def test_process_event(tmp_path, monkeypatch):
    log_dir = tmp_path / "logs"
    log_file = log_dir / "events.log"

    def fake_write_event(event):
        log_dir.mkdir(exist_ok=True)
        log_file.write_text(
            event + "\n",
            encoding="utf-8"
        )

    monkeypatch.setattr(main, "write_event", fake_write_event)

    event = Event(
        timestamp=datetime(2026, 8, 17, 16, 30, 0),
        event_type="TEST",
        value="INTEGRATION_TEST",
        source="test_source"
    )

    main.process_event(event)

    assert log_file.exists()
    assert log_file.read_text(encoding="utf-8") == (
        "[2026-08-17 16:30:00] [TEST] [test_source] INTEGRATION_TEST\n"
    )
def test_process_event_handles_logging_error(monkeypatch, capsys):
    def fail_write_event(event):
        raise LoggingError("simulated logging failure")

    monkeypatch.setattr(main, "write_event", fail_write_event)

    event = Event(
        timestamp=datetime(2026, 8, 17, 16, 30, 0),
        event_type="TEST",
        value="FAILURE_TEST",
        source="test_source"
    )

    result = main.process_event(event)

    captured = capsys.readouterr()

    assert result is False
    assert "Logging failed: simulated logging failure" in captured.out
