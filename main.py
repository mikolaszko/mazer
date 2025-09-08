from pyray import *

CELL_VISITED = 0x10

# would like to make this a user input
CELLS_WIDTH, CELLS_HEIGHT = 60, 30


SQUARE_WIDTH, SQUARE_HEIGHT = 10, 10


PATH_WIDTH = 3
def main():
    stack = [] # pair (x, y)
    visited = [0] * CELLS_WIDTH *  CELLS_HEIGHT
    visited_cnt = 0 
    stack.append((0,0))
    visited[0] = CELL_VISITED
    
    visited_cnt += 1
    print(stack, visited)
    
    init_window(500, 500, "Mazer")
    while not window_should_close():
        for x in range(CELLS_WIDTH):
            for y in range(CELLS_HEIGHT):
                if visited[x + (y * CELLS_HEIGHT)] == 0x10:
                    draw_rectangle(x * (PATH_WIDTH + 1 + SQUARE_WIDTH), y * (PATH_WIDTH + 1 + SQUARE_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, WHITE)
                else:
                    draw_rectangle(x * (PATH_WIDTH + 1 + SQUARE_WIDTH), y * (PATH_WIDTH + 1 + SQUARE_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, GREEN)
        begin_drawing()
        clear_background(BLACK)
        end_drawing()
    close_window()


if __name__ == "__main__":
    main()
