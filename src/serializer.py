import json

from src.event import Event


def serialize_event(event: Event) -> str:
    return json.dumps(
        event.to_dict(),
        ensure_ascii=False
    )
