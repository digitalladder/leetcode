#problem 1408 / string matching in array
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

# 可先按长度排序
def stringMatching(self, words: List[str]) -> List[str]:
    if not words:
        return None
    
    words.sort(key=lambda w: len(w))
    res = set()
    
    for i, word in enumerate(words):
        for pw in words[i+1:]:
            if word in pw:
                res.add(word)
    return list(res)