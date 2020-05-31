# problem 1455 / check if a word occurs as a prefix of any word in a sentence
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sent = sentence.split(' ')
        n = len(sent)
        for i in range(n):
            if searchWord == sent[i][:len(searchWord)]:
                return i+1
        return -1