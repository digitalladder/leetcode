# problem 636 / exclusive time of functions
# stack
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        first = logs[0].split(':')
        stack.append(int(first[0]))
        res = [0]*n
        i = 1
        prev = int(first[2])
        while i < len(logs):
            temp = logs[i].split(':')
            if temp[1] == 'start':
                if stack:
                    res[stack[-1]] += int(temp[2])-prev
                stack.append(int(temp[0]))
                prev = int(temp[2])
            else:
                res[stack[-1]] += int(temp[2])-prev+1
                stack.pop()
                prev = int(temp[2])+1
            i += 1
        return res