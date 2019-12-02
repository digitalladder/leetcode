#problem 1275 / find winner on a tic tac toe game
##
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def iffin(board):
            for i in range(9):
                if board[i] == '-':
                    return False
            return True
        def winner(board):
            lines = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:7:2]]
            if ['x']*3 in lines:
                return 'A'
            elif ['o']*3 in lines:
                return 'B'
            elif not iffin(board):
                return 'Pending'
            else:
                return 'Draw'
        board = ['-']*9
        for i in range(len(moves)):
            move = moves[i]
            if i%2 == 0:
                board[move[0]*3+move[1]] = 'x'
            else:
                board[move[0]*3+move[1]] = 'o'
        return winner(board)
##method 2
def tictactoe(self, moves: List[List[int]]) -> str:
        def has_won(i, j, ch): 
            rows[(i, ch)] += 1
            cols[(j, ch)] += 1
            if i == j: diaga[ch] += 1
            if i + j == 2: diagb[ch] += 1
            if rows[(i, ch)] == 3 or cols[(j, ch)] == 3 or diaga[ch] == 3 or diagb[ch] == 3:
                return True
            
        rows, cols, diaga, diagb = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for p, (i,j) in enumerate(moves):
            if has_won(i, j, p%2):
                return "A" if p%2 == 0 else "B"
        return "Draw" if len(moves) == 9 else "Pending"