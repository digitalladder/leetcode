#problem348 / design tic-tac-toe
# O(1) time each move() operation
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = [[-1]*n for i in range(n)]
        self.row_count = [[0]*n for i in range(2)]
        self.col_count = [[0]*n for i in range(2)]
        self.dia_count = [0,0]
        self.rev_dia_count = [0,0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.board[row][col] != -1:
            return False
        if player == 1:
            self.board[row][col] = 1
        else:
            self.board[row][col] = 2
        self.row_count[player-1][row] += 1
        self.col_count[player-1][col] += 1
        if row == col:
            self.dia_count[player-1] += 1
        if row + col == self.n-1:
            self.rev_dia_count[player-1] += 1
        if self.row_count[player-1][row] == self.n or self.col_count[player-1][col] == self.n or self.dia_count[player-1] == self.n or self.rev_dia_count[player-1] == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)