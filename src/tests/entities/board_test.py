import pytest
from src.aneior_challenge.entities.board import Board


class BoardTest:

    @staticmethod
    def test_init_board():
        board = Board([4, 5])
        assert board.num_cells == 20

        with pytest.raises(AttributeError) as exception_info:
            board2 = Board([0, 0])
        assert 'Board size is not correct' in str(exception_info.value)

        with pytest.raises(AttributeError) as exception_info:
            board3 = Board([-10, 4])
        assert 'Board size is not correct' in str(exception_info.value)

        with pytest.raises(AttributeError) as exception_info:
            board4 = Board([1, 4, 3])
        assert 'Invalid number of dimensions for Board' in str(exception_info.value)

    @staticmethod
    def test_position_in_board():
        board = Board([4, 5])
        assert not board.is_correct_position((4, 5))
        assert board.is_correct_position((0, 0))
        assert board.is_correct_position((2, 3))
        assert not board.is_correct_position((-1, 4))
        assert not board.is_correct_position((2, 6))
        assert board.is_correct_position((3, 4))

        assert board.are_positions_correct([[1, 0], [2, 0], [3, 3]])
        assert not board.are_positions_correct([[-1, 0], [2, 0], [3, 3]])
        assert not board.are_positions_correct([[4, 0], [2, 0], [3, 3]])

    @staticmethod
    def test_movements():
        board = Board([4, 5])

        assert board.get_position_neighbors((2, 3)) == [(2, 2), (2, 4), (1, 3), (3, 3)]
        assert board.get_position_neighbors((0, 0)) == [(0, 1), (1, 0)]
        assert board.get_position_neighbors((3, 4)) == [(3, 3), (2, 4)]
        assert board.get_position_neighbors((3, 3)) == [(3, 2), (3, 4), (2, 3)]

        with pytest.raises(AttributeError) as exception_info:
            board.get_position_neighbors((21, 3))
        assert 'Original position not in the board' in str(exception_info.value)


if __name__ == "__main__":
    BoardTest.test_init_board()
    BoardTest.test_position_in_board()
    BoardTest.test_movements()
