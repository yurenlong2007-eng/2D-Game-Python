import tkinter as tk
import graphic, handler

g = graphic.Graphic()


class Player():
    def __init__(self, window_p_width, window_p_height, window_sf, canvas: tk.Canvas):
        self.world_x = 0
        self.world_y = 0
        self.max_speed = 10

        self.screen_x = int(window_p_width/2)
        self.screen_y = int(window_p_height/2)

        self.sprite_image = g.enlarge(file_path="res/nfm_left_001.png", sf=window_sf)
        self.sprite = canvas.create_image(self.screen_x, self.screen_y, image=self.sprite_image)

    def update(self, kh: handler.KeyHandler):
        x = int(kh.key_pressed("a")) - int(kh.key_pressed("d"))
        y = int(kh.key_pressed("w")) - int(kh.key_pressed("s"))
        if x and y:
            x *= 0.7071
            y *= 0.7071
        self.world_x += int(x * self.max_speed)
        self.world_y += int(y * self.max_speed)

    def draw(self, canvas: tk.Canvas):
        canvas.tag_raise(self.sprite)