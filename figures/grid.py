import tkinter as tk


class Grid:

    def __init__(self):
        pass

    def draw(self, canvas):
        for i in range(0, canvas.number_of_x_cells):
            self.draw_horisontal_line(canvas, (i + 1) * canvas.cell_width)
        for i in range(0, canvas.number_of_y_cells):
            self.draw_vertical_line(canvas, (i + 1) * canvas.cell_width)

    def draw_horisontal_line(self, canvas, y):
        canvas.create_line(0, y, canvas.width, y)

    def draw_vertical_line(self, canvas, x):
        canvas.create_line(x, 0, x, canvas.height)
