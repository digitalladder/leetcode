#problem 20 / valid parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ss in s:
            if ss in "([{":
                stack.append(ss)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if ss == ")" and temp == "(":
                    continue
                elif ss == "]" and temp == "[":
                    continue
                elif ss == "}" and temp == "{":
                    continue
                else:
                    return False
        if not stack:
            return True
        return False