#problem 68 / text justification
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        temp = []
        length = 0
        for word in words:
            if len(temp)+length+len(word) > maxWidth:
                spacelen = maxWidth-length
                j = 0
                while j < spacelen:
                    temp[j%(len(temp)-1 or 1)] += ' '
                    j += 1
                res.append(''.join(temp))
                temp = []
                length = 0
            temp.append(word)
            length += len(word)
        if temp:
            spacelen = maxWidth-length-len(temp)+1
            temp[-1] += ' '*spacelen
            res.append(' '.join(temp))
        return res