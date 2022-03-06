
def create_dead_cells(x=2, y=2):
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
