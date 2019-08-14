#problem 242 / valid anagram
#sort
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

#hash table
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = {}
        for cs in s:
            if cs not in counter:
                counter[cs] = 1
            else:
                counter[cs] += 1
        for ct in t:
            if ct not in counter:
                return False
            counter[ct] -= 1
            if counter[ct] < 0:
                return False
        return True