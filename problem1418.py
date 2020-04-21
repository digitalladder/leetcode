#problem 1418 / display table of food order
class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        items = set()
        for order in orders:
            table[int(order[1])].append(order[2])
            items.add(order[2])
        res = []
        temp = ['Table']
        temp.extend(sorted(items))
        res.append(temp)
        mapper = {}
        temp = sorted(items)
        for i,t in enumerate(temp):
            mapper[t] = i+1
        for key in sorted(table.keys()):
            print(key)
            temp = ['0']*(len(items)+1)
            temp[0] = str(key)
            for item in table[key]:
                temp[mapper[item]] = str(int(temp[mapper[item]])+1)
            res.append(temp)
        return res
            
# collections.Counter 
import collections
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        desk = collections.defaultdict(collections.Counter)
        meal = set()
        for _, table, food in orders:
            meal.add(food)
            desk[table][food] += 1
        foods = sorted(meal)
        result = [['Table'] + [food for food in foods]]
        for table in sorted(desk, key=int):
            result.append([table] + [str(desk[table][food]) for food in foods])
        return result
                