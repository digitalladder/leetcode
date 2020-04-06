#problem 1062 / longest repeating substring
# rolling hash / binary search
class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        def search(l,a,modulus,n,nums):
            h = 0
            for i in range(l):
                h = (h*a+nums[i])%modulus
            seen = {h}
            al = pow(a,l,modulus)
            for start in range(1,n-l+1):
                h = (h*a-nums[start-1]*al+nums[start+l-1])%modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1
        
        n = len(S)
        nums = [ord(S[i])-ord('a') for i in range(n)]
        left = 1
        right = n
        while left <= right:
            mid = left+(right-left)//2
            if search(mid,26,2**24,n,nums) != -1:
                left = mid+1
            else:
                right = mid-1
        return left-1