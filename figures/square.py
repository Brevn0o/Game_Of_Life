from .rectangle import *


class Square(Rectangle):

    def __init__(self, x, y, width):
        super().__init__(x, y, width, width)
