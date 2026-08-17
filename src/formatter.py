def format_event(event):
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"[{timestamp}] "
        f"[{event.event_type}] "
        f"[{event.source}] "
        f"{event.value}"
    )
