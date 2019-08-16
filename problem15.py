#problem 15 / 3sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s = i+1
            e = n-1
            while s < e:
                if nums[s]+nums[e]+nums[i] == 0:
                    res.append([nums[i],nums[s],nums[e]])
                    s += 1
                    while s<e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s]+nums[e]+nums[i] > 0:
                    e -= 1
                else:
                    s += 1
        return res

# more faster way, split nums into two parts
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
    	results=[]

        hashsets=[set(),set()] # hashsets[0] for negative numbers, hashsets[0] for 0 and positive numbers
        duplicates=set()	#record duplicate numbers, triplets and above should be counted as duplets, except in case of triplet 0's.
        for n in num:
        	if n==0 and 0 in hashsets[1] and 0 in duplicates and len(results)==0:
        		results.append([0,0,0])
        	if n <0:
        		if n in hashsets[0]:
        			duplicates.add(n)
        		else:
	        		hashsets[0].add(n)
        	else:
        		if n in hashsets[1]:
        			duplicates.add(n)
        		else:
	        		hashsets[1].add(n)
        sortedLists=[sorted(hashsets[0]),sorted(hashsets[1])]

        for x in xrange(len(sortedLists[0])):
        	if sortedLists[0][x] in duplicates:
        		if -2*sortedLists[0][x] in hashsets[1]:
        			results.append([sortedLists[0][x],sortedLists[0][x],-2*sortedLists[0][x]])
        	for y in xrange(x+1,len(sortedLists[0])):
        		if -(sortedLists[0][x]+sortedLists[0][y]) in hashsets[1]:
        			results.append([sortedLists[0][x],sortedLists[0][y],-sortedLists[0][x]-sortedLists[0][y]])

        for x in xrange(len(sortedLists[1])):
        	if sortedLists[1][x] in duplicates:
        		if -2*sortedLists[1][x] in hashsets[0]:
        			results.append([-2*sortedLists[1][x],sortedLists[1][x],sortedLists[1][x]])
        	for y in xrange(x+1,len(sortedLists[1])):
        		if -(sortedLists[1][x]+sortedLists[1][y]) in hashsets[0]:
        			results.append([-sortedLists[1][x]-sortedLists[1][y],sortedLists[1][x],sortedLists[1][y]])

     	
     	return results