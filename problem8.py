#problem 8 / string to integer(atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        s = str.strip()
        i, res = 0,0                        #注意特殊输入：'+-2', ' -22', 'word 987'以及输入为零的情况 
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-','+']:
            s = s[1:]
        while i < len(s):
            if s[i].isdigit():
                res = res*10+int(s[i])
                if res > 2**31-1 and sign == 1:
                    return MAX_INT
                if res > 2**31 and sign == -1:
                    return MIN_INT
            else:break
            i+=1
        return res*sign

#re模块正则匹配解法
    class Solution:
        # @return an integer
        def atoi(self, str):
            str = str.strip()
            str = re.findall('(^[\+\-0]*\d+)\D*', str)
    
            try:
                result = int(''.join(str))
                MAX_INT = 2147483647
                MIN_INT = -2147483648
                if result > MAX_INT > 0:
                    return MAX_INT
                elif result < MIN_INT < 0:
                    return MIN_INT
                else:
                    return result
            except:
                return 0