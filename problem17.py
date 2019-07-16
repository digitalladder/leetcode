#problem 17 / letter combinations of a phone number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        memo = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def helper(res,i,digits,temp):
            if i == len(digits):
                res.append(temp)
                return
            for d in memo[digits[i]]:
                helper(res,i+1,digits,temp+d)
        if not digits:
            return []
        res = []
        helper(res,0,digits,'')
        return res