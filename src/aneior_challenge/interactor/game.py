from src.aneior_challenge.entities.snake import Snake
from src.aneior_challenge.entities.board import Board


class Game:

    def __init__(self, board: Board, depth: int, snake: Snake):

        if depth < 1:
            raise AttributeError('Depth value incorrect')

        if not board.are_positions_correct(snake.get_snake()):
            raise AttributeError('Snake positions are incorrect')

        self.board = board
        self.depth = depth
        self.snake = snake

    def count_paths(self):

        def paths_recursive(board, snake, depth):

            if depth == 0:
                return 1
            else:
                snake_aux = Snake(snake.get_snake())
                snake_aux.pop()
                positions = board.get_position_neighbors(snake_aux.get_head_position())
                moves = []

                for pos in positions:
                    if not snake_aux.is_part_of_snake(pos):
                        moves.append(pos)

                num_paths = 0
                for mov in moves:
                    snake_aux2 = Snake(snake_aux.get_snake())
                    snake_aux2.push(mov)
                    num_paths += paths_recursive(board, snake_aux2, depth - 1)

                return num_paths

        return paths_recursive(self.board, self.snake, self.depth)

