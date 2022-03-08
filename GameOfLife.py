from copy import deepcopy
from typing import List
import fire
from time import sleep
from random import randrange


Grid = List[List[int]]


def main(amountofsleep: float = None, amountofrows: int = None, amountoflines: int = None):
    if not amountofsleep:
        amountofsleep = float(input("Enter Amount of Sleep(Speed): "))
    if not amountofrows:
        amountofrows = int(input("Enter Amount of Rows(Y-Axis): "))
    if not amountoflines:
        amountoflines = int(input("Enter Amount of Lines(X-Axis): "))
    grid = create_dead_cells(amountofrows, amountoflines)
    grid = initialize_random(grid)
    build_printable_grid(grid)
    while(True):
        sleep(amountofsleep)
        grid = evolutionary_grid_generator(grid)
        build_printable_grid(grid)


def initialize_random(grid):
    for y_position, a_line in enumerate(grid):
        for x_position, value in enumerate(a_line):
            random_number = randrange(100)
            if random_number < 23:
                    grid[y_position][x_position] = 1

    return grid


def create_dead_cells(x: int = 2, y: int = 2) -> Grid:
    grid_y = []
    for row_number in range(0, y):
        grid_y.append(0)

    grid_x = []
    for row_number in range(0, x):
        grid_x.append(deepcopy(grid_y))

    return grid_x


def get_neighbour_value(y, x, y_position, x_position, grid):
    new_y = y_position + y
    if new_y == -1:
        return 0

    new_x = x_position + x
    if new_x == -1:
        return 0


    try:
        result =  grid[new_y][new_x]
    except:
        return 0

    return result


def evolutionary_grid_generator(grid: Grid) -> Grid:

    result = deepcopy(grid)
    for y_position, a_line in enumerate(grid):
        for x_position, value in enumerate(a_line):

            North = get_neighbour_value(-1, 0, y_position, x_position, grid)
            East = get_neighbour_value(0, 1, y_position, x_position, grid)
            South = get_neighbour_value(1, 0, y_position, x_position, grid)
            West = get_neighbour_value(0, -1, y_position, x_position, grid)
            NorthEast = get_neighbour_value(-1, 1, y_position, x_position, grid)
            SouthEast = get_neighbour_value(1, 1, y_position, x_position, grid)
            SouthWest = get_neighbour_value(1, -1, y_position, x_position, grid)
            NorthWest = get_neighbour_value(-1, -1, y_position, x_position, grid)

            total = North + East + South + West + NorthEast + SouthEast + SouthWest + NorthWest
            is_alive = result[y_position][x_position] == 1

            if total == 2 and is_alive:
                result[y_position][x_position] = 1
            elif total == 3:
                result[y_position][x_position] = 1
            else:
                result[y_position][x_position] = 0

    return result


def build_printable_grid(grid):
    alive = "*"
    dead = " "
    print("\033c")
    for a_line in grid:
        line_str = ""
        for value in a_line:
            if value == 1:
                line_str += alive
            else:
                line_str += dead
        print(line_str)


if __name__ == '__main__':
    fire.Fire()
