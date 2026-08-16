from datetime import datetime


def format_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {event}"
