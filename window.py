from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width=800, height=600):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.__running = False

        # Bind the close method to the window's close button
        self.__root.protocol("WM_DELETE_WINDOW", self.close)        

    def draw_line(self, line):
        if isinstance(line, Line):
            line.draw(self.canvas)
        else:
            raise TypeError("Expected a Line object")

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
            
    def close(self):
        self.__running = False
        self.__root.destroy() 

