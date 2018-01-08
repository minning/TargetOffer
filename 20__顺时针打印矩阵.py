# coding:utf-8
'''
    Author:minning
    Date:2018/1/8
    代码目的：剑指offer 第 20 题：二叉树的镜像
            题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
                  例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
                  则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
            思路：依次打印矩阵的第一行元素，然后将第一行删除后将矩阵逆时针旋转90度，重复上述操作
    
'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            matrix = map(list, zip(*matrix))[::-1]
            print matrix
        return ret


s = Solution()
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8]]
print s.printMatrix(matrix)
