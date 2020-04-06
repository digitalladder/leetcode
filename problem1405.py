#problem 1405 / longest happy string
# heap / max heap
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        if a == 0 and b == 0 and c == 0:
            return ''
        res = ''
        heap = [(-a,'a'),(-b,'b'),(-c,'c')]
        heapq.heapify(heap)
        pre_val = 0
        pre_let = ''
        while heap:
            val,let = heapq.heappop(heap)
            if pre_val < 0:
                heapq.heappush(heap,(pre_val,pre_let))
            if abs(val) >= 2:
                if abs(val) > abs(pre_val):
                    res += let*2
                    val += 2
                else:
                    res += let
                    val += 1
            elif abs(val) == 1:
                res += let
                val += 1
            elif val == 0:
                break
            pre_val = val
            pre_let = let
        return res