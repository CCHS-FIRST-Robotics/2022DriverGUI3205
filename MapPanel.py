import tkinter as tk
from tkinter.font import Font
import frc.robot.network as netwk
import math

mouse_enabled = False
COORD_SCALE = 3 # in cm
PIXEL_SCALE = 1.176 # cm
starting_pos = [0, 0]

class Window:
    def __init__(self, root):
        self.map_box = tk.Canvas(root, width=1400, height=700, bg='black')
        field_map = tk.PhotoImage(file='Field Map.gif')
        self.map_box.create_image(0, 0, image=field_map, anchor="nw")
        self.old_heading = 0
        starting_pos = [0, 0]
        self.map_box.bind('<Button-1>', self.map_clicked)

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
        self.map_box.update_idletasks()()
        self.map_box.update()

    def update_robo_start(self, start_pos):
        starting_pos = start_pos

    def restart(self, start_pos):
        self.update_robo_start(start_pos)
        # reset network table and robot Coordinates
        # reset hardware, off on, and clear value slate

    def map_clicked(self, event):
        if mouse_enabled:
            mouse_x = event.x
            mouse_y = event.y
            new_x = ((starting_pos[0] - mouse_x) * PIXEL_SCALE) / COORD_SCALE
            new_y = (-(starting_pos[1] - mouse_y) * PIXEL_SCALE) / COORD_SCALE
            #send coords 



def create_rectangle_points(robo_x, robo_y, heading):
    x_pos = starting_pos[0] + robo_x
    y_pos = starting_pos[1] + robo_y
    ROBO_SMALL_SIDE = 30 # SEE MATH PAGE IN NOTEBOOK, NUMBERS ARE IN PIXELS, /2 of total length
    ROBO_LARGE_SIDE = 35
    angles = []
    points = []
    radius = math.sqrt(ROBO_LARGE_SIDE^2 + ROBO_SMALL_SIDE^2)
    major_angle = math.atan(ROBO_SMALL_SIDE/ROBO_LARGE_SIDE)
    minor_angle = math.atan(ROBO_LARGE_SIDE/ROBO_SMALL_SIDE)
    angles.append((heading + major_angle) % (math.pi * 2))
    angles.append((heading + major_angle + 2 * minor_angle) % (math.pi * 2))
    angles.append((heading + 3 * major_angle + 2 * minor_angle) % (math.pi * 2))
    angles.append((heading + 3 * major_angle + 4 * minor_angle) % (math.pi * 2))
    for angle in angles:
        y_add = math.sin(angle) * radius
        x_add = math.cos(angle) * radius
        point_ycor = (y_pos * COORD_SCALE) / PIXEL_SCALE - y_add
        point_xcor = (x_pos * COORD_SCALE) / PIXEL_SCALE + x_add
        points.extend([point_xcor, point_ycor])

    return points


        # 1400x700, center is 700x350
        # field 1646x823cm, every pixel on screen is 1.176 cms
