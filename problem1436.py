#problem 1436 / destination city
# graph / out order
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        dic = {}
        for path in paths:
            if path[0] not in dic:
                dic[path[0]] = 0
            if path[1] not in dic:
                dic[path[1]] = 0
            dic[path[0]] += 1
        for key in dic.keys():
            if dic[key] == 0:
                return key