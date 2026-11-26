import tkinter as tk
from PIL import Image,ImageTk

class Map:
    def __init__(self, window_b_width, window_b_height, block_size, sf, canvas: tk.Canvas):
        #self.frame_width = int(window_b_width * block_size)
        #self.frame_height = int(window_b_height * block_size)
        self.sf = sf
        self.camera_x: int = 0
        self.camera_y: int = 0
        #self.x1: int = self.x0 + self.frame_width
        #self.y1: int = self.y0 + self.frame_height
        #self.frame = (self.x0, self.y0, self.x1, self.y1)
        map_file = Image.open("res/murano.png")
        image_width, image_height = map_file.size
        scaled_map = map_file.resize((int(image_width * self.sf), int(image_height * self.sf)), Image.Resampling.NEAREST)
        self.map_image = ImageTk.PhotoImage(scaled_map)
        self.map = canvas.create_image(0,0,anchor="nw", image = self.map_image)

    def update(self, canvas: tk.Canvas, x, y):
        self.camera_x = x
        self.camera_y = y

        canvas.coords(self.map, x, y)
        #self.x1 = self.x0 + self.frame_width
        #self.y1 = self.y0 + self.frame_height
        #self.frame = (self.x0, self.y0, self.x1, self.y1)
