from window import Window
from line import Line
from cell import Cell
from point import Point

def main():
    # Create a window with a specified width and height
    window = Window(800, 600)

    # create 5 lines with different start and end points, colors and widths:
    lines = [
        Line(Point(50, 50), Point(200, 50), fill_color="red", width=2),
        Line(Point(100, 100), Point(300, 100), fill_color="green", width=4),
        Line(Point(150, 150), Point(400, 150), fill_color="blue", width=6),
        Line(Point(200, 200), Point(500, 200), fill_color="yellow", width=8),
        Line(Point(250, 250), Point(600, 250), fill_color="purple", width=10),
    ]

    for line in lines:
        window.draw_line(line)
    
    # Create 5 cells with different positions, sizes, and colors
    cells = [
        Cell(Point(10, 10), Point(100, 100), has_left_wall=True, has_top_wall=True, has_right_wall=True, has_bottom_wall=True, window=window),
        Cell(Point(100, 200), Point(200, 300), has_left_wall=False, has_top_wall=True, has_right_wall=True, has_bottom_wall=False, window=window),
        Cell(Point(200, 100), Point(300, 200), has_left_wall=True, has_top_wall=False, has_right_wall=False, has_bottom_wall=True, window=window),
        Cell(Point(300, 200), Point(400, 300), has_left_wall=True, has_top_wall=True, has_right_wall=False, has_bottom_wall=False, window=window),
        Cell(Point(400, 100), Point(500, 200), has_left_wall=False, has_top_wall=False, has_right_wall=True, has_bottom_wall=True, window=window),

    ]

    for cell in cells:
        cell.draw()







    # Start the event loop to keep the window open
    window.wait_for_close()

if __name__ == "__main__":
    main()


