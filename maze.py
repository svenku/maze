from cell import Cell
from point import Point
from time import sleep


class Maze:
    def __init__(self, cell_size, window):

        self.cell_size = cell_size
        self.window = window
        self.num_rows = int((600 - 20) / self.cell_size)
        self.num_cols = int((800 - 20) / self.cell_size)

    def setup(self):
        self.cells = []

        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):
                top_left = Point(col * self.cell_size + 10, row * self.cell_size + 10)
                bottom_right = Point((col + 1) * self.cell_size + 10, (row + 1) * self.cell_size +10)
                cell = Cell(top_left, bottom_right, window=self.window)
                row_cells.append(cell)
                # Draw the cell on the window
                cell.draw()
                self.animate()
            self.cells.append(row_cells)
    
    def animate(self):
        self.window.redraw()
        sleep(0.005)
        

    
        



