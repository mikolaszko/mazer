from pyray import *
def main():
    init_window(300, 300, "Mazer")
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello World", 190, 200, 20, VIOLET)
        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
