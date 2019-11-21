#problem 347 / top k frequent elements
import heapq
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k,count.keys(), key = count.get)

#
from collections import Counter, defaultdict        
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq, result = Counter(nums), []
        inverse_freq = defaultdict(list)
        for k1,v1 in freq.items():
            inverse_freq[v1].append(k1)
        for x in range(len(nums), 0, -1):
            if x in inverse_freq:
                result.extend(inverse_freq[x])
                if len(result) >= k:
                    break
        return result[:k]