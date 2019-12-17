#problem 1291 / sequential digits
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def digitsnum(num):
            n = 0
            while num:
                num = num//10
                n += 1
            return n
        n = digitsnum(low)
        m = digitsnum(high)
        res = set()
        l = n
        while l < m+1:
            for i in range(1,10):
                temp = 0
                for j in range(i,min(10,i+l)):
                    temp = temp*10+j
                if temp <= high and temp >= low:
                    res.add(temp)
            l += 1
        return sorted(res)

##
def sequentialDigits(self, low: int, high: int) -> List[int]:
    ans = []
    for digit in range(1, 9):
        num = next = digit
        while num <= high and next < 10:
            if num >= low:
                ans.append(num)
            next += 1
            num = num * 10 + next
    return sorted(ans)