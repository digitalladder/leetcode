#problem 1451 / rearrange words in a sentence
class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.split(' ')
        for i in range(len(words)):
            words[i] = (len(words[i]),words[i].lower())
        res = ''
        words.sort(key = lambda x:x[0])
        for word in words:
            res += word[1]
            res += ' '
        return res[0].upper()+res[1:-1]