from pynput.mouse import Controller
from pynput.mouse import Listener

import time
import tkinter as tk

import numpy as np

root = tk.Tk()
mouse = Controller()

# stop movement by clicking
stop_movement = False

def on_click(x, y, button, pressed):
    """to stop the movement"""
    global stop_movement
    if pressed:
        stop_movement = True
        return False


listener = Listener(on_click=on_click)
listener.start()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x, center_y = screen_width // 2, screen_height // 2
scale = 100

# butterfly function 
t_values = np.linspace(0, 12 * np.pi, 5000)
points = []
for t in t_values:
    r = np.exp(np.cos(t)) - 2 * np.cos(4 * t) + (np.sin(5 * t / 112)) ** 5
    x = r * np.sin(t) * scale + center_x
    y = r * np.cos(t) * scale + center_y
    points.append((x, y))


# movement 
while not stop_movement:
    for point_x, point_y in points:
        if stop_movement:
            break
        mouse.position = (int(point_x), int(point_y))
        time.sleep(0.02)

listener.stop()
