#problem 1410 / HTML entity parser
class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        res = ''
        temp = ''
        flag = 0
        dic_ = {'&quot;':'\"', '&apos;':"'", '&amp;': '&', '&gt;': '>', '&lt;' : '<', '&frasl;': '/'}
        for t in text:
            if not flag:
                if t == '&':
                    temp += t
                    flag = 1
                else:
                    res += t
            else:
                if t == '&':
                    res += temp
                    temp = '&'
                elif t == ';':
                    temp += t
                    if temp in dic_:
                        res += dic_[temp]
                    else:
                        res += temp
                    temp = ''
                    flag = 0
                else:
                    temp += t
        return res