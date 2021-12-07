from typing import List
from typing import Optional


class Solution:

    def __init__(self):
        self.m = 0
        self.n = 0

    def check_boundary(self, row, col):
        if 0 <= row <= self.m - 1 and 0 <= col <= self.n - 1:
            return True
        else:
            return False

    def get_neighors(self, row, col):
        neighbors = []
        if self.check_boundary(row, col + 1):
            neighbors.append((row, col + 1))
        if self.check_boundary(row, col - 1):
            neighbors.append((row, col - 1))
        if self.check_boundary(row + 1, col):
            neighbors.append((row + 1, col))
        if self.check_boundary(row - 1, col):
            neighbors.append((row - 1, col))
        return neighbors

    def search_from(self, i, j, word, board):

        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        # first character is found, check the remaining part
        tmp = board[i][j]
        board[i][j] = "#"  # avoid visit again

        # check if new path with neighbor added equal to the prefix of word
        ns = self.get_neighors(i, j)
        res = self.search_from(i, j, word[1:], board)
        for n in ns:
            res = res or self.search_from(n[0], n[1], word[1:], board)

        board[i][j] = tmp
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        i = 0
        while i < self.m:
            j = 0
            while j < self.n:
                if self.search_from(i, j, word, board):
                    return True
                j += 1
            i += 1
        return False

def test():
    solution = Solution()
    # test method
    print(solution.exist([["a"]], "a"))
    print(solution.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(solution.exist([['a', 'b'], ['c', 'd']], "acdb"))
    print(solution.exist(
        [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
        , "AAAAAAAAAAAAAA"))

    # False
    print(solution.exist([["a"]], "ab"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
    print(solution.exist(
        [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
        , "AAAAAAAAAAAABA"))


test()
