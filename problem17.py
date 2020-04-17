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

# approach 2
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],
               5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],
               8:['t','u','v'],9:['w','x','y','z']}
        res = []
        for digit in digits:
            temp = []
            if not res:
                res.extend(dic[int(digit)])
            else:
                while res:
                    nextstep = res.pop()
                    for e in dic[int(digit)]:
                        temp.append(nextstep+e)
                res = temp
        return res