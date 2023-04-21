import json
import os
import random
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
from dataclasses import dataclass
import numpy as np
from PIL import Image

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

        self.cells = []
        self.live_cells = 0
        self.generation = 0
        self.kill_cells()
        self.session_key = ''
        self.pause = True

        self.root = tk.Tk()
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height - 2, bg='white')
        self.canvas.grid()

        self.control_buttons_frame = tk.Frame(self.root)

        self.step_button = ttk.Button(self.control_buttons_frame, text='Step', width=self.width // 50,
                                      command=self.on_step)
        self.step_button.grid(column=2, row=0)

        self.start_pause_button = ttk.Button(self.control_buttons_frame, text='Start', width=self.width // 30,
                                             command=self.on_start_pause)
        self.start_pause_button.grid(column=3, row=0)

        self.clear_button = ttk.Button(self.control_buttons_frame, text='Clear', width=self.width // 50,
                                       command=self.on_clear)
        self.clear_button.grid(column=4, row=0)

        self.mode = tk.StringVar()
        self.paint_mode_combo_box = ttk.Combobox(self.control_buttons_frame, values=['Add', 'Kill'],
                                                 width=self.width // 60,
                                                 state='readonly', textvariable=self.mode)
        self.paint_mode_combo_box.set('Add')
        self.paint_mode_combo_box.grid(column=5, row=0)

        self.control_buttons_frame.grid()

        self.other_buttons_frame = tk.Frame(self.root)

        self.save_button = ttk.Button(self.other_buttons_frame, text='Save', width=self.width // 60,
                                      command=self.on_save)
        self.save_button.grid(column=0, row=0)

        self.load_button = ttk.Button(self.other_buttons_frame, text='Load', width=self.width // 60,
                                      command=self.on_load)
        self.load_button.grid(column=1, row=0, padx=(0, self.width // 27))

        self.load_image_button = ttk.Button(self.other_buttons_frame, text='Load Image', width=self.width // 45,
                                      command=self.on_load_image)
        self.load_image_button.grid(column=2, row=0)

        self.other_buttons_frame.grid()

        self.build_canvas(self.number_of_x_cells, self.number_of_y_cells, self.cell_width)
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_click)
        self.draw_canvas()
        self.root.after(self.step_delay, self.living_thread)

    def on_start_pause(self):
        self.pause = False if self.pause else True
        if not self.pause:
            self.start_pause_button.config(text='Pause')
        else:
            self.start_pause_button.config(text='Start')

    def on_clear(self):
        self.kill_cells()
        self.generation = 0
        self.draw_canvas()

    def on_step(self):
        self.make_step()

    def on_save(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.json', initialdir='.')
        try:
            with open(file_path, 'w') as f:
                json.dump({'config': {'number_of_x_cells': self.number_of_x_cells,
                                      'number_of_y_cells': self.number_of_y_cells,
                                      'cell_width': self.cell_width},
                           'cells': self.cells}, f)
        except FileNotFoundError:
            pass

    def on_load(self):
        file_path = filedialog.askopenfilename(filetypes=[('JSON files', '*.json')], initialdir='.')
        try:
            with open(file_path, 'r') as f:
                json_str = f.read()
                json_data = json.loads(json_str)
            self.build_canvas(json_data['config']['number_of_x_cells'],
                              json_data['config']['number_of_y_cells'],
                              json_data['config']['cell_width'])
            self.cells = json_data['cells']
            self.draw_canvas()
            self.generation = 0
        except FileNotFoundError:
            pass

    def on_load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', ('*.jpg', '*.png'))], initialdir='.')
        if not os.path.exists(file_path):
            return
        try:
            img = Image.open(file_path)
            img = img.resize(self.transform_image_size(img.size[0], img.size[1], 150))
            img_width, img_height = img.size
            img = img.convert("1")
            self.cells = []
            for y in range(img_width):
                row = []
                for x in range(img_height):
                    pixel = img.getpixel((y, x))
                    row.append(False if pixel == 255 else True)
                self.cells.append(row)
            self.build_canvas(img_width, img_height, 4)
            self.draw_canvas()
            self.generation = 0
        except FileNotFoundError:
            pass

    def on_click(self, event):
        if 0 < event.x < self.width and 0 < event.y < self.height:
            x, y = self.translate_coord_to_cell_coord(event.x, event.y)
            cell_row, cell_column = self.get_cell_by_coordinates(x, y)
            self.cells[cell_row][cell_column] = True if self.mode.get() == 'Add' else False
            square = Square(x, y, self.cell_width)
            square.set_fill('black')
            square.draw(self.canvas)
        self.draw_canvas()

    def living_thread(self):
        if not self.pause:
            self.make_step()
        if True:
            self.root.after(self.step_delay, self.living_thread)

    def draw_canvas(self):
        self.canvas.delete('all')
        if self.grid:
            grid = Grid()
            grid.draw(self.canvas, 'lightgrey')
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j]:
                    x, y = self.get_coordinates_by_cell(i, j)
                    square = Square(x, y, self.cell_width)
                    square.set_fill('black')
                    square.draw(self.canvas)
        self.count_live_cells()
        self.canvas.create_text(5, 15,
                                text=f'Gen: {self.generation}\n'
                                     f'Cells: {self.live_cells}',
                                fill='green', anchor='w', font=('TkDefaultFont', 8))

    def translate_coord_to_cell_coord(self, x, y):
        section_x = x / self.cell_width * self.cell_width + self.cell_width / 2
        section_y = y / self.cell_width * self.cell_width + self.cell_width / 2
        return section_x, section_y

    def get_coordinates_by_cell(self, cell_row, cell_column):
        x = cell_row * self.cell_width + self.cell_width / 2
        y = cell_column * self.cell_width + self.cell_width / 2
        return x, y

    def get_cell_by_coordinates(self, x, y):
        cell_row = int((x - self.cell_width / 2) / self.cell_width)
        cell_column = int((y - self.cell_width / 2) / self.cell_width)
        return cell_row, cell_column

    def kill_cells(self):
        self.cells = [[False for _ in range(self.number_of_y_cells)] for _ in range(self.number_of_x_cells)]

    def build_canvas(self, number_of_x_cells, number_of_y_cells, cell_width):
        self.number_of_x_cells = number_of_x_cells
        self.number_of_y_cells = number_of_y_cells
        self.cell_width = cell_width
        self.width = self.number_of_x_cells * self.cell_width
        self.height = self.number_of_y_cells * self.cell_width
        self.canvas.config(width=self.width, height=self.height - 2)
        self.root.config(width=self.width, height=self.height + 57)
        self.canvas.cell_width = self.cell_width
        self.canvas.number_of_x_cells = self.number_of_x_cells
        self.canvas.number_of_y_cells = self.number_of_y_cells
        self.canvas.width = self.width
        self.canvas.height = self.height

    def make_step(self):
        self.generation += 1
        self.cells = self.get_next_generation(self.cells)
        self.draw_canvas()

    @staticmethod
    def show_error(text):
        messagebox.showerror(message=text)

    def count_live_cells(self):
        self.live_cells = 0
        for row in self.cells:
            for cell in row:
                if cell:
                    self.live_cells += 1

    @staticmethod
    def count_live_neighbors(grid, row, col):
        rows, cols = grid.shape
        slices = (slice(max(row - 1, 0), min(row + 2, rows)), slice(max(col - 1, 0), min(col + 2, cols)))
        return np.sum(grid[slices]) - grid[row, col]

    @staticmethod
    def get_next_generation(grid):
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
    def transform_image_size(width, height, new_size):
        if width > height:
            new_width = new_size
            new_height = int(height * (new_size / width))
        else:
            new_height = new_size
            new_width = int(width * (new_size / height))
        return new_width, new_height

    def run(self):
        self.root.mainloop()
