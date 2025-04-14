from point import Point

class Line:
    def __init__(self, start, end, fill_color="black", width=2):
        self.__start = Point(start[0], start[1])
        self.__end = Point(end[0], end[1])
        self.fill_color = fill_color
        self.width = width

    def draw(self, canvas):
        canvas.create_line(self.__start.x, self.__start.y, \
                           self.__end.x, self.__end.y, \
                           fill=self.fill_color, width=self.width)