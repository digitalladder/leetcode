#problem 394 / decode string
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                temp = ''
                while stack:
                    x = stack.pop()
                    if x != '[':
                        temp = x+temp
                    else:
                        n = ''
                        while stack and stack[-1].isdigit():
                            n = stack.pop()+n
                        stack.append(temp*int(n))
                        break
        return ''.join(stack)