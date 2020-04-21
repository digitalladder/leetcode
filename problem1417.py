#problem 1417 / reformat the string
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = []
        let = []
        for ss in s:
            if 48<=ord(ss)<=57:
                num.append(ss)
            else:
                let.append(ss)
        if abs(len(num)-len(let)) > 1:
            return ''
        res = ''
        if len(num) > len(let):
            res += num.pop()
        while num or let:
            if let:
                res += let.pop()
            if num:
                res += num.pop()
        return res