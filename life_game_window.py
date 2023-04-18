import random
import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
import numpy as np

from figures.square import Square
from figures.grid import Grid


@dataclass
class LifeGameWindow:
    number_of_x_cells: int
    number_of_y_cells: int
    cell_width: int
    step_delay: int = 200  # in milliseconds
    grid: bool = True

    def __post_init__(self):
        self.width = self.number_of_x_cells * self.cell_width
        self.height = self.number_of_y_cells * self.cell_width

        self.cells = [[False for _ in range(self.number_of_y_cells)] for _ in range(self.number_of_x_cells)]
        self.session_key = ''

        self.root = tk.Tk()
        self.root.geometry(f'{self.width}x{self.height + 32}')
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height - 2, bg='white')
        self.canvas.grid()

        self.buttons_frame = tk.Frame(self.root)

        self.start_button = ttk.Button(self.buttons_frame, text='Start', width=self.width // 10, command=self.on_start)
        self.start_button.grid()

        self.buttons_frame.grid()

        self.canvas.cell_width = self.cell_width
        self.canvas.number_of_x_cells = self.number_of_x_cells
        self.canvas.number_of_y_cells = self.number_of_y_cells
        self.canvas.width = self.width
        self.canvas.height = self.height
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_click)
        self.draw_canvas()

    def on_start(self):
        self.session_key = LifeGameWindow.generate_key()
        self.root.after(self.step_delay, self.living_thread, self.session_key)

    def on_click(self, event):
        if 0 < event.x < self.width and 0 < event.y < self.height:
            x, y = self.translate_coord_to_cell_coord(event.x, event.y)
            cell_row, cell_column = self.get_cell_by_coordinates(x, y)
            self.cells[cell_row][cell_column] = True
            square = Square(x, y, self.cell_width)
            square.set_fill('black')
            square.draw(self.canvas)

    def living_thread(self, session_key):
        if session_key != self.session_key:
            return
        self.cells = self.get_next_generation(self.cells)
        self.draw_canvas()
        if True:
            self.root.after(self.step_delay, self.living_thread, session_key)

    def draw_canvas(self):
        self.canvas.delete('all')
        if self.grid:
            grid = Grid()
            grid.draw(self.canvas)
        print(self.cells)
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j]:
                    x, y = self.get_coordinates_by_cell(i, j)
                    square = Square(x, y, self.cell_width)
                    square.set_fill('black')
                    square.draw(self.canvas)

    def translate_coord_to_cell_coord(self, x, y):
        section_x = x // self.cell_width * self.cell_width + self.cell_width // 2
        section_y = y // self.cell_width * self.cell_width + self.cell_width // 2
        return section_x, section_y

    def get_coordinates_by_cell(self, cell_row, cell_column):
        x = cell_row * self.cell_width + self.cell_width / 2
        y = cell_column * self.cell_width + self.cell_width / 2
        return x, y

    def get_cell_by_coordinates(self, x, y):
        cell_row = int((x - self.cell_width / 2) / self.cell_width)
        cell_column = int((y - self.cell_width / 2) / self.cell_width)
        return cell_row, cell_column

    def count_live_neighbors(self, grid, row, col):
        rows, cols = grid.shape
        slices = (slice(max(row - 1, 0), min(row + 2, rows)), slice(max(col - 1, 0), min(col + 2, cols)))
        return np.sum(grid[slices]) - grid[row, col]

    def get_next_generation(self, grid):
        grid = np.array(grid)
        new_grid = np.zeros_like(grid)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                live_neighbors = np.sum(grid[max(0, i - 1):i + 2, max(0, j - 1):j + 2]) - grid[i, j]
                if grid[i, j] and (live_neighbors == 2 or live_neighbors == 3):
                    new_grid[i, j] = 1
                elif not grid[i, j] and live_neighbors == 3:
                    new_grid[i, j] = 1
        return new_grid.tolist()

    @staticmethod
    def generate_key():
        return ''.join([random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for _ in range(7)])

    def run(self):
        self.root.mainloop()
