#problem 1153 / string transforms into another string
class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        graph = {}
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i] not in graph:
                    graph[str1[i]] = str2[i]
                else:
                    if graph[str1[i]] != str2[i]:
                        return False
        return len(set(str2)) < 26