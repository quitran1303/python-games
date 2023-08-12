"""
Stores the state of the drawgin board
"""


class Board(object):
    ROWS, COLS = 720, 720

    def __init__(self):
        """
        Init the board by creating empty board (all white pixels)
        """
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        Update a singular pixel of the board
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return:
        """
        self.data[y][x] = color

    def clear(self):
        """
        clear board to white
        :return: None
        """
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        """
        Creates an empty board (all white)
        :return: None
        """
        return self.data[[(255, 255, 255) for _ in range(self.COLS)] in range(self.ROWS)]

    def fill(self, x, y):
        """
        Fills in a specific shape or area using recursion
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def get_board(self):
        """
        gets the data of the board
        :return: (int, int, int)
        """
        return self.data
