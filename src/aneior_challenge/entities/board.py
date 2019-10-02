from array import array


class Board:

    def __init__(self, dimensions: array):
        if len(dimensions) != 2:
            raise AttributeError('Invalid number of dimensions for Board')

        self.weight = dimensions[0]
        self.height = dimensions[1]
        self.num_cells = self.weight * self.height

        if self.height < 1 or self.weight < 1:
            raise AttributeError('Board size is not correct')

        self.movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def is_correct_position(self, position: tuple):
        if position[0] < 0 or position[0] >= self.weight:
            return False

        if position[1] < 0 or position[1] >= self.height:
            return False

        return True

    def are_positions_correct(self, positions):

        for position in positions:
            if not self.is_correct_position(tuple(position)):
                return False

        return True

    def get_position_neighbors(self, position):
        if not self.is_correct_position(position):
            raise AttributeError('Original position not in the board')

        result = []

        for movement in self.movements:
            cell = tuple(x + y for x, y in zip(position, movement))
            if self.is_correct_position(cell):
                result.append(cell)

        return result


