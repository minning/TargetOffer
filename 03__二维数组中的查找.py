# coding:utf-8
'''
    代码目的：剑指offer 第 3 题
            题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
                每一列都按照从上到下递增的顺序排序。请完成一个函数，
                输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
            解题思路：
                从右上角（左下角）开始找，
                1)命中，查找成功
                2)右上角数字比target大，删除最右一行
                3）右上角比target小，删除上一行

                左下角类似，主要思想 夹逼 。
    
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array) - 1
        n = len(array[0]) - 1
        i = 0

        while i <= m and n >= 0:
            if array[i][n] == target:
                return True
            elif array[i][n] > target:
                n -= 1
            elif array[i][n] < target:
                i += 1
        return False

    def searchNum(self,target, array):
        '''
        搜索递增列表中包含几个target
        '''
        m = len(array) - 1
        n = len(array[0]) - 1
        i = 0
        count = 0
        while i <= m and n >= 0:
            if array[i][n] == target:
                count += 1
                i += 1
            elif array[i][n] > target:
                n -= 1
            elif array[i][n] < target:
                i += 1
        return count


arr = [[1,4,8,9],
       [4,7,10,13]]
target = 4
s = Solution()
print s.Find(target,arr)
print s.searchNum(target,arr)

