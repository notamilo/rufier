# sits.py
from kivy.uix.label import Label
from kivy.clock import Clock


class Sits(Label):
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        text = f"Залишилось присідань {self.total}"
        super().__init__(text=text, color=(75 / 255, 0 / 255 ,130 / 255), **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        self.text = f"Залишилось присідань {remain}"
