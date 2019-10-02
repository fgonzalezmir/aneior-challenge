import pytest
from src.aneior_challenge.entities.snake import Snake
from src.aneior_challenge.entities.board import Board
from src.aneior_challenge.interactor.game import Game


class GameTest:

    @staticmethod
    def test_games_1():

        board = Board([4, 3])
        snake = Snake([[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]])
        depth = 3

        game = Game(board, depth, snake)

        assert game.count_paths() == 7

    @staticmethod
    def test_games_2():

        board = Board([2, 3])
        snake = Snake([[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]])
        depth = 10

        game = Game(board, depth, snake)
        assert game.count_paths() == 1

    @staticmethod
    def test_games_3():
        board = Board([10, 10])
        snake = Snake([[5, 5], [5, 4], [4, 4], [4, 5]])
        depth = 4

        game = Game(board, depth, snake)

        assert game.count_paths() == 81


if __name__ == "__main__":
    GameTest.test_games_1()
    GameTest.test_games_2()
    GameTest.test_games_3()

