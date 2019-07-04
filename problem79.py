#problem 79 /word search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = {}
        
        if not board:
            return False
        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,word,i,j,visited,0):
                    return True
        return False
                    
    def dfs(self,board,word,row,line,visited,pos):
        xtrans = [-1,1,0,0]
        ytrans = [0,0,-1,1]
        if pos == len(word):
            return True
        if row < 0 or row >= len(board):
            return False
        if line < 0 or line >= len(board[0]):
            return False
        if visited.get((row,line)) or board[row][line] != word[pos]:
            return False
        visited[(row,line)] = True
        res = False
        for i in range(4):
            res = res or self.dfs(board,word,row+xtrans[i],line+ytrans[i],visited,pos+1)
        visited[(row,line)] = False
        
        return res