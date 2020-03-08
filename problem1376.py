#problem 1376 / Time Needed to Inform All Employees
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        manage = collections.defaultdict(list)
        for i in range(n):
            manage[manager[i]].append(i)
        res = 0
        queue = collections.deque([(headID,0)])
        while queue:
            tempid,time = queue.popleft()
            totaltime = time + informTime[tempid]
            res = max(res,totaltime)
            for employee in manage[tempid]:
                queue.append((employee,totaltime))
        return res