#problem 1249 / minimum remove to make valid parentheses
# stack, 可以用stack记录符合规则的括号下标，根据下标输出最后结果，不用所有字母入栈
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack,stack2 = [],[]
        flag = 0
        for ss in s:
            if ss == ')':
                if not stack or flag == 0:
                    continue
                else:
                    stack.append(ss)
                    flag -= 1
            else:
                if ss == '(':
                    flag += 1
                stack.append(ss)
        flag = 0
        while stack:
            p = stack.pop()
            if p == '(':
                if not stack2 or flag == 0:
                    continue
                else:
                    stack2.append(p)
                    flag -= 1
            else:
                if p == ')':
                    flag += 1
                stack2.append(p)
        stack2.reverse()
        return ''.join(stack2)
            