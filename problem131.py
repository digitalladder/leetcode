#Problem 131 /Palindrome Partitioning
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        path = []
        self.createpartition(s,0,path,result)
        return result
    def createpartition(self,s,index,path,result):
        if index == len(s):
            result.append(path)
            return
        for i in range(index,len(s)):
            if self.ifpalindrome(s[index:i+1]):
                self.createpartition(s,i+1,path+[s[index:i+1]],result)
    def ifpalindrome(self,s):
        palinset = []
        if len(s) == 1 or s in palinset:
            return True
        for i in range(0,len(s)/2):
            if s[i] != s[len(s)-i-1]:
                return False
        palinset.append(s)
        return True

#Solution two (more faster way)        