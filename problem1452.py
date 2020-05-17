#problem 1452 / people whose list of favorite companies is not a subset of another list
# hashmap
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        dic = collections.defaultdict(set)
        for i,favorite in enumerate(favoriteCompanies):
            for company in favorite:
                dic[i].add(company)
        res = []
        for p in range(len(favoriteCompanies)):
            subs = set(favoriteCompanies[p])
            res.append(p)
            for i in range(len(favoriteCompanies)):
                if i == p:
                    continue
                else:
                    full = dic[i]
                    if subs.issubset(full):
                        res.pop()
                        break
        return res