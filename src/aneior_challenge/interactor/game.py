from src.aneior_challenge.entities.snake import Snake
from src.aneior_challenge.entities.board import Board


class Game:

    @staticmethod
    def count_paths(board: Board, depth: int, snake: Snake):

        def paths_recursive(_board, _snake, _depth):
            snake_aux = _snake.pop()
            positions = _board.get_position_neighbors(snake_aux.get_head_position())
            moves = []

            for pos in positions:
                if not snake_aux.is_part_of_snake(pos):
                    moves.append(pos)

            if _depth == 1:
                return len(moves)
            else:
                num_paths = 0
                for mov in moves:
                    snake_aux_2 = Snake(snake_aux.get_snake()).push(mov)
                    num_paths += paths_recursive(_board, snake_aux_2, _depth - 1)

            return num_paths

        if depth < 1:
            raise AttributeError('Depth value incorrect')

        if not board.are_positions_correct(snake.get_snake()):
            raise AttributeError('Snake positions are incorrect')

        return paths_recursive(board, snake, depth)

