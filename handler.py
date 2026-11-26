

class KeyHandler:
    def __init__(self):
        self.pressed = set()

    def on_key_press(self, event):
        self.pressed.add(event.keysym)

    def on_key_release(self, event):
        self.pressed.discard(event.keysym)

    def key_pressed(self, key: str)-> bool:
        if key in self.pressed: return True
        else: return False
