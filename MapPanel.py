import tkinter as tk
from tkinter.font import Font
import frc.robot.network as netwk
import math


class Window:
    def __init__(self, root):
        self.map_box = tk.Canvas(root, width=1400, height=700, bg='black')
        field_map = tk.PhotoImage(file='Field Map.gif')
        self.map_box.create_image(0, 0, image=field_map, anchor="nw")
        self.old_heading = 0
        self.starting_pos = [0, 0]

    def update_robo_pos(self, netwk):
        self.map_box.delete("all")
        self.robo_pos = netwk.getPosVal()
        self.robo_pos[0] = self.starting_pos + self.robo_pos[0]
        self.robo_pos[1] = self.starting_pos - self.robo_pos[1]
        self.robo_heading = netwk.getHeadingVal()
        field_map = tk.PhotoImage(file='Field Map.gif')
        self.map_panel.map_box.create_image(0, 0, image=field_map, anchor="nw")
        self.rec_points = create_rectangle_points(self.robo_pos[0], self.robo_pos[1], self.robo_heading)
        self.map_box.create_polygon(self.rec_points, fill="grey", outline="black")

    def update_robo_start(self, start_pos):
        self.starting_pos = start_pos

    def restart(self, start_pos):
        self.update_robo_start(start_pos)
        # reset network table and robot Coordinates
        # reset hardware, off on, and clear value slate

def create_rectangle_points(x_pos, y_pos, heading):
    angles = []
    points = []
    radius = math.sqrt(70^2 + 60^2) # SEE MATH PAGE IN NOTEBOOK, NUMBERS ARE IN PIXELS, MAKE VARIABLE NAMES
    major_angle = math.atan(21/25)
    minor_angle = math.atan(25/21)
    angles.append((heading + major_angle) % (math.pi * 2))
    angles.append((heading + major_angle + 2 * minor_angle) % (math.pi * 2))
    angles.append((heading + 3 * major_angle + 2 * minor_angle) % (math.pi * 2))
    angles.append((heading + 3 * major_angle + 4 * minor_angle) % (math.pi * 2))
    for angle in angles:
        y_add = math.sin(angle) * radius
        x_add = math.cos(angle) * radius
        point_ycor = y_pos - y_add
        point_xcor = x_pos + x_add
        points.extend([point_xcor, point_ycor])

    return points


        # 1400x700, center is 700x350
        # field 1646x823cm, every pixel on screen is 1.176 cms
