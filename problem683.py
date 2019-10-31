#problem 683 / k tmpty slots
class Solution(object):                         #O(N)
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        n = len(bulbs)
        days = [0]*n
        for d,pos in enumerate(bulbs,1):
            days[pos-1] = d
        
        ans = n+1
        left,right = 0,K+1
        while right < n:
            for i in xrange(left+1,right):              #范围很大时 xrange 比 range 速度快很多，此题用 range 会超时
                if days[i] < days[left] or days[i] < days[right]:
                    left,right = i,i+K+1
                    break
            else:
                ans = min(ans,max(days[left],days[right]))
                left,right = right,right+K+1
        return ans if ans < n+1 else -1

#O(NlogN)
class Solution(object):
    def kEmptySlots(self, bulbs, k):
        active = []
        for day, bulb in enumerate(bulbs, 1):
            i = bisect.bisect(active, bulb)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - bulb) - 1 == k:
                    return day
            active.insert(i, bulb)
        return -1