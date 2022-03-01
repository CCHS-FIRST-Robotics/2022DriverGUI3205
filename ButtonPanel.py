from tkinter import *
import tkinter as tk
from tkinter.font import Font
import GUI
import MapPanel


class Window:
    def __init__(self, root):
        self.button_box = tk.Frame(root)
        # May not need tk. for Menubutton and directions
        #self.start_dropdown = tk.Menubutton(self.button_box, anchor="w", text="Start Pos", relief=tk.RAISED)
        #self.start_pos1 = IntVar()
        #self.start_pos2 = IntVar()
        #self.start_pos3 = IntVar()
        #self.start_pos4 = IntVar()
        #self.start_dropdown.menu.add_checkbutton(label="Pos 1", variable=start_pos1)
        #self.start_dropdown.menu.add_checkbutton(label="Pos 2", variable=start_pos2)
        #self.start_dropdown.menu.add_checkbutton(label="Pos 3", variable=start_pos3)
        #self.start_dropdown.menu.add_checkbutton(label="Pos 4", variable=start_pos4)

        self.reset_button = tk.Button(self.button_box, text="Reset", command=self.reset_program)
        self.reset_button.pack(side=tk.RIGHT)

        self.mouse_button = tk.Button(self.button_box, text="Command Mode", command=self.enable_mouse_input)
        self.mouse_button.pack(side=tk.RIGHT)

        self.start_button = tk.Button(self.button_box, text="Start", command=self.start_program)
        self.start_button.pack(side=tk.RIGHT)


    def start_program(self):
        if not GUI.program_started:
            import GUIRunner
            GUI.program_started = True
            GUIRunner.robot_visual.start_interface()

    def reset_program(self):
        # add are you sure box
        if GUI.program_started:
            GUI.program_started = False
            # Wipe Network data, set current pos to selected pos

    def enable_mouse_input(self):
        if not MapPanel.mouse_enabled:
            MapPanel.mouse_enabled = True
        else:
            MapPanel.mouse_enabled = False
