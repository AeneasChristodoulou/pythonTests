from copy import deepcopy
from typing import List
import fire


Grid = List[List[int]]


def main():
    pass


def create_dead_cells(x :int =2, y :int =2) -> Grid:
    grid_y = []
    for row_number in range(0, y):
        grid_y.append(0)

    grid_x = []
    for row_number in range(0, x):
        grid_x.append(grid_y)

    return grid_x


def test_create_grid():
    assert create_dead_cells(2, 5) == [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]
    assert create_dead_cells(1, 2) == [ [0, 0] ]
    assert create_dead_cells(2, 2) == [ [0, 0], [0, 0] ]


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
    dead = "."
    line_str = "\033c"
    for y_position, a_line in enumerate(grid):
        for x_position, value in enumerate(a_line):
            if value == 1:
                    line_str+=alive
            else:
                line_str += dead
        line_str+="\n"

    print(line_str)





def test_stay_alive():
    """
        Is the Cell able to survive?
        Yes if it has 2 or 3 neighbours
    """

    assert evolutionary_grid_generator(
        [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]) == [
               [0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]
           ]
    assert evolutionary_grid_generator([[0, 0, 1]]) == [[0, 0, 0]]
    assert evolutionary_grid_generator([[1, 1, 1]]) == [[0, 1, 0]]
    assert evolutionary_grid_generator(
        [
            [0,1,0],
            [0,1,1]
        ]) == [
            [0,1,1],
            [0,1,1]
        ]


def test_dont_stay_alive():

    assert evolutionary_grid_generator(
        [
            [0,1,0],
            [1,1,1],
            [0,1,0]
        ])  == [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ]


def test_get_alive():

    assert evolutionary_grid_generator(
        [
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0]
        ]) == [
               [0, 0, 0],
               [0, 1, 1],
               [0, 0, 0]
           ]

def test_limitations():
    assert evolutionary_grid_generator(
        [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0]
        ]) == [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0]
           ]


if __name__ == '__main__':
        fire.Fire()