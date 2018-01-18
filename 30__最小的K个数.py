# coding:utf-8
'''
    author : minning 
    Date : 2018/1/18
    代码目的：剑指offer 第 30 题 ：最小的K个数
            题目：输入 n 个整数，找出其中最小的 K 个数。例如输入 4,5,1,6,2,7,3,8 这 8 个数字，则最小的 4 个数字是 1,2,3,4,。
            思路：冒泡排序输出前k个
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        for i in range(k):
            for j in range(len(tinput) - 1, i, -1):
                if tinput[j] < tinput[j - 1]:
                    tinput[j], tinput[j - 1] = tinput[j - 1], tinput[j]

        return tinput[:k]
