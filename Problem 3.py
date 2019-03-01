##Problem 3 /Longest Substring Without Repeating Characters

#My solution:
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr=[]
        i,j=0,0
        maxk=0
        while i+j<len(s):
            if s[i+j] not in substr:
                substr.append(s[i+j])
                j=j+1
            else:
                i=i+1
                j=0
                substr=[]
            if j>maxk:
                maxk=j
        return maxk

#An O(n) solution
##
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
