import tkinter as tk
import player, map, handler, time

p: player.Player
m: map.Map
kh: handler.KeyHandler

window_b_width: int = 6
window_b_height: int = 6
block_size: int = 32
window_sf: int = 4
window_p_width = int(window_b_width * block_size * window_sf)
window_p_height = int(window_b_height * block_size * window_sf)

def main():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("My 2D Life")

    canvas = tk.Canvas(master=root, width=window_p_width, height=window_p_height, background="Black", highlightthickness=0)
    canvas.pack()

    init(canvas)

    root.bind("<KeyPress>", kh.on_key_press)
    root.bind("<KeyRelease>", kh.on_key_release)
    
    update(root, canvas)
    root.mainloop()

def init(canvas: tk.Canvas):
    global p,m,kh
    p = player.Player(window_p_width, window_p_height, window_sf, canvas)
    m = map.Map(window_b_width, window_b_height, block_size, window_sf, canvas)
    kh = handler.KeyHandler()

def update(root: tk.Tk, canvas: tk.Canvas):
    start = time.perf_counter()

    m.update(canvas, p.world_x - int(window_p_width/2), p.world_y - int(window_p_height/2))
    #m.draw(canvas)
    p.update(kh)
    p.draw(canvas)

    elapsed_ms = (time.perf_counter() - start) * 1000

    # print(f"{elapsed_ms:.2f} ms") # DEBUG

    delay = max(1, int(1000 / 60 - elapsed_ms))
    root.after(delay, update, root, canvas)

main()