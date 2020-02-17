#problem 735 / asteroid collision
#stack solution
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == -ast:
                        stack.pop()
                        break
                    elif stack[-1] < -ast:
                        stack.pop()
                        continue
                    else:
                        break
                else:
                    stack.append(ast)
        return stack

##合理利用 break continue else 使代码更简洁
class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans