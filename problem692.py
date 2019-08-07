#problem 692 / top k frequent words
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w],w))      #.sort()默认升序排列，所以加负号，或者指定reverse参数
        return candidates[:k]