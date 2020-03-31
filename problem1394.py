#problem 1394 / find lucky interger in an array
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = collections.Counter(arr)
        res = -1
        for i in count.keys():
            if i == count[i]:
                res = max(res,i)
        return res