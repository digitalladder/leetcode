#problem 412 / fizz buzz
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        dic = {3:'Fizz',5:'Buzz'}
        for num in range(1,n+1):
            ans_str = ''
            for key in dic.keys():
                if num%key == 0:
                    ans_str += dic[key]
            if not ans_str:
                ans_str = str(num)
            ans.append(ans_str)
        return ans