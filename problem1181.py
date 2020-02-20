#problem 1181 / before and after puzzle
class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        front = collections.defaultdict(set)
        back = collections.defaultdict(set)
        res = set()
        for phrase in phrases:
            temp = phrase.split(' ')
            if temp[0] in back:
                res |= {a+phrase[len(temp[0]):] for a in back[temp[0]]}
            if temp[-1] in front:
                res |= {phrase+b for b in front[temp[-1]]}      # set()  |=   合并两个set，添加元素最好用这种方法
            front[temp[0]].add(phrase[len(temp[0]):])
            back[temp[-1]].add(phrase)
        return sorted(list(res))