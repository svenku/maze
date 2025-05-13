from window import Window
from line import Line
from maze import Maze
from cell import Cell
from point import Point

def main():
    # Create a window with a specified width and height
    window = Window(800, 600)

    # Create a maze with a specified cell size
    cell_size = 50
    maze = Maze(cell_size, window)
    maze.setup()
    maze.make_entrance_and_exit()

    # Start the event loop to keep the window open
    window.wait_for_close()

if __name__ == "__main__":
    main()


