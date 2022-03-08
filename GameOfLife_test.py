from GameOfLife import create_dead_cells, evolutionary_grid_generator


def test_create_grid():
    assert create_dead_cells(2, 5) == [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]
    assert create_dead_cells(1, 2) == [ [0, 0] ]
    assert create_dead_cells(2, 2) == [ [0, 0], [0, 0] ]


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
