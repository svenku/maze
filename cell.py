from line import Line
from point import Point

class Cell:

    def __init__(self, top_left: Point, bottom_right: Point, has_left_wall=True, has_top_wall=True, has_right_wall=True, has_bottom_wall=True, window=None):

        self.top_left = top_left
        self.bottom_right = bottom_right
        
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.window = window

    def draw(self):
        x1, y1 = self.top_left.get_x(), self.top_left.get_y()
        x2, y2 = self.bottom_right.get_x(), self.bottom_right.get_y() 


        if self.has_left_wall:
            self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_top_wall:
            self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_right_wall:
            self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_bottom_wall:
            self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def get_center(self):
        x1, y1 = self.top_left.get_x(), self.top_left.get_y()
        x2, y2 = self.bottom_right.get_x(), self.bottom_right.get_y()
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        return Point(center_x, center_y)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            move_color = "gray"
        else:
            move_color = "red"
        self.window.draw_line(Line(self.get_center(), to_cell.get_center(), fill_color=move_color, width=2))

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"