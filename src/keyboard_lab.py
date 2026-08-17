import tkinter as tk
from datetime import datetime

from src.event import Event
from src.main import process_event


def process_test_input(value):
    if not value.strip():
        return False

    event = Event(
        timestamp=datetime.now(),
        event_type="KEYBOARD_TEST",
        value=value,
        source="keyboard_lab"
    )

    process_event(event)
    return True


class KeyboardLab:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keyboard Security Lab")
        self.root.geometry("500x250")

        self.label = tk.Label(
            self.root,
            text="Enter test text below:"
        )
        self.label.pack(pady=20)

        self.entry = tk.Entry(
            self.root,
            width=50
        )
        self.entry.pack()

        self.button = tk.Button(
            self.root,
            text="Process Test Input",
            command=self.process_input
        )
        self.button.pack(pady=20)

        self.entry.focus_set()

    def process_input(self):
        value = self.entry.get()

        if process_test_input(value):
            self.entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    lab = KeyboardLab()
    lab.run()
