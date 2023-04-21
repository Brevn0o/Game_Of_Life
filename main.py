import tkinter
from game_of_life_window import *


class LifeGame:

    def __init__(self):
        self.number_of_x_cells = 70
        self.number_of_y_cells = 70
        self.cell_width = 8

    def run(self):
        win = LifeGameWindow(self.number_of_x_cells,
                             self.number_of_y_cells,
                             self.cell_width,
                             100,
                             True)
        win.run()



lg = LifeGame()
lg.run()
