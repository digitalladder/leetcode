#problem 1419 / minimum number of frogs croaking
class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        c,r,o,a,k = 0,0,0,0,0
        res = 0
        for s in croakOfFrogs:
            if s == 'c':
                c += 1
                r += 1
                o += 1
                a += 1
                k += 1
            elif s == 'r':
                r -= 1
                if r < 0:
                    return -1
            elif s == 'o':
                o -= 1
                if o < 0:
                    return -1
            elif s == 'a':
                a -= 1
                if a < 0:
                    return -1
            elif s == 'k':
                k -= 1
                if k < 0:
                    return -1
                else:
                    c -= 1
            else:
                return -1
            res = max(res,c)
        if c == r == o == a == k:
            return res
        else:
            return -1

# 用一个新计数器 记录需要的frog数
    def minNumberOfFrogs(self, croak):
        c, r, o, a, k, in_use, answer = 0, 0, 0, 0, 0, 0, 0
        for d in croak:
            if d == 'c':
                c, in_use = c+1, in_use+1
            elif d == 'r':
                r += 1
            elif d == 'o':
                o += 1
            elif d == 'a':
                a += 1
            else:
                k, in_use = k+1, in_use-1
                
            answer = max(answer, in_use)
            
            if c < r or r < o or o < a or a < k:
                return -1
            
        if in_use == 0 and c == r and r == o and o == a and a == k:
            return answer
        
        return -1