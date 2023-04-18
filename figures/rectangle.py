from .figure import *


class Rectangle(Figure):

    def __init__(self, x, y, width, height):
        super().__init__((x, y))
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.create_rectangle(self.x - self.width // 2,
                                self.y - self.height // 2,
                                self.x + self.width // 2,
                                self.y + self.height // 2,
                                self.options)
