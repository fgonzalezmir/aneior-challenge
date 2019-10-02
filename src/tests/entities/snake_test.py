import pytest
from src.aneior_challenge.entities.snake import Snake


class SnakeTest:

    @staticmethod
    def test_init_snake():
        snake = Snake([[5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]])
        assert snake.length == 6

        with pytest.raises(AttributeError) as exception_info:
            snake2 = Snake([[5, 0]])
        assert 'Snake length too small' in str(exception_info.value)

        with pytest.raises(AttributeError) as exception_info:
            snake2 = Snake([[5, 0], [1, 0], [3, 0], [2, 0], [1, 0], [0, 0]])
        assert 'Snake no well formed' in str(exception_info.value)

        assert snake.get_head_position() == (5, 0)

        assert snake.pop().get_snake() == [[5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]

        assert snake.push((5, 1)).get_snake() == [[5, 1], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]

    @staticmethod
    def test_part_of_snake():
        snake = Snake([[5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]])
        assert snake.is_part_of_snake([2, 0])
        assert not snake.is_part_of_snake([0, 1])


if __name__ == "__main__":
    SnakeTest.test_init_snake()
    SnakeTest.test_part_of_snake()


