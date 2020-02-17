#problem 1048 / longest string chain
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words,key = len)
        dic = {}
        res = 1
        for word in words:
            dic[word] = 1
            for i in range(len(word)):
                if word[:i]+word[i+1:] in dic:
                    dic[word] = max(dic[word],dic[word[:i]+word[i+1:]]+1)
        return max(dic.values())                