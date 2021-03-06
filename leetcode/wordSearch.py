# wordSearch: https://leetcode.com/problems/word-search/
# The question's input example is wrong. Input should be list of strings,
# not list of list of strings.


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[str]
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True

        my_board = [list(string) for string in board]
        # visited entries in board are set to None
        len_row = len(board[0])
        len_col = len(board)
        # each (x, y) as start point
        for y in xrange(len_row):
            for x in xrange(len_col):
                if self.dfs(my_board, word, x, y):
                    return True
        return False

    def dfs(self, board, word, x, y):
        # base case
        if len(word) == 0:
            return True

        len_row = len(board[0])
        len_col = len(board)
        new_word = word[1:]
        # index out of range, then failed
        if x < 0 or y < 0:
            return False
        if x >= len_col or y >= len_row:
            return False

        if board[x][y] == word[0]:
            # set visited to None
            board[x][y] = None
            if self.dfs(board, new_word, x, y+1):
                return True

            if self.dfs(board, new_word, x, y-1):
                return True

            if self.dfs(board, new_word, x+1, y):
                return True

            if self.dfs(board, new_word, x-1, y):
                return True
            # don't forget to set visited slot back to original char after the dfs's
            board[x][y] = word[0]
        return False

class WordPath:
    """
    @return: List[List[Tuples]], all possible paths that forms the word in the board
    """
    def find_path(self, board, word):
        self.result = []
        my_board = [list(string) for string in board]
        for x in xrange(len(my_board)):
            for y in xrange(len(my_board[0])):
                path = []
                if x == 0 and y == 2:
                    self.dfs(my_board, word, x, y, path)
        return self.result

    def dfs(self, board, word, x, y, path):
        # base: Success
        if len(word) == 0:
            # do not forget make new list()
            self.result.append(list(path))
            return True
        # base: Fail
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        # recursion
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if board[x][y] == word[0]:
            for direction in directions:
                board[x][y] = None
                new_x, new_y = x + direction[0], y + direction[1]
                path.append((x, y))
                if self.dfs(board, word[1:], new_x, new_y, path):
                    return True
                path.pop()
                board[x][y] = word[0]
        return False

board = [
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "CBF"
# Sol = Solution()
Path = WordPath()
# print Sol.exist(board, word)
print Path.find_path(board, word)