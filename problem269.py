#problem 269 / alien dictionary
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        adj = collections.defaultdict(set)
        degree = {key:0 for key in set(''.join(words))}
        for i in range(len(words)-1):                       #可用zip()函数   for pair in zip(words, words[1:]):                                                
            first,second = words[i],words[i+1]              #                   for c1, c2 in zip(*pair):
            for j in range(min(len(first),len(second))):
                if first[j] != second[j]:
                    if second[j] not in adj[first[j]]:
                        degree[second[j]] += 1
                    adj[first[j]].add(second[j])    
                    break
        queue = collections.deque()
        res = ''
        for key in degree:                  #filter()函数 queue = collections.deque(filter(lambda key: not degree[key], degree.keys()))
            if degree[key] == 0:
                queue.append(key)
        while queue:
            temp = queue.popleft()
            res += temp
            for letter in adj[temp]:
                degree[letter] -= 1
                if degree[letter] == 0:
                    queue.append(letter)
        return res if len(res) == len(degree) else ''       #最后要检查