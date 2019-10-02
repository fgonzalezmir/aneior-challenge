from array import array


class Snake:

    def __init__(self, snake_cells: array):
        self.queue = snake_cells[::-1]
        self.length = len(self.queue)
        self.correct_distances = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]

        self._is_correct_snake()

    def pop(self):
        self.queue.pop(0)
        return Snake(self.queue[::-1])

    def push(self, position):
        self.queue.append(list(position))
        return Snake(self.queue[::-1])

    def get_head_position(self):
        return tuple(self.queue[-1])

    def is_part_of_snake(self, position):
        return list(position) in self.queue

    def get_snake(self):
        return self.queue[::-1]

    def _is_correct_snake(self):

        if self.length < 2:
            raise AttributeError('Snake length too small')

        for i in range(len(self.queue)-1):
            distance = tuple(x - y for x, y in zip(self.queue[i], self.queue[i+1]))
            if distance not in self.correct_distances:
                raise AttributeError('Snake no well formed')
