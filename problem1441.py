#problem 1441 / build an array with stack operations
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        m = len(target)
        curr = 1
        for i in range(m):
            if target[i] != curr:
                while target[i] != curr:
                    curr += 1
                    res.append('Push')
                    res.append('Pop')
            res.append('Push')
            curr += 1
        return res