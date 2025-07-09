# TypeWriterEffectControl.py
import flet as ft
import threading
import time

class TypeWriterControl(ft.Text):
    def __init__(self, value="", font_family=None, color=None, transparency=True):
        super().__init__(
            value="",  # Start with empty text
            font_family=font_family,
            color=color,
            size=14,
        )
        self.text_to_print = value
        self.transparency = transparency

    def start_typing(self):
        def type_effect():
            typed = ""
            for char in self.text_to_print:
                typed += char
                self.value = typed
                self.update()
                time.sleep(0.03)
        threading.Thread(target=type_effect).start()