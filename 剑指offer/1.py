#二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = len(array[0])-1
        j = 0
        while 0 <= i < len(array[0]) and 0 <= j < len(array):
            if target == array[j][i]:
                return True
            if target > array[j][i]:
                j += 1
            else:
                i -= 1
        return False