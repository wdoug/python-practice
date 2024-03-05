from typing import Iterable, List, MutableSet

type InputBoard = List[List[str]]

_trie_end = '_END_'


class Boggle:
    board: InputBoard
    trie: dict = {}

    def __init__(self, board: InputBoard, allowed_words: Iterable[str]) -> None:
        self.validate_board(board)
        self.board = board
        self.set_words_trie(allowed_words)

    def validate_board(self, board: InputBoard):
        # make sure the board is iterable
        iter(board)
        width = len(board[0])
        for row in board:
            if len(row) != width:
                raise TypeError('Board is not an iterable')

    def sanitize_word(self, word: str) -> str:
        return word.lower().strip()

    def set_words_trie(self, allowed_words: Iterable[str]) -> None:
        for w in allowed_words:
            word = self.sanitize_word(w)
            current_dict = self.trie
            for char in word:
                if char not in current_dict:
                    current_dict[char] = {}
                current_dict = current_dict[char]
            current_dict[_trie_end] = True

    def get_all_board_words(self) -> MutableSet[str]:
        def get_unused_neighbors(r: int, c: int, visited_nodes: set) -> set:
            neighbors = set()
            for i in [r - 1, r, r + 1]:
                for j in [c - 1, c, c + 1]:
                    if i >= 0 and j >= 0 and i < len(self.board) and j < len(self.board[0]):
                        neighbors.add((i, j))
            return neighbors - visited_nodes

        def dfs_get_words(
            r: int,
            c: int,
            visited_board_nodes=frozenset(),
            parent_trie_node: dict = self.trie,
            word_seg: str = '',
        ) -> MutableSet[str]:
            char = self.board[r][c]
            if char not in parent_trie_node:
                return set()
            trie_node = parent_trie_node[char]
            words = set()

            if _trie_end in trie_node:
                words.add(word_seg + char)

            visited_nodes = visited_board_nodes | {(r, c)}
            neighbors = get_unused_neighbors(r, c, visited_nodes)

            for nr, nc in neighbors:
                words |= dfs_get_words(nr, nc, visited_nodes, trie_node, word_seg + char)

            return words

        all_words = set()

        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                all_words |= dfs_get_words(r, c)

        return all_words
