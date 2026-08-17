from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    timestamp: datetime
    event_type: str
    value: str
