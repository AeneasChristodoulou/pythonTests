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

def evolutionary_grid_generator(grid: Grid) -> Grid:

    result = deepcopy(grid)
    for position_lines, a_line in enumerate(grid):
        for position_row, value in enumerate(a_line):
            neighbour_before = grid[position_lines][position_row - 1] if position_row != 0 else 0
            neighbour_after = grid[position_lines][position_row + 1] if position_row != len(a_line)-1 else 0

            if neighbour_before == 1 and neighbour_after == 1:

                result[position_lines][position_row] = 1
            else:
                result[position_lines][position_row] = 0


    return result


def test_evolutionary_grid_generator():
    assert evolutionary_grid_generator([[0, 0, 1]]) == [[0, 0, 0]]
    assert evolutionary_grid_generator([[1, 1, 1]]) == [[0, 1, 0]]
    #assert evolutionary_grid_generator()