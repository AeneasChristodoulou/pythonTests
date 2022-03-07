from copy import deepcopy
from typing import List


Grid = List[List[int]]
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

def get_grid_value(y, x, y_position, x_position, grid):
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

            neighbour_N = grid[y_position - 1][x_position] if y_position != 0 else 0
            neighbour_E = grid[y_position][x_position + 1] if x_position != len(a_line)-1 else 0
            neighbour_S = grid[y_position +1][x_position] if y_position != len(grid)-1 else 0
            neighbour_W = get_grid_value(0, -1, y_position, x_position, grid)

            neighbour_NE = get_grid_value(-1, 1, y_position, x_position, grid)
            neighbour_SE = get_grid_value(1, 1, y_position, x_position, grid)
            neighbour_SW = get_grid_value(1, -1, y_position, x_position, grid)
            neighbour_NW = get_grid_value(-1, -1, y_position, x_position, grid)

            total = neighbour_N + neighbour_E + neighbour_S + neighbour_W + neighbour_NE + neighbour_SE + neighbour_SW + neighbour_NW
            if total >= 2 and result[y_position][x_position] == 1:
                result[y_position][x_position] = 1
            else:
                result[y_position][x_position] = 0


    return result


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
            [0,1,0],
            [0,1,1]
        ]

