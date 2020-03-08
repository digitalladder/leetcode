#problem 415 / add strings
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num2:
            return num1
        if not num1:
            return num2
        n = len(num1)
        m = len(num2)
        if n > m:
            n,m = m,n
            num1,num2 = num2,num1
        def add(num1,num2,offset):
            if not num1 and not num2:
                return ['',0]
            if offset > 0:
                temp,carry = add(num1,num2[1:],offset-1)
                carry,summary = divmod(int(num2[0])+carry,10)
            elif offset == 0:
                temp,carry = add(num1[1:],num2[1:],0)
                summary = int(num1[0])+int(num2[0])+carry
                carry,summary = divmod(summary,10)
            return [str(summary)+temp,carry]
        a,b = add(num1,num2,m-n)
        if b == 1:
            a = '1'+a
        return a

#也可以用stack