# Keylogger Security Lab

## Educational and Authorized-Use Disclaimer

This project is developed strictly for educational purposes, cybersecurity
learning, and authorized security research in controlled laboratory
environments.

Any testing involving this project must be performed only on systems owned by
the tester or where explicit authorization has been granted.

This project is intended to help understand keyboard-event monitoring concepts,
software behavior, logging, security indicators, detection techniques, and
defensive security measures.

The current laboratory implementation is intentionally controlled. It does not
capture keyboard input from arbitrary applications, browser windows, password
fields, or other users.

This project must not be used for unauthorized surveillance, credential theft,
privacy violations, or unauthorized access to systems or data.

---

## Project Overview

**Keylogger Security Lab** is an educational cybersecurity project designed to
study the technical concepts and security implications associated with
keyboard-event monitoring.

The project combines Python software engineering with cybersecurity concepts
such as:

- Keyboard-event handling in a controlled application
- Event modeling and validation
- Local security-event logging
- Human-readable log formatting
- Structured JSON Lines logging
- Log rotation and controlled log growth
- Error handling
- Automated testing
- Security-event analysis
- Detection concepts
- Defensive security measures

The project is developed incrementally using a milestone-based approach.

---

## Objectives

1. Understand how keyboard events can be handled programmatically in a
   controlled environment.
2. Develop a modular Python application.
3. Implement controlled local event logging.
4. Implement structured security-event representation.
5. Implement controlled log growth through log rotation.
6. Practice automated testing with pytest.
7. Practice professional Git and GitHub workflows.
8. Study the security implications of keylogging-related behavior.
9. Understand observable behaviors that defenders can use for detection.
10. Develop defensive security knowledge through controlled laboratory testing.

---

## Security Boundary

This project intentionally maintains a strict laboratory boundary.

### Current Implementation

The current implementation:

- Accepts test input through a controlled application interface.
- Creates validated `Event` objects.
- Processes events through a modular pipeline.
- Writes human-readable event logs.
- Writes structured JSON Lines event logs.
- Supports controlled log rotation.
- Provides automated tests for the application components.

### Event Model

Each event contains:

```text
timestamp
event_type
value
source
```

The `Event` model validates that the required textual fields are not empty.

### Human-Readable Logging

Events are formatted into a human-readable representation:

```text
[2026-08-18 00:09:15] [TEST] [test_source] TEST_EVENT
```

### Structured Logging

Events can also be represented as JSON Lines:

```json
{"timestamp": "2026-08-18T00:09:15", "event_type": "TEST", "value": "TEST_EVENT", "source": "test_source"}
```

Each JSONL line represents one event.

### Log Rotation

The application uses a configurable maximum log size.

When the configured limit is reached, the existing log can be rotated:

```text
events.log
    |
    v
events.log.1

new events.log
```

This helps prevent uncontrolled growth of the primary log file.

---

## Project Architecture

The application follows a modular event-processing architecture:

```text
Input Source
     |
     v
   Event
     |
     v
run_source()
     |
     v
process_event()
     |
     +----------------------+
     |                      |
     v                      v
Formatter              Serializer
     |                      |
     v                      v
events.log             events.jsonl
```

The same validated `Event` object is used to generate both logging formats.

---

## Project Structure

```text
Keylogger_security_lab/
|
+-- src/
|   +-- __init__.py
|   +-- config.py
|   +-- event.py
|   +-- formatter.py
|   +-- input_source.py
|   +-- keyboard_lab.py
|   +-- logger.py
|   +-- main.py
|   +-- serializer.py
|
+-- tests/
|   +-- test_config.py
|   +-- test_event.py
|   +-- test_formatter.py
|   +-- test_input_source.py
|   +-- test_keyboard_lab.py
|   +-- test_logger.py
|   +-- test_main.py
|   +-- test_serializer.py
|
+-- logs/
+-- .gitignore
+-- README.md
+-- requirements.txt
```

Generated logs and the Python virtual environment are excluded from version
control.

---

## Technologies

- Python 3.13
- pytest
- Tkinter
- Visual Studio Code
- Git
- GitHub
- Windows
- VirtualBox
- Kali Linux

---

## Setup

### 1. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 2. Activate the Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## Running the Application

Run the main controlled test application:

```powershell
python -m src.main
```

Expected output:

```text
Test event written successfully.
```

The application processes a controlled test event and writes it to the
configured logging destinations.

---

## Running the Keyboard Security Lab

Run:

```powershell
python -m src.keyboard_lab
```

The lab provides a controlled interface where test input can be entered
explicitly.

The entered test data is converted into an event and passed through the normal
event-processing pipeline.

Example:

```text
Input entered in lab
        |
        v
KEYBOARD_TEST event
        |
        v
process_event()
        |
        +------------------+
        |                  |
        v                  v
   events.log        events.jsonl
```

---

## Running Tests

Run the complete test suite:

```powershell
python -m pytest
```

The project uses automated tests to verify:

- Configuration
- Event validation
- Event serialization
- Formatting
- Input-source behavior
- Keyboard-lab behavior
- Logging
- Log rotation
- Logging error handling
- Application processing
- Structured logging

The project currently contains a comprehensive automated test suite.

---

## Configuration

The log directory can be changed using the environment variable:

```text
KEYLOGGER_LAB_LOG_DIR
```

Example:

```powershell
$env:KEYLOGGER_LAB_LOG_DIR="$PWD\custom_logs"
python -m src.main
```

If the environment variable is not configured, the default `logs/` directory
is used.

The application also supports a configurable maximum log size for log
rotation.

---

## Logging Output

The application can maintain two representations of events.

### Human-Readable Log

```text
logs/events.log
```

Example:

```text
[2026-08-18 13:57:30] [TEST] [test_source] TEST_EVENT
```

### Structured JSONL Log

```text
logs/events.jsonl
```

Example:

```json
{"timestamp": "2026-08-18T13:57:30.349388", "event_type": "TEST", "value": "TEST_EVENT", "source": "test_source"}
```

The structured format is useful for later programmatic analysis and security
event processing.

---

## Testing Philosophy

The project uses automated testing throughout development.

Tests are designed to verify individual components as well as integration
between components.

Temporary directories are used where appropriate so tests do not depend on
the project's real log files.

The test suite is run after significant changes to prevent regressions.

---

## Git Workflow

The project is maintained using Git and GitHub.

A typical development workflow is:

```powershell
git status
git add <files>
git diff --cached
git diff --cached --check
python -m pytest
git commit -m "message"
git push
git status
```

The working tree should be clean after a successful checkpoint.

---

## Security Perspective

The project is not intended to demonstrate offensive keylogger deployment.

Instead, it provides a controlled foundation for studying:

```text
Application Behavior
        |
        v
Security Observables
        |
        v
Detection Opportunities
        |
        v
Defensive Controls
```

The project can later be used as a foundation for authorized security analysis
in isolated laboratory environments.

---

## Limitations

The current project intentionally does not provide:

- System-wide keyboard surveillance
- Credential harvesting
- Browser credential capture
- Covert persistence
- Antivirus or EDR evasion
- Remote exfiltration
- Unauthorized monitoring

The current keyboard lab only processes input explicitly entered into the
controlled laboratory interface.

These boundaries are intentional and form part of the project's security
design.

---

## Future Security Analysis

Future work will focus on the defensive and VAPT perspective of
keylogging-related behavior.

Potential areas include:

- Security telemetry
- Process behavior analysis
- File and log artifacts
- Detection opportunities
- Endpoint security controls
- Monitoring strategies
- Incident investigation
- Defensive hardening

All future testing will remain limited to systems owned by the tester or
explicitly authorized laboratory environments.

---

## Author

**Gayathri**

Cybersecurity learner focused on developing practical skills in VAPT,
cybersecurity, and defensive security.
