#problem 22 /Generate parentheses
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.helper('',0,0,ans,n)
        return ans
        
    def helper(self,s,left,right,ans,n):
        if len(s) == 2*n:
            ans.append(s)
            return
        if left < n:
            self.helper(s+'(',left+1,right,ans,n)
        if right < left:
            self.helper(s+')',left,right+1,ans,n)