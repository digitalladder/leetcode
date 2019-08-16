#problem 451 / sort characcters by frequency
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        res = ""
        for char,counts in count.most_common():
            res += char*counts
        return res