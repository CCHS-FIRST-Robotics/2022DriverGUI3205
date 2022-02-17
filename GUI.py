#!usr/bin/Python
# menu_runner.py
# -*- coding: utf-8 -*-

'''Makes and dispays basic menu to allow user to quit or run game
may provide added funcitonality later'''

__author__ = "Brian Tilford"
__version__ = "0.1"


import tkinter as tk
import threading as th
from tkinter.font import Font
import InfoPanel
import MapPanel
import ButtonPanel
import PyNetInformation


timer_running = True
program_started = False

class Window:
    def __init__(self, name):
        self.display = tk.Tk(name)
        self.display.title(name)
        self.display.option_add('*Font', '27')
        self.display.resizable(0, 0)
        self.network_table = PyNetInformation.NetTable()
        self.button_panel = ButtonPanel.Window(self.display)
        self.info_panel = InfoPanel.Window(self.display)
        self.map_panel = MapPanel.Window(self.display)
        self.button_panel.button_box.grid(row=1, column=0, columnspan=6)
        self.map_panel.map_box.grid(row=1, column=0, rowspan=3, columnspan=6)
        self.info_panel.text_box.grid(row=4, column=0, columnspan=6)

    def start_interface(self):
        self.initialize_update_timer()

    def update_interface(self):
        self.display.update_idletasks()
        self.display.update()

    def initialize_update_timer(self):
        update_timer = th.Timer(0.001, self.update_info)
        update_timer.start()

    def update_graphics(self):
        if program_started:
            self.map_panel.update_robo_pos(self.network_table)
            self.info_panel.update_robo_info(self.network_table)
            self.update_interface()
        if timer_running:
            self.initialize_update_timer()
