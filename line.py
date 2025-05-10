from point import Point

class Line:
    def __init__(self, start: Point, end: Point, fill_color="black", width=2):
        self.start = start
        self.end = end
        self.fill_color = fill_color
        self.width = width

    def draw(self, canvas):
        canvas.create_line(self.start.get_x(), self.start.get_y(), \
                           self.end.get_x(), self.end.get_y(), \
                           fill=self.fill_color, width=self.width)