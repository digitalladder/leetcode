#problem 1169 / invalid transactions
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        temp = collections.defaultdict(list)
        res = set()
        for tran in transactions:
            name,time,amount,city = tran.split(',')
            if int(amount) > 1000:
                res.add(tran)
            if name in temp:
                for tt,aa,cc in temp[name]:
                    if city != cc and abs(int(time)-int(tt)) <= 60:
                        res.add(','.join([name,tt,aa,cc]))
                        res.add(tran)
                          
            temp[name].append([time,amount,city])
        return res