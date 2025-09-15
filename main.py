import random
from typing import Callable
from pyray import *

CELL_PATH_N = 0x01
CELL_PATH_E = 0x02
CELL_PATH_S = 0x04
CELL_PATH_W = 0x08
CELL_VISITED = 0x10

# would like to make this a user input
MAZE_WIDTH, MAZE_HEIGHT = 60, 30


SQUARE_WIDTH, SQUARE_HEIGHT = 10, 10


PATH_WIDTH = 3
def main():
    # temporary representation 
    stack: list[tuple[int, int]] = [] # pair (x, y)
    # actual maze
    visited = [0] * MAZE_WIDTH *  MAZE_HEIGHT
    visited_cnt = 0 
    stack.append((0,0))
    visited[0] = CELL_VISITED
    
    visited_cnt += 1 
    init_window(500, 500, "Mazer")
    offset: Callable[[int, int], int] = lambda x, y: ((stack[-1][1] + y) * MAZE_WIDTH + stack[-1][0] + x)

    while not window_should_close():
        # this rocks
        if visited_cnt < MAZE_WIDTH * MAZE_HEIGHT:
            neighbours: list[int] = []

            # north neighbour
            if (stack[-1][1] > 0 and (visited[offset(0, -1)] & CELL_VISITED) == 0):
                neighbours.append(0)
            # east neighbour
            if (stack[-1][0] < MAZE_WIDTH - 1 and (visited[offset(1, 0)] & CELL_VISITED) == 0):
                neighbours.append(1)
            # south neighbour
            if (stack[-1][1] < MAZE_HEIGHT - 1 and (visited[offset(0, 1)] & CELL_VISITED) == 0):
                neighbours.append(2)
            # west neightbour
            if (stack[-1][0] > 0 and (visited[offset(-1, 0)] & CELL_VISITED) == 0):
                neighbours.append(3)

            if neighbours:
                next_cell_dir = random.choice(neighbours)

                match(next_cell_dir):
                    case 0:
                        visited[offset(0, -1)] |= CELL_VISITED | CELL_PATH_S
                        visited[offset(0, 0)] |= CELL_PATH_N
                        stack.append((stack[-1][0], stack[-1][1] - 1))
                    case 1: 
                        visited[offset(1, 0)] |= CELL_VISITED | CELL_PATH_W
                        visited[offset(0, 0)] |= CELL_PATH_E
                        stack.append((stack[-1][0] + 1, stack[-1][1]))
                    case 2:
                        visited[offset(0, 1)] |= CELL_VISITED | CELL_PATH_N
                        visited[offset(0, 0)] |= CELL_PATH_S
                        stack.append((stack[-1][0], stack[-1][1] + 1))
                    case 3: 
                        visited[offset(-1, 0)] |= CELL_VISITED | CELL_PATH_E
                        visited[offset(0, 0)] |= CELL_PATH_W
                        stack.append((stack[-1][0] - 1, stack[-1][1]))
                    case _:
                        print("ffs")
                visited_cnt += 1
            else:
                _ = stack.pop()



                

        

        
        # drawing section
        begin_drawing()
        for x in range(MAZE_WIDTH):
            for y in range(MAZE_HEIGHT):
                if visited[x + (y * MAZE_HEIGHT)] & CELL_VISITED == 0:
                    draw_rectangle(x * (PATH_WIDTH + 1 + SQUARE_WIDTH), y * (PATH_WIDTH + 1 + SQUARE_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, WHITE)
                else:
                    draw_rectangle(x * (PATH_WIDTH + 1 + SQUARE_WIDTH), y * (PATH_WIDTH + 1 + SQUARE_HEIGHT), SQUARE_WIDTH, SQUARE_HEIGHT, GREEN)
        clear_background(BLACK)
        end_drawing()
    close_window()



if __name__ == "__main__":
    main()
