from dataclasses import dataclass
from game_of_life_window import GameOfLifeWindow


@dataclass
class GameOfLife:
    number_of_x_cells: int = 30
    number_of_y_cells: int = 30
    cell_width: int = 15
    step_delay: int = 100
    grid: bool = True
    aiming: bool = True

    def run(self):
        win = GameOfLifeWindow(self.number_of_x_cells,
                               self.number_of_y_cells,
                               self.cell_width,
                               self.step_delay,
                               self.grid,
                               self.aiming)
        win.run()


lg = GameOfLife(60, 60, 10, 100, True, True)
lg.run()
