class Figure:
    def __init__(self, center):
        self.x = center[0]
        self.y = center[1]
        self.options = {'fill': 'yellow'}

    def set_fill(self, fill):
        self.options['fill'] = fill