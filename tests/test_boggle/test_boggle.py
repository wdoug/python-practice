import unittest

import pytest
from boggle.boggle import Boggle


class TestBoggle(unittest.TestCase):
    def test_single_char_boggle_board_no_match(self) -> None:
        board = [['x']]
        allowed_words = ['a']
        b = Boggle(board, allowed_words)
        board_words = b.get_all_board_words()
        self.assertEqual(board_words, set())

    def test_single_char_boggle_board_match(self) -> None:
        board = [['a']]
        allowed_words = ['a']
        b = Boggle(board, allowed_words)
        board_words = b.get_all_board_words()
        self.assertEqual(board_words, {'a'})

    def test_small_boggle_board(self) -> None:
        # fmt: off
        board = [
            ['c', 'a'],
            ['n', 't']
        ]
        # fmt: on
        allowed_words = ['a', 'an', 'at', 'cat', 'sat', 'tac']
        b = Boggle(board, allowed_words)
        board_words = b.get_all_board_words()
        self.assertEqual(board_words, {'a', 'an', 'at', 'cat', 'tac'})

    def test_multiple_of_same_word(self) -> None:
        """When there are multiple options for 'ax', it should still work properly"""
        # fmt: off
        board = [
            ['c', 'a', 'x'],
            ['n', 't', 'x'],
            ['x', 'x', 'x']
        ]
        # fmt: on
        allowed_words = ['a', 'an', 'at', 'ax', 'cat', 'sat', 'tac']
        b = Boggle(board, allowed_words)
        board_words = b.get_all_board_words()
        self.assertEqual(board_words, {'a', 'an', 'ax', 'at', 'cat', 'tac'})

    def test_invalid_board_input(self) -> None:
        with pytest.raises(TypeError):
            Boggle(5, [])

    def test_invalid_board_shape(self) -> None:
        with pytest.raises(TypeError):
            Boggle([[], ['a']], [])

    def test_sanitize_words(self) -> None:
        """Input words are sanitized"""
        board = [['a', 'i']]
        allowed_words = ['  A ', 'I']
        b = Boggle(board, allowed_words)
        board_words = b.get_all_board_words()
        self.assertEqual(board_words, {'a', 'i'})
