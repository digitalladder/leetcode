#problem 51 / n-queens
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(row,state,res):
            if row == n:
                path = []
                for k,s in enumerate(state):
                    path.append('.'*s+'Q'+'.'*(n-s-1))
                res.append(path)
                return
            for i in range(n):
                state[row] = i
                if available(row,state):
                    dfs(row+1,state,res)
        def available(row,state):
            for j in range(row):
                if state[j] == state[row]:
                    return False
                if abs(state[row]-state[j]) == row-j:
                    return False
            return True  
        state = [-1]*n
        res = []
        dfs(0,state,res)
        return res