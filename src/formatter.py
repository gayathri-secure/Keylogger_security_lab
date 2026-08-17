def format_event(event):
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] [{event.event_type}] {event.value}"

