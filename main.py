from window import Window
from line import Line

def main():
    # Create a window with a specified width and height
    window = Window(800, 600)

    # create 5 lines with different start and end points, colors and widths:
    lines = [
        Line((50, 50), (200, 50), fill_color="red", width=2),
        Line((100, 100), (300, 100), fill_color="green", width=4),
        Line((150, 150), (400, 150), fill_color="blue", width=6),
        Line((200, 200), (500, 200), fill_color="yellow", width=8),
        Line((250, 250), (600, 250), fill_color="purple", width=10),
    ]

    for line in lines:
        window.draw_line(line)
  
    # Start the event loop to keep the window open
    window.wait_for_close()

if __name__ == "__main__":
    main()


