#problem 459 / Repeated Substring Pattern
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1,n/2+1):
            if n%i == 0 and self.check(s,i,n):
                return True
        return False
                
    def check(self,s,i,n):
        l = i
        k = 0
        while l < n:
            if s[l] != s[k]:
                return False
            else:
                l=l+1
                k=k+1
                if k == i:
                    k = 0
        return True

#Treaky way
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s[1:]+s[:-1]   #if ss includes s, than s has repeated substring pattern
        return ss.find(s) != -1