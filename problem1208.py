#problem 1208 / get equal substrings within budget
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """

        diff = [0]*len(s) 
        for i in range(len(s)):
            diff[i] = abs(ord(s[i])-ord(t[i]))
        i = j = 0
        cost = 0
        for j in range(len(s)):
            cost += diff[j]
            if cost > maxCost:
                cost -= diff[i]
                i += 1
        return j-i+1