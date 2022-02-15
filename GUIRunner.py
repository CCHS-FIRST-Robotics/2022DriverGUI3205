#!usr/bin/Python
# GUIRunner.py

'''Makes and dispays GUI for robot field visualization'''

__author__ = "Brian Tilford"
__version__ = "0.1"


import tkinter
from tkinter.font import Font
import GUI


def main():
    robot_visual = GUI.Window("Field Map Cisualization")
    robot_visual.start_interface()


main()
