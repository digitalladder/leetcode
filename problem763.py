#problem 763 / partition labels
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i in range(len(S)):
            d[S[i]].append(i)
        res = []
        start,end = 0,0
        while start < len(S):
            end = max(d[S[start]])
            j = start+1
            while j <= end:
                if S[j] != S[start]:
                    end = max(end,max(d[S[j]]))
                j += 1
            res.append(end-start+1)
            start = end+1
        return res

##优化解法，只需要记录每个字母最后出现的下标，不需要defaultdict
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans