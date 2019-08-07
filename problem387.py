#problem 387 / first unique character in a string
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for ss in s:
            if ss not in count:
                count[ss] = 1
            else:
                count[ss] += 1
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1