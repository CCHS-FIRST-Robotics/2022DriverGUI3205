from tkinter import *
import tkinter as tk
from tkinter.font import Font


class Window:
    def __init__(self, root):
        self.content = StringVar()
        self.text_box = tk.Label(root, bg="black", fg="white", font="Courier", height=10, width=150, padx=0, pady=0, textvariable=self.content)
        self.robo_pos = [0, 0]

    def update_robo_info(self, netwk):
        self.robo_pos = netwk.getPosVal()
        self.robo_heading = netwk.getHeadingVal()
        self.content = f"X Coordinates: {robo_pos[0]}, Y Coordinates: {robo_pos[1]}, Heading: {robo_heading}"
