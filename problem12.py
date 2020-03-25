#problem 12 / integer to roman
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mappint = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        mapprom = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        ans = ''
        for i in range(13):
            a = num/mappint[i]
            b = num%mappint[i]
            ans += mapprom[i]*a
            num = b
        return ans