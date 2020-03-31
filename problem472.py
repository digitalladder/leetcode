#problem 472 / concatenated words
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(word,cache,wordmap):
            if word in cache:
                return cache[word]
            for i in range(1,len(word)):
                if word[:i] in wordmap:
                    suffix = word[i:]
                    if suffix in wordmap or dfs(suffix,cache,wordmap):
                        cache[word] = True
                        return True
            cache[word] = False
            return False
        cache = {}
        wordmap = set(words)
        res = []
        for word in words:
            if dfs(word,cache,wordmap):
                res.append(word)
        return res