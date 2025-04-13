from window import Window

def main():
    # Create a window with a specified width and height
    window = Window(800, 600)
    
    # Start the event loop to keep the window open
    window.wait_for_close()

if __name__ == "__main__":
    main()


