#problem 953 / verifying an alien dictionary
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        for i,letter in enumerate(order):
            dic[letter] = i
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            for k in range(min(len(word1),len(word2))):
                if word1[k] != word2[k]:
                    if dic[word1[k]] > dic[word2[k]]:
                        return False
                    break                       #此处一定要break
            else:
                if len(word1) > len(word2):
                    return False
        return True